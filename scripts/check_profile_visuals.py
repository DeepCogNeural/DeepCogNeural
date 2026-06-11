#!/usr/bin/env python3
"""Check GitHub profile SVG visuals for low-resolution embedded raster art.

This exists because an SVG wrapper can be sharp while an embedded PNG inside it
is blurry after GitHub/README scaling. The local preview uses an HTTP-served
HTML wrapper instead of file:// or a direct SVG URL, which Chrome automation may
block.
"""

from __future__ import annotations

import argparse
import base64
import contextlib
import html
import http.server
import os
from pathlib import Path
import re
import socket
import socketserver
import subprocess
import threading
import urllib.request


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SVG = REPO_ROOT / "assets" / "skills-map.svg"
DEFAULT_MIN_SCALE = 2.0


def read_png_size(data: bytes) -> tuple[int, int]:
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("not a PNG")
    return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")


def attr(tag: str, name: str) -> str | None:
    match = re.search(rf'\b{name}\s*=\s*["\']([^"\']+)["\']', tag)
    return match.group(1) if match else None


def float_attr(tag: str, name: str) -> float | None:
    value = attr(tag, name)
    if not value:
        return None
    match = re.match(r"([0-9.]+)", value)
    return float(match.group(1)) if match else None


def decode_image_href(href: str, base_dir: Path) -> tuple[str, tuple[int, int]]:
    if href.startswith("data:image/png;base64,"):
        data = base64.b64decode(href.split(",", 1)[1])
        return "embedded PNG", read_png_size(data)
    if href.lower().endswith(".png"):
        path = (base_dir / href).resolve()
        return str(path), read_png_size(path.read_bytes())
    raise ValueError(f"unsupported image href: {href[:80]}")


def check_svg(svg_text: str, label: str, min_scale: float, base_dir: Path) -> list[str]:
    failures: list[str] = []
    image_tags = re.findall(r"<image\b[^>]*>", svg_text)
    if not image_tags:
        failures.append(f"{label}: no SVG <image> tags found")
        return failures

    print(f"{label}: found {len(image_tags)} SVG image tag(s)")
    for idx, tag in enumerate(image_tags, start=1):
        href = attr(tag, "href") or attr(tag, "xlink:href")
        display_w = float_attr(tag, "width")
        display_h = float_attr(tag, "height")
        if not href or not display_w or not display_h:
            failures.append(f"{label} image {idx}: missing href/width/height")
            continue

        try:
            source, (pixel_w, pixel_h) = decode_image_href(href, base_dir)
        except Exception as exc:  # noqa: BLE001 - report exact visual-check issue.
            failures.append(f"{label} image {idx}: {exc}")
            continue

        scale_w = pixel_w / display_w
        scale_h = pixel_h / display_h
        print(
            f"{label} image {idx}: {source}; pixels={pixel_w}x{pixel_h}; "
            f"display={display_w:g}x{display_h:g}; scale={scale_w:.2f}x/{scale_h:.2f}x"
        )
        if scale_w < min_scale or scale_h < min_scale:
            failures.append(
                f"{label} image {idx}: raster scale below {min_scale:.1f}x "
                f"({scale_w:.2f}x/{scale_h:.2f}x)"
            )

    return failures


def check_local(svg_path: Path, min_scale: float) -> list[str]:
    svg_text = svg_path.read_text(encoding="utf-8")
    return check_svg(svg_text, str(svg_path.relative_to(REPO_ROOT)), min_scale, svg_path.parent)


def check_github_raw(url: str, min_scale: float) -> list[str]:
    with urllib.request.urlopen(url, timeout=20) as response:
        svg_text = response.read().decode("utf-8")
    return check_svg(svg_text, url, min_scale, REPO_ROOT)


class PreviewHandler(http.server.SimpleHTTPRequestHandler):
    preview_svg = "/assets/skills-map.svg"

    def log_message(self, format: str, *args: object) -> None:
        return

    def do_GET(self) -> None:  # noqa: N802 - stdlib callback name.
        if self.path in {"/", "/__visual_preview__.html"}:
            markup = f"""<!doctype html>
<meta charset="utf-8">
<title>DeepCogNeural visual preview</title>
<style>
  body {{ margin: 0; background: #f8f1e4; }}
  main {{ max-width: 1600px; margin: 0 auto; }}
  img {{ display: block; width: 100%; height: auto; }}
</style>
<main>
  <img src="{html.escape(self.preview_svg)}" alt="Core skills map">
</main>
"""
            data = markup.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        super().do_GET()


def free_port() -> int:
    with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def run(cmd: list[str], cwd: Path) -> str:
    result = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, timeout=45, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stdout + result.stderr)
    return result.stdout + result.stderr


def playwright_cli() -> Path:
    path = Path.home() / ".codex" / "skills" / "playwright" / "scripts" / "playwright_cli.sh"
    if not path.exists():
        raise FileNotFoundError(f"missing Playwright CLI wrapper: {path}")
    return path


def preview_screenshot(output: Path, width: int, height: int) -> None:
    port = free_port()
    handler = lambda *args, **kwargs: PreviewHandler(*args, directory=str(REPO_ROOT), **kwargs)
    server = socketserver.ThreadingTCPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    session = f"profile-visual-{os.getpid()}"
    cli = playwright_cli()
    url = f"http://127.0.0.1:{port}/__visual_preview__.html"
    try:
        run(["bash", str(cli), f"-s={session}", "open", url, "--headed"], REPO_ROOT)
        run(["bash", str(cli), f"-s={session}", "resize", str(width), str(height)], REPO_ROOT)
        eval_output = run(
            [
                "bash",
                str(cli),
                f"-s={session}",
                "eval",
                "() => JSON.stringify({"
                "images:[...document.images].map(img=>({complete:img.complete,naturalWidth:img.naturalWidth,naturalHeight:img.naturalHeight,"
                "rect:{width:Math.round(img.getBoundingClientRect().width),height:Math.round(img.getBoundingClientRect().height)}})),"
                "overflowX:document.body.scrollWidth>document.documentElement.clientWidth+2,"
                "bodyW:document.body.scrollWidth,clientW:document.documentElement.clientWidth})",
            ],
            REPO_ROOT,
        )
        run(["bash", str(cli), f"-s={session}", "screenshot", "--filename", str(output), "--full-page"], REPO_ROOT)
        print(f"preview screenshot: {output}")
        print(eval_output)
    finally:
        with contextlib.suppress(Exception):
            run(["bash", str(cli), f"-s={session}", "close"], REPO_ROOT)
        server.shutdown()
        server.server_close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--svg", type=Path, default=DEFAULT_SVG, help="local SVG to inspect")
    parser.add_argument("--min-scale", type=float, default=DEFAULT_MIN_SCALE, help="minimum raster/display scale")
    parser.add_argument("--github-raw", help="raw GitHub SVG URL to inspect after push")
    parser.add_argument("--preview", type=Path, help="write a browser preview screenshot to this PNG path")
    parser.add_argument("--preview-width", type=int, default=1600)
    parser.add_argument("--preview-height", type=int, default=760)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    failures = check_local(args.svg.resolve(), args.min_scale)
    if args.github_raw:
        failures.extend(check_github_raw(args.github_raw, args.min_scale))
    if args.preview:
        preview_screenshot(args.preview.resolve(), args.preview_width, args.preview_height)

    if failures:
        print("\nFAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nPASS: visual raster density checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

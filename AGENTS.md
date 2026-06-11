# DeepCogNeural Agent Rules

## Visual Assets

- Public GitHub profile visuals must be checked as rendered assets, not just edited as source.
- SVG can still be blurry if it embeds a low-resolution raster image. Always inspect embedded `data:image/*` or linked PNG/JPEG dimensions and compare them with the displayed SVG `<image width height>`.
- For README/profile images, embedded or linked raster art should be at least 2x the displayed size. Use vector/SVG for text whenever possible.
- Do not use Chrome `file://` or direct local SVG URLs for the final local check. Chrome automation may block those surfaces. Use a local HTTP preview page that wraps the SVG in normal HTML, then screenshot that page.
- After push, verify the actual GitHub profile page when feasible. If GitHub image caching is suspected, also verify the raw SVG on GitHub and parse the embedded raster dimensions.

Recommended local command:

```bash
python3 scripts/check_profile_visuals.py --preview /tmp/skills-map-preview.png --github-raw https://raw.githubusercontent.com/DeepCogNeural/DeepCogNeural/main/assets/skills-map.svg
```

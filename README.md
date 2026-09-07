# Linghao Xu

**Quantitative research · Market microstructure · Statistical inference**

I build probabilistic models and research systems for decisions under uncertainty: from stochastic neural dynamics to market making and execution. I am a computational neuroscience Ph.D. researcher at **Albert Einstein College of Medicine**, with a minor in applied mathematics and statistics and a B.S. in mathematics.

My primary focus is **quantitative research and trading**. I also work on causal experiments in machine learning and practical research tools.

[Quant projects](#quantitative-research--trading) · [Research](#mathematical-research) · [Merged contributions](#open-source-contributions) · [Email](mailto:linghaoxu11@gmail.com)

## Quantitative research & trading

### [Binary-options market making](https://github.com/DeepCogNeural/quant-trading-challenge-2026-case-study)

A Python market maker combining rate-transition models, conditional return distributions, and cross-company residual covariance. Estimated probabilities become quotes and sizes subject to uncertainty, inventory, and capital limits.

**Akuna Challenge 2026: 15.70/16 strategy points · 20/20 evaluation cases passed · zero bankruptcies.** These are captured simulation results, not a competition ranking or live return. The public case study covers the modeling approach and results without disclosing challenge materials or submission code.

### [Market microstructure lab](https://github.com/DeepCogNeural/microstructure-lab)

An open-source research scaffold for central limit order books: deterministic Level-2 replay, features available at decision time, future-midpoint labels, purged walk-forward evaluation, and negative controls. A visible-depth cost sweep makes execution assumptions explicit.

**What it demonstrates:** data causality, reproducible event reconstruction, and cost-aware evaluation. The shipped sample is synthetic; it establishes pipeline behavior rather than trading profitability.

### Independent trading research

I develop and operate a prediction-market research and execution system, with settlement-based evaluation, inventory-aware market making, and post-trade attribution. My research asks whether an apparent entry signal survives uncertainty analysis, and separates trading outcomes from venue incentives.

I have also traded SK Hynix relative value across Korean shares, USD-settled perpetual futures, and the U.S. ADR, studying funding, hedge construction, convergence, and financing constraints. Trading code and account records remain private.

## Mathematical research

My research centers on **stochastic processes, latent-state inference, and likelihood-based estimation**. In Ruben Coen-Cagli's lab, I develop continuous-time normalization models with stochastic input and volatility, derive moment approximations, and fit response dynamics to neural data.

- **[Probabilistic segmentation & neural dynamics](https://github.com/DeepCogNeural/sun-v1-segmentation-uncertainty)** — public research code connecting natural-image structure, inferred uncertainty, and early visual cortical dynamics.
- **[Bayesian observer models](https://github.com/DeepCogNeural/bayesian-heading-observer)** — efficient sensory encoding, Bayesian inference, and perception-to-action mapping; Python demo and original MATLAB code from my perception research with Alan Stocker at UPenn.

**Selected publications:** co-first author, [*PLOS Computational Biology* (2025)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1013147), on response-range-dependent heading biases; first author, [*Journal of Vision* (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9652722/), on serial dependence in heading perception.

## Open-source contributions

**Four merged external upstream PRs** across prediction-market infrastructure and node tooling. Status checked September 7, 2026.

| Project | Contribution | Merged PRs |
| :--- | :--- | :--- |
| **PMXT** | SDK alias compatibility and forwarding optional order parameters | [#1064](https://github.com/pmxt-dev/pmxt/pull/1064), [#1065](https://github.com/pmxt-dev/pmxt/pull/1065), [#1290](https://github.com/pmxt-dev/pmxt/pull/1290) |
| **Filecoin Lotus** | CLI warning when an API flag overrides the configured listen address | [#13670](https://github.com/filecoin-project/lotus/pull/13670) |

<details>
<summary>Other contributions and current status</summary>

- **Open:** Stratum V2 [#2211](https://github.com/stratum-mining/stratum/pull/2211) and companion [sv2-apps #584](https://github.com/stratum-mining/sv2-apps/pull/584); Polymarket CLI [#83](https://github.com/Polymarket/polymarket-cli/pull/83); The Graph [#2141](https://github.com/graphprotocol/graph-tooling/pull/2141); rust-bitcoin [#170](https://github.com/rust-bitcoin/bitcoind/pull/170).
- **Closed, not merged:** cryptofeed [#1115](https://github.com/bmoscon/cryptofeed/pull/1115) and [#1116](https://github.com/bmoscon/cryptofeed/pull/1116).
- **Collaboration project:** ColaMD search and LaTeX support, merged [#14](https://github.com/marswaveai/ColaMD/pull/14); listed separately from the four upstream PRs above.

Statuses are a dated snapshot, not a live feed.

</details>

## ML experiments & research tools

**[Mechanistic interpretability lab](https://github.com/DeepCogNeural/mech-interp-lab)** — causal interventions in GPT-2-small, matched controls, and explicit decision rules. The public record includes null and inconclusive results alongside a bounded causal-subspace study; compact evidence is available, while full reruns require additional source artifacts.

Tools I build for research workflows: **[taskdone-runner](https://github.com/DeepCogNeural/taskdone-runner)** for background-task notifications and review tracking; **[HTML report skill](https://github.com/DeepCogNeural/html-artifact-report-skill)** for readable reports with structured evidence; **[Codex Quota Bar](https://github.com/DeepCogNeural/codex-quota-bar)** for a native macOS view of subscription quotas ([interactive preview](https://codex-quota-bar.sheyajane.chatgpt.site/)).

## Recent updates

- **September 2026:** published taskdone-runner and added Codex Quota Bar to the public tool portfolio.
- **August 2026:** published the [quant trading challenge case study](https://github.com/DeepCogNeural/quant-trading-challenge-2026-case-study) and expanded the [causal-subspace research record](https://github.com/DeepCogNeural/mech-interp-lab/tree/main/experiments/05_number_agreement_circuit).
- **June–July 2026:** four upstream PRs merged into PMXT and Filecoin Lotus.

---

**Core tools:** Python · NumPy / SciPy / pandas · SQL · PyTorch · MATLAB / R  
**Engineering contributions:** TypeScript · Go  
**Contact:** [linghaoxu11@gmail.com](mailto:linghaoxu11@gmail.com) · Ph.D. expected December 2027

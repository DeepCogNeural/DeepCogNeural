# Linghao Xu

**Computational neuroscience · Bayesian inference · Quantitative research**

I am a **Computational Neuroscience Ph.D. researcher at Albert Einstein College of Medicine**, with a B.S. in mathematics and a minor in applied mathematics and statistics. My primary focus is **computational neuroscience and probabilistic modeling**, with applications to quantitative research and market microstructure.

[Academic research](#academic-research) · [Market microstructure](#market-microstructure-lab) · [Open source](#open-source-contributions)

**Published work:** [PLOS Computational Biology (2025)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1013147) · [Journal of Vision (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9652722/)

## Academic Research

I use Bayesian models to understand how sensory uncertainty, prior experience, and response mapping shape perception and decisions.

- **Co-first author, PLOS Computational Biology (2025):** explained response-range-dependent heading biases with an efficient Bayesian observer and a perception-to-action mapping.
- **First author, Journal of Vision (2022):** separated perceptual and postperceptual contributions to serial dependence in heading judgments.

[Bayesian Heading Observer — Python demo and original MATLAB code](https://github.com/DeepCogNeural/bayesian-heading-observer)

## Market Microstructure Lab

**85.8 million order messages · Python + C++20**

Reconstructed limit order books for five Warsaw Stock Exchange equities and evaluated forecasts, crossing costs, and conditional passive fills. Positive prediction scores did **not** survive visible spread costs—a central finding of the historical study. The C++ replay backend matched Python outputs exactly and ran **8.98× faster on the fixed replay benchmark**.

[Research, results & code](https://github.com/DeepCogNeural/microstructure-lab)

## Open-source contributions

| Project | Contribution | Public record |
| :--- | :--- | :--- |
| **cryptofeed** | Fixed Poloniex trade quantities and processing of batched trade messages | Merged: [#1139](https://github.com/bmoscon/cryptofeed/pull/1139) |
| **PMXT** | Prediction-market SDK compatibility and optional order parameters | Merged: [#1064](https://github.com/pmxt-dev/pmxt/pull/1064), [#1065](https://github.com/pmxt-dev/pmxt/pull/1065), [#1290](https://github.com/pmxt-dev/pmxt/pull/1290) |
| **Filecoin Lotus** | CLI diagnostics when a flag overrides the configured API address | Merged: [#13670](https://github.com/filecoin-project/lotus/pull/13670) |
| **ColaMD** (collaboration project) | Search and LaTeX support | Merged: [#14](https://github.com/marswaveai/ColaMD/pull/14) |

**In development:** [array-api-extra #1001](https://github.com/data-apis/array-api-extra/pull/1001) — proposed one-dimensional interpolation across Array API namespaces. Draft PR; not yet merged.

### Codex Quota Bar

Built an open-source **CodexBar + Subrouter integration** for monitoring multiple Codex subscription accounts on macOS. The optional native integration adds quota bars and **manual subscription-account selection for new chats**; routing is handled by Subrouter.

[Product website](https://codex-quota-bar.sheyajane.chatgpt.site/) · [Source & installation](https://github.com/DeepCogNeural/codex-quota-bar)

**Other tools:** [taskdone-runner](https://github.com/DeepCogNeural/taskdone-runner), background-task notifications and review tracking; [HTML report skill](https://github.com/DeepCogNeural/html-artifact-report-skill), readable research reports with structured evidence.

My independent trading work spans prediction-market execution and cross-market relative value, with attention to settlement, hedging, inventory, and financing constraints.

---

**Tools:** Python · C++ · SQL · NumPy / SciPy / pandas · PyTorch · MATLAB  
Ph.D. expected December 2027

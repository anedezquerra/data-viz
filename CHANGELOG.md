# Changelog

- Unreleased: chore(packaging): switch to dynamic version (single source of truth in `dataviz/__init__.py`), drop EOL Python 3.8, add upper bounds on runtime deps, declare `export` extra (`kaleido`), ship `py.typed` PEP 561 marker, add `MANIFEST.in`.
- Unreleased: chore(ci): add cross-platform `tests.yml` (Linux/macOS/Windows × Python 3.9–3.12) running pytest + coverage + lint + build + clean-install smoke test; add `release.yml` for tag-driven GitHub Releases with optional PyPI Trusted Publishing.
- Unreleased: chore(security): add `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `.github/dependabot.yml` (weekly pip + actions updates, grouped).
- Unreleased: docs: add install-from-GitHub instructions in README and getting_started page; document the `export` extra.

- Unreleased: docs: overhaul `getting_started.rst` with quickstart, install matrix, return-value contract, and troubleshooting; add `sphinx-copybutton` and `sphinx-design`.
- Unreleased: Expanded bivariate, SPC, and comprehensive univariate suites; added shared validation/type helpers, typed Google-style docstrings, and executable SPC API examples with professional four-image gallery placeholders.
- 0.1.0: Initial DataViz package with static and interactive chart modules for EDA, univariate, bivariate, multivariate, SPC, ML diagnostics, and XAI.

# DataViz — Copilot Instructions

Python data visualization package with modular organization, dual rendering backends (matplotlib/plotly), and ML/statistical diagnostics.

## Core Architecture

**Dual-Mode Pattern**: Every chart function has `_static` (matplotlib/seaborn) and `_interactive` (plotly) variants with identical signatures. A convenience default alias (no suffix) points to `_static`. Example: `dv.histogram()` → `histogram_static()`, `dv.histogram_interactive()`.

**Module Organization** (in `dataviz/`):
- **univariate/** — histograms, density, box plots, diagnostics, fits, bootstrap
- **bivariate/** — scatter, line, correlation, joint plots, categorical relationships
- **multivariate/** — heatmaps, parallel coordinates, PCA, 3D plots
- **eda/** — missing data, distribution summaries, class balance
- **spc/** — control charts, run charts, Levey-Jennings, trend analysis (20+ families)
- **regression/** — residuals, partial residuals, influence, diagnostics, learning curves (160+ families)
- **classification/** — confusion, ROC, PR, calibration, fairness, multilabel (72+ families)
- **clustering/** — scatter clusters, dendrograms, elbow, silhouette
- **xai/** — SHAP, importance (permutation, grouped, drop-column), PDP, ICE, ALE, LIME (66+ families)
- **types.py** — Shared type aliases (`ArrayLike`, `MatrixLike`, `MatplotlibAxes`, `PlotlyFigure`)
- **utils/** — Validation, error handling, theme utilities

**Re-export Pattern**: Each module's `__init__.py` imports both `_static` and `_interactive` versions, plus a convenience default alias. The top-level `dataviz/__init__.py` re-exports the full public API.

## Build, Test, Lint

**Install (development)**:
```bash
pip install -e ".[dev,docs]"
```

**Run locally before opening a PR** (same commands run in CI):
```bash
black --check dataviz tests              # Format check
flake8 dataviz tests                     # Lint
mypy dataviz                             # Type check
pytest --cov=dataviz --cov-report=term-missing  # Test with coverage
```

**Rebuild Sphinx documentation**:
```bash
python -m sphinx -b html -W --keep-going docs/source docs/build/html
```

**Single test** (not full suite):
```bash
pytest tests/test_univariate_core.py::test_histogram_static -v
```

## Key Conventions

**Code Style & Comments**:
- Minimal comments; one short line maximum for non-obvious logic only.
- No narration, decorative banners, or ASCII headers.
- Match existing formatting (Black line-length 88, indentation 4).
- Use type hints; Google-style docstrings with `Args`, `Returns`, `Raises`, `Example`.
- Clear identifiers; single-letter names only for trivial loop indices.
- Avoid dead code (commented-out code, unused imports, debug prints).

**Python Version**: >=3.9 (check `pyproject.toml`)

**Dependencies** (from `pyproject.toml`):
- **Runtime**: matplotlib >=3.9.4,<3.11; seaborn >=0.13.2; numpy >=2.0.2; pandas >=2.3.3; plotly >=5.0,<7; scipy >=1.13.1
- **Dev**: pytest, pytest-cov, black, flake8, mypy, build, twine
- **Docs**: sphinx >=8.0, sphinx-rtd-theme >=3.0, sphinx-copybutton, sphinx-design
- **Export**: kaleido (for Plotly static image export)

**Naming & Branches**:
- Functions: snake_case with `_static` / `_interactive` suffixes.
- Branches: `<type>/<description>` (no personal names). Types: `feat/`, `fix/`, `docs/`, `chore/`, `refactor/`, `test/`.
- Include issue ID when available: `feat/123-spc-cusum-chart`.

**Commits & Changelog**:
- Conventional Commits format: `<type>(<scope>): <subject>` (imperative, lowercase, max 72 chars, no period).
- Changelog entries (in `CHANGELOG.md` under `Unreleased`) are single-line summaries: `- <type>: <what changed>`.
- Detailed rationale, migration steps, and examples belong in `README.md`, not CHANGELOG.

**Adding a New Chart**:
1. Place `chart_name_static(...)` and `chart_name_interactive(...)` in appropriate module (e.g., `dataviz/univariate/histogram.py`).
2. Both versions must have identical parameter signatures and return correct types (`plt.Axes` vs. `go.Figure`).
3. Export both from module `__init__.py`; add convenience alias (default to static).
4. Add tests for both variants in `tests/` (smoke tests and edge cases).
5. Add docstring with `Args`, `Returns`, `Raises`, `Example`.
6. If adding top-level convenience import, update `dataviz/__init__.py`.
7. Update `CHANGELOG.md` with a single-line entry.

**Error Handling**:
- Validate inputs at boundaries; raise specific errors with actionable messages.
- Catch specific exception types, not bare `except`.
- Preserve root-cause context and stack traces (use `raise ... from e` where appropriate).

**No Over-Engineering**: 
- Solve only the stated problem.
- Prefer simplest solution; avoid speculative abstractions, plugins, or premature optimization.
- Reuse existing patterns; do not invent new ones.

## Files to Know

- `README.md` — canonical source for usage, rationale, configuration, examples, migration steps
- `CONTRIBUTING.md` — setup, QA commands, branch naming, commit format, PR structure
- `AGENTS.md` — detailed Copilot/agent rules (response style, code quality, no over-engineering)
- `pyproject.toml` — dependencies, versions, tool configuration (Black, pytest, mypy, coverage)
- `.github/workflows/tests.yml` — CI pipeline (format, lint, type-check, test, build across Linux/macOS/Windows × Python 3.9–3.12)
- `.github/dependabot.yml` — weekly pip and Actions updates (grouped, pinned ranges)

## Example Workflow

1. Pick a module (e.g., `univariate`).
2. Create `def chart_name_static(...)` and `def chart_name_interactive(...)`.
3. Export in module `__init__.py`; alias default to static.
4. Test: `pytest tests/test_univariate_core.py -v`.
5. Lint/format: `black dataviz tests && flake8 dataviz tests && mypy dataviz`.
6. Update `CHANGELOG.md` and commit: `feat(univariate): add chart_name function`.
7. Push to branch and open PR with detailed summary.



# Security Policy

## Supported Versions

DataViz is in early-stage development. Only the latest release on the `main`
branch receives security fixes.

| Version | Supported |
| ------- | --------- |
| `main`  | ✅        |
| `< 0.1` | ❌        |

## Reporting a Vulnerability

Please **do not open public GitHub issues** for security vulnerabilities.

Instead, report privately through GitHub's
[private vulnerability reporting](https://github.com/anedezquerra/data-viz/security/advisories/new)
form. Include:

* A description of the vulnerability and its impact.
* Steps to reproduce, ideally with a minimal code sample.
* Affected versions or commit SHAs.
* Any suggested mitigation, if known.

You should receive an acknowledgement within five business days. Coordinated
disclosure timelines are negotiated case by case but generally do not exceed
90 days from the initial report.

## Scope

In scope:

* The `dataviz` Python package and its public API.
* Documentation that ships with the repository.
* Release artifacts published from this repository.

Out of scope:

* Vulnerabilities in upstream dependencies (matplotlib, plotly, pandas,
  numpy, scipy, seaborn) — report those to their respective maintainers.
* Findings against forks or modified copies of this repository.

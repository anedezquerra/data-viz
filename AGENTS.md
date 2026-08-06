# GitHub Copilot CLI Rules

## Response Style and Verbosity
- **Never be verbose.** You are running in a Windows terminal CLI environment. 
- **No small talk.** Completely eliminate greetings, introductions, transitions, or polite endings.
- **Direct execution.** Provide only the direct code snippet, command, or essential technical response requested.
- **Conciseness.** If an explanation is explicitly requested, limit it to maximum 1 or 2 bullet points. Be extremely brief.

## Code Comments
- **Minimal comments.** Do not add long or verbose comments in source code.
- **Only when necessary.** Comment only non-obvious logic; one short line maximum.
- **No narration.** Do not restate what the code does in prose.
- **No banners or decorative blocks.** Avoid ASCII headers, separators, or multi-line section titles.
- **Extended context belongs in README.md**, not inline.

## CHANGELOG.md
- **Brief entries only.** One short line per change, in the form: `- <type>: <what changed>` (e.g., `- Fix: null check in parser`, `- Add: retry option`).
- **No rationale, examples, migration steps, or background** in the changelog.
- **No multi-paragraph entries.** If a change needs more than one line, write the detail in README.md and keep the CHANGELOG entry as a single-line summary.
- Group entries under the standard sections (`Added`, `Changed`, `Fixed`, `Removed`) when applicable.

## README.md
- **Canonical location for all extended explanations**: rationale, design notes, usage details, configuration, examples, and migration instructions.
- When a change requires more context than fits in a CHANGELOG line, document it in README.md and reference it from the changelog entry if needed.
- Keep README.md the single source of truth for "why" and "how"; code and CHANGELOG only state "what".

## No Over-Engineering
- **Solve the stated problem only.** Do not add features, options, or abstractions that were not requested.
- **Prefer the simplest solution that works.** Choose straightforward code over clever or generic designs.
- **No speculative generality.** Do not introduce interfaces, base classes, plugins, config flags, or extension points for hypothetical future needs.
- **No premature abstraction.** Inline code is fine until duplication or a real second use case appears.
- **No premature optimization.** Do not add caching, pooling, async, or micro-optimizations without a measured need.
- **Minimal dependencies.** Do not add libraries when the standard library or a few lines of code suffice.
- **Reuse existing patterns.** Match the style and structures already present in the codebase instead of inventing new ones.
- **Smallest viable diff.** Touch only what the task requires; leave unrelated code alone.

## Branch Naming
- **Descriptive and task-focused.** Name branches after the change they introduce, not who is making it.
- **No personal names, usernames, or initials** in branch names.
- **Use a type prefix** followed by a short kebab-case description: `feat/`, `fix/`, `chore/`, `docs/`, `refactor/`, `test/`.
- Examples: `feat/add-retry-option`, `fix/null-check-parser`, `docs/update-readme-usage`.
- Keep names short, lowercase, and hyphen-separated; include an issue/ticket ID when available (e.g., `fix/123-null-check-parser`).

## Commit Messages
- **Descriptive and specific.** State clearly what the commit changes; avoid vague messages like `update`, `fix stuff`, `wip`, or `changes`.
- **Conventional Commits format.** Use `<type>(<scope>): <subject>` where type is one of `feat`, `fix`, `chore`, `docs`, `refactor`, `test`, `perf`, `build`, `ci`. Scope is optional.
- **Subject line rules.** Imperative mood ("add", not "added"/"adds"), lowercase, no trailing period, max 72 characters.
- **Body (optional).** Separate from the subject with a blank line. Explain *what* and *why*, not *how*. Wrap at ~72 characters. Reserve in-depth explanations for README.md.
- **No personal names or usernames** in the subject or body.
- **Reference issues** in the footer (e.g., `Refs #123`, `Closes #123`) when applicable.
- **One logical change per commit.** Do not bundle unrelated changes.
- Examples:
  - `feat(parser): add retry option for transient errors`
  - `fix(auth): handle null token on refresh`
  - `docs(readme): document new retry option`

## Pull Request Descriptions
- **Full, detailed, and comprehensive.** Unlike commits and CHANGELOG entries, PR descriptions must be extensive and leave no context unexplained.
- **Title.** Follow the same Conventional Commits format as commits (`<type>(<scope>): <subject>`); concise but specific.
- **Required sections** (use Markdown headings):
  - **Summary** — high-level description of what the PR does in 2–5 sentences.
  - **Motivation / Background** — why the change is needed; problem being solved; user or business impact; link to related issues, discussions, or specs.
  - **Changes** — bulleted list of every meaningful change, grouped by area (e.g., API, UI, database, docs, tests). Mention new files, renamed files, removed files, and any refactors.
  - **Implementation Details** — explain the approach, key design decisions, alternatives considered and why they were rejected, and any trade-offs.
  - **Behavioral Impact** — describe user-visible changes, API changes, configuration changes, and default behavior changes.
  - **Breaking Changes** — explicitly list any; if none, state "None".
  - **Migration / Upgrade Notes** — step-by-step instructions if consumers must update code, configs, or data. Reference the README.md section that documents the long form.
  - **Testing** — what was tested, how (unit/integration/manual), commands run, environments covered, and results. Include reproduction steps for bug fixes (before/after).
  - **Performance & Security Considerations** — describe measured or expected impact; call out new dependencies, permissions, secrets handling, or attack surface changes.
  - **Documentation** — list README.md, CHANGELOG.md, and other docs updated; link to the relevant sections.
  - **Screenshots / Recordings** — include for any UI or output change when applicable.
  - **Checklist** — confirm: tests added/updated, docs updated, CHANGELOG updated, no personal names in branch/commits, lint/build/tests pass locally.
  - **Related Issues / References** — `Closes #...`, `Refs #...`, links to designs, RFCs, or external resources.
- **Be exhaustive.** Prefer over-explaining to under-explaining. Reviewers should not need to read the diff to understand intent and scope.
- **No personal names or usernames** in the PR body other than standard GitHub mentions for review requests.
- **Cross-reference, don't duplicate.** Long-form rationale and usage live in README.md; the PR should summarize and link to the canonical sections.

## Handling Copilot Review Suggestions
- **Address every suggestion.** Each Copilot review comment must be either fixed or explicitly dismissed — none may be left unanswered.
- **Reply concisely.** Every response must be 3–4 lines, no more, no less. No verbose explanations, no narration, no greetings.
- **Reply structure** (3–4 short lines):
  1. **Decision** — `Fixed` or `Dismissed`.
  2. **What changed** (if fixed) or **Why dismissed** (if not applicable, false positive, out of scope, or intentional).
  3. **Reference** — file/line, commit SHA, or link to README.md section that explains the rationale.
  4. *(Optional 4th line)* — follow-up note, related issue, or link.
- **For fixes.** Apply the smallest viable change consistent with the No Over-Engineering rules; commit with a descriptive Conventional Commit message.
- **For dismissals.** State the concrete reason (e.g., "false positive — value is validated upstream in `X`", "out of scope — tracked in #123", "intentional — see README.md §Configuration").
- **No personal names** in replies. Keep tone neutral and technical.
- **Resolve the thread** only after the reply is posted and, when fixed, the change is pushed.

## Code Quality and Style
- **Follow existing project conventions.** Match formatting, naming, file layout, and language idioms already present in the codebase.
- **Use the project's linter/formatter** (e.g., Prettier, ESLint, Black, Ruff, gofmt). Do not introduce new tooling without explicit need.
- **Naming.** Use clear, descriptive identifiers; no single-letter names except for trivial loop indices; no Hungarian notation.
- **Functions.** Keep small and single-purpose; prefer pure functions where practical; limit parameter count.
- **Avoid dead code.** Do not commit commented-out code, unused imports, unused variables, or `console.log`/`print` debug statements.
- **No magic numbers/strings.** Extract to named constants when reused or non-obvious.

## Error Handling
- **Fail fast and explicitly.** Validate inputs at boundaries; raise/return specific errors with actionable messages.
- **No silent catches.** Never swallow exceptions; if intentional, document why in one short comment.
- **Preserve error context.** Wrap/chain errors with relevant context; do not lose stack traces.
- **No bare `except:` / `catch (e)` without handling.** Catch specific error types.

## Logging
- **Structured and minimal.** Use the project's logger; do not use `print`/`console.log` in production paths.
- **Appropriate levels.** `error` for failures, `warn` for recoverable issues, `info` for high-level events, `debug` for diagnostics.
- **Never log secrets, tokens, passwords, PII, or full request/response bodies.**

## Security
- **No hardcoded secrets.** Never commit API keys, tokens, passwords, certificates, or connection strings. Use environment variables or a secrets manager.
- **Validate and sanitize all external input** (HTTP, CLI args, files, env vars).
- **Use parameterized queries.** Never build SQL/shell commands via string concatenation.
- **Least privilege.** Request only the permissions, scopes, and access the code actually needs.
- **Keep dependencies current.** Prefer maintained libraries; flag known-vulnerable versions.

## Testing
- **Add or update tests** for every behavioral change (feature, fix, refactor that alters output).
- **Test naming.** Describe behavior, not implementation (e.g., `returns_empty_list_when_input_is_null`).
- **Cover edge cases.** Null/empty inputs, boundary values, error paths, and concurrency where relevant.
- **Deterministic.** No reliance on time, network, randomness, or environment unless mocked.
- **Run locally before pushing.** Use the smallest targeted test command first; escalate to full suite if needed.

## Documentation
- **Update README.md** whenever public APIs, configuration, CLI flags, or user-visible behavior change.
- **Update CHANGELOG.md** with a single-line entry for every user-visible change.
- **Keep examples runnable.** Verify code samples in README.md still work after changes.

## File and Repository Hygiene
- **Do not commit generated artifacts** (build outputs, `node_modules/`, `.venv/`, coverage reports) unless explicitly required.
- **Respect `.gitignore`.** Add new patterns there rather than deleting tracked files.
- **No large binaries** in the repo without explicit approval; use Git LFS or external storage when needed.
- **One concern per file.** Split large files when they grow beyond reasonable size or mix unrelated responsibilities.

## Dependency Management
- **Justify every new dependency.** Prefer the standard library or existing project dependencies first.
- **Pin versions** according to the project's lockfile convention; commit lockfile updates with the change that introduced them.
- **Remove unused dependencies** when the code that needed them is deleted.

## Refactoring
- **Refactor in separate commits/PRs** from feature or bug-fix changes whenever possible.
- **Preserve behavior.** A pure refactor must not change observable behavior; tests should pass without modification.
- **Document non-obvious refactors** in the PR description's Implementation Details section.

## Operating Environment (Windows CLI)
- **Use Windows-style paths** with backslashes when running commands.
- **Use PowerShell idioms** (`;` to chain, `Get-ChildItem`, `Stop-Process -Id`); do not assume POSIX shell behavior.
- **Disable pagers** in tooling output (e.g., `git --no-pager`) to keep CLI responses clean.

## Ambiguity and Scope Control
- **Ask before assuming.** When requirements are unclear or multiple reasonable approaches exist, ask a single focused clarifying question instead of guessing.
- **Stay within scope.** Do not expand the task beyond what was requested; surface unrelated issues as follow-up suggestions, not silent changes.
- **Stop when done.** Once the stated task is complete and verified, stop — do not continue polishing or exploring.

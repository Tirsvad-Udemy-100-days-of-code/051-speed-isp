# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [MIL-003], [QC-PY-001], [ADR-0001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version; review of the MIL-003 code deliverable (AI as stand-in for S01) | pending |

---

## Artifact Under Review

- Instance reviewed: MIL-003 code deliverable: `src/speed_isp/**`, `tests/**`, `pyproject.toml`, `docker/Dockerfile` ([MIL-003])
- Checklist used: [QC-PY-001] (`QC-PY-001`); recorded deviation: [ADR-0001] (criteria 10 and 17)
- Scope: full review, round 1 (one defect fixed during the review, then re-checked)
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing | Pass | `SocialSite`, `YSite`, `XSite`, `MissingCredentialsError` (PascalCase); `compose_complaint`, `create_site`, `wait_clickable` (snake_case); `UPPER_SNAKE` constants. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations | Pass | `Y_COMPOSER_SELECTOR`, `X_NEXT_XPATH`, `format_speed`. `down` and `up` are the assignment's names. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check src tests`: all checks passed; `ruff format --check`: 24 files already formatted. One suppression in the tree: `# type: ignore[misc]` in `tests/unit/test_speed.py`, which deliberately assigns to a frozen dataclass to test immutability; it names the error code and is the point of the test. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Covered by `mypy --strict` (criterion 12). |
| 5 | No bare `except:`, no swallowed exceptions; `raise ... from` | Pass | `YSite.login` and `XSite.login` catch only `TimeoutException` and raise `LoginError(...) from error`. The two cookie-banner helpers catch only `TimeoutException`, log, and continue by design (the banner is optional). `create_site` raises `MissingCredentialsError` or `ValueError` before any navigation. `cli.main` catches only the two named errors, logs the message and returns 1. No bare `except`, no `except Exception`. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | None present. |
| 7 | Files, locks and connections are managed with context managers | Pass | The browser is released by `try/finally: bot.close()` in `main`; same note as [RC-009] (an `__enter__`/`__exit__` would be cleaner, not required). The sites hold no resources of their own. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every module, class, protocol method and function has a Doxygen docstring. `doxygen Doxyfile`: 0 warnings, also after the fix. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` in `src`. Logged texts hold speeds, timeouts, "Logged in to Y/X" and "Posted on Y/X". `MissingCredentialsError` names the environment variables, never their values; `LoginError` texts hold no credential, e-mail or page content. Credentials go only to `send_keys`. `test_no_credential_value_appears_in_logs` asserts it. The complaint text is posted, not logged. Working-tree scan (`git grep`, `.env` not read) for assigned passwords, tokens and keys: only the README placeholder `"your-password"`. `.env` and `out/` are git-ignored. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No DCD; the deviation is recorded in [ADR-0001]. The new classes trace to tasks 2-4 of [MIL-003]. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `.venv/Scripts/python -m pytest -q`: 59 passed in about 2.2 s, no browser, no network (fake drivers). Covers the message (with and without handle, blank handle, exact limit, too long), Y and X login and post sequences, login timeout, missing credentials before navigation, unknown service, skip when the speed is fine, screenshots, and no credentials in logs. |
| 12 | Type checker runs in strict mode without errors | Pass | `mypy` (`strict = true`): no issues in 24 source files. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Optional. `selenium>=4.20` and `pytest>=8` are lower bounds, not pins; both are used. Carried over from [RC-009]; not blocking. |
| 14 | Each piece of knowledge is defined in one place | Pass | Round 1: the 280-character limit was defined twice (`COMPLAINT_MAX_LENGTH` in `domain/complaint.py` and the unused `POST_MAX_LENGTH` in `constants.py`). Fixed: the unused constant was removed; the domain owns the rule, so it does not import configuration. URLs, selectors, timeouts and environment names are in `constants.py`. `XSite` and `YSite` have similar constructors and `post` bodies but different selectors and login flows and change for different reasons; not merged, correctly. The screenshot literals `step-2-...` and `step-3-...` in `bot.py` are noted in [RC-009]; make them constants if a third use appears. |
| 15 | Imports point inward; no import cycles | Pass | `domain.speed` imports `dataclasses`; `domain.complaint` imports only `domain.speed` (stdlib only: no `constants`, no selenium). `application.run_bot` imports only the domain. `infrastructure` imports domain and `constants`; `presentation.cli` is the composition root. No cycles: `site_factory` imports `x_site`, `y_site` and `social_site`; the sites import `social_site` only. |
| 16 | SOLID holds | Pass | Single responsibility: composing the text is a domain function, the site flows are in `YSite` and `XSite`, selection is in `site_factory`, and the bot only orchestrates (the [RC-009] follow-up to move posting out of the bot is done). Open/closed and Liskov: `SocialSite` is a narrow protocol (`login`, `post`) and both sites honour it. Adding a service means a new class plus one branch in `create_site`; the `if/elif` on the service exists in one place only, not repeated. Dependency inversion, partly: `InternetSpeedTwitterBot` calls the module function `create_site`, so it depends on the concrete factory instead of an injected one; tests monkeypatch constants. Acceptable at this size; see Action Items. |
| 17 | Source is laid out in the clean architecture layers and folders, in `snake_case`, imports inward | Pass | `domain`, `application`, `infrastructure`, `presentation` under `src/speed_isp/`; `tests/unit`, `integration`, `e2e`. The `SocialSite` port lives in `infrastructure` next to its implementations, because only the infrastructure bot uses it; [ADR-0001] covers criteria 10 and 17 as the user asked. |
| 18 | File and folder names are English, no space, allowed characters, language casing | Pass | New files `complaint.py`, `site_factory.py`, `social_site.py`, `x_site.py`, `y_site.py`, `test_complaint.py`, `test_tweet_sites.py` and `docs/images/step-1-y-login.png` are English, use allowed characters and `snake_case`. |

## MIL-003 Go / No-Go criteria

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Message names measured and promised speeds, at most 280 characters | Pass | `compose_complaint` yields, for example, "Hey, why is my internet speed 94.7down/50.5up when I pay for 150down/10up?"; `test_complaint.py` checks the content, the default limit, the exact limit and the `ValueError` above it. |
| 2 | Credentials only from environment variables; none in the repository | Pass | `constants.py` reads `os.environ.get(...)` with an empty default. `git grep` for assigned secrets finds only the README placeholder. `.env` is git-ignored and was not read. |
| 3 | `python -m pytest` passes without browser or network | Pass | 59 passed, exit 0. |
| 4 | A run against Y posts the message, or the missing-credentials stop is recorded in the Open Issues | Pass, by the second alternative | `out/live-run-mil-003.log` shows a real measurement (97.32 Mbps down, 49.72 up) and then the clean stop "set the environment variables Y_EMAIL and Y_PASSWORD". The Project Plan's Open Issues already records that Y and X credentials are not available and that S01 supplies them. The first alternative (a post on Y) is not met. |
| 5 | Code reviewed against the Python checklist, `RC-*` is Go | Pass | This record. |

## Not verified live

- The Y login and post flow: the selectors were verified on the login page only (step-1 screenshot); login, composer and post were never run with real credentials, so the post itself is covered by the fake driver only.
- The X flow: the selectors are best effort and were never run against x.com. X may demand a CAPTCHA or e-mail confirmation, which the bot does not bypass (it stops with `LoginError`). `x_site.py` and `constants.py` say so.
- The screenshot `step-4-tweet-posted.png` does not exist yet.

## Overall Verdict

Go. Every Mandatory criterion of QC-PY-001 passes after the round 1 fix, and Go/No-Go rows 1-5 of [MIL-003] pass, row 4 by its second alternative only; the actual post on Y is still outstanding and is an action item. Criterion 13 is an Optional Fail and not blocking. Mode: autonomous, not independent (AI as stand-in for S01).

Changes made during the review: `src/speed_isp/constants.py` (removed the unused, duplicate `POST_MAX_LENGTH`). Re-run: 59 tests passed, ruff and mypy clean, doxygen 0 warnings. ruff and mypy were installed in `.venv` for the check and uninstalled again.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Supply `Y_EMAIL` and `Y_PASSWORD`, re-run the Docker live run and save `step-4-tweet-posted.png` and a log that shows the post (closes the unverified Y flow) | S01 | 2026-11-05 |
| Optional: verify or drop the X selectors if X is ever used | S01 | 2026-11-06 |
| Optional: pin Selenium and pytest (carried over from [RC-009]) | S01 | 2026-11-06 |
| Optional: inject the site factory into the bot (full dependency inversion) and give the bot `__enter__`/`__exit__` | S01 | 2026-11-06 |

---

[MIL-003]: ../../milestones/mil-003-tweet-bot.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[ADR-0001]: ../../adr/adr-0001-no-design-artifacts-for-a-one-class-script.md
[RC-009]: rc-009-mil-002-code.md

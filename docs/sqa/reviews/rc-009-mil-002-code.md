# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [MIL-002], [QC-PY-001], [ADR-0001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version; review of the MIL-002 code deliverable (AI as stand-in for S01) | [39813c3] |

---

## Artifact Under Review

- Instance reviewed: MIL-002 code deliverable: `src/speed_isp/**`, `tests/**`, `pyproject.toml`, `Doxyfile`, `docker/Dockerfile` ([MIL-002])
- Checklist used: [QC-PY-001] (`QC-PY-001`); recorded deviation: [ADR-0001] (criteria 10 and 17)
- Scope: full review, round 1 (two documentation defects fixed during the review, then re-checked)
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing | Pass | `InternetSpeedTwitterBot`, `SpeedResult` (PascalCase); `get_internet_speed`, `parse_mbps` (snake_case); `UPPER_SNAKE` constants. The assignment's method names are kept. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations | Pass | `SPEEDTEST_DONE_XPATH`, `SCREENSHOT_SETTLE_SECONDS`, `parse_mbps`. `down` and `up` are the assignment's names, explained in the Doxygen comments. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check src tests`: all checks passed; `ruff format --check`: 17 files formatted. No `noqa` or `type: ignore` in the tree. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Covered by `mypy --strict` (criterion 12); test helpers and fakes are annotated. |
| 5 | No bare `except:`, no swallowed exceptions; `raise ... from` | Pass | `_reject_cookies` catches only `TimeoutException`, logs "No cookie banner shown" and continues by design (banner is optional). `parse_mbps` re-raises `ValueError ... from error`. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | None present. |
| 7 | Files, locks and connections are managed with context managers | Pass | The browser is the only resource; `main` releases it with `try/finally: bot.close()`, which is equivalent. Note: a `__enter__`/`__exit__` on the bot would be cleaner; not required. The screenshot file is written by the driver, not opened by the code. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every module, class and function has a Doxygen docstring. Round 1: `doxygen Doxyfile` gave 158 warnings. 156 came from a broken `FILE_PATTERNS` in `Doxyfile` (the default pattern list was left under `*.py` without line continuations). Fixed by removing the stray lines. 2 came from `@var` in `SpeedResult`, which Doxygen read as a declaration of `Mbps`. Fixed by describing the attributes in prose. `doxygen Doxyfile` now prints no warning. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `logging` only; the logged texts hold speeds and timeouts only. Credentials are read from the environment (`constants.py`) and never logged. Working-tree scan for assigned passwords, tokens and key patterns (`.env` excluded, not read): none found. `.env` and `out/` are git-ignored (`git check-ignore`). |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No DCD exists; the deviation is recorded in [ADR-0001]. The classes trace to the lecture steps 2 and 3 in [MIL-002]. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `python -m pytest -q`: 29 passed in 1.2 s, with a hand-written fake driver, no browser, no network. Timeouts are patched small; screenshots go to `tmp_path`. Covers the timeout path, the missing cookie banner and the use-case order. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy` (`strict = true`): no issues in 17 source files. `cast(WebDriver, driver)` in the tests is the single concession to the fake driver. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Optional. `selenium>=4.20` and `pytest>=8` are lower bounds, not pins. Selenium is now used. Carried over from [RC-008]; not blocking. |
| 14 | Each piece of knowledge is defined in one place | Pass | URLs, XPaths, timeouts and paths are in `constants.py`. Note: the two screenshot file names exist as literals in `bot.py` and as the lecture's step names in the tests and docs; acceptable, but make them constants if a third use appears. |
| 15 | Imports point inward; no import cycles | Pass | `domain.speed` imports only `dataclasses`; `application.run_bot` imports only the domain (the bot is a `Protocol`); `infrastructure` imports domain and constants; `presentation.cli` is the composition root. |
| 16 | SOLID holds | Pass | The use case depends on a protocol and receives the bot. `InternetSpeedTwitterBot` also takes screenshots and declines cookies; these are small private steps of one speed test, below the size where a split pays (the assignment fixes the class). Re-check in MIL-003, when posting is added: if the class grows the login and the post, the posting should move to its own class behind the same protocol. |
| 17 | Source is laid out in the clean architecture layers and folders, in `snake_case`, imports inward | Pass | `domain`, `application`, `infrastructure`, `presentation` under `src/speed_isp/`; `tests/unit`, `integration`, `e2e`. No layer is merged; [ADR-0001] covers criteria 10 and 17 as the user asked, and is not needed for the layout itself. |
| 18 | File and folder names are English, no space, allowed characters, language casing | Pass | All names checked, including `docker/Dockerfile` (well-known name) and `docs/images/step-*.png`. |

## MIL-002 Go / No-Go criteria

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The class and both methods exist with the assignment's names and Doxygen comments | Pass | `InternetSpeedTwitterBot` with `__init__` (driver, `down`, `up`), `get_internet_speed()` and the stub `tweet_at_provider()`, in `src/speed_isp/infrastructure/bot.py`, each with a Doxygen comment; `main` calls them in order through `run_bot`. |
| 2 | `python -m pytest` passes without browser or network | Pass | `.venv/Scripts/python -m pytest -q`: 29 passed, exit 0, run again after the round 1 fixes. |
| 3 | A live run in a Docker container prints a download and an upload speed | Pass | `out/live-run-mil-002.log`: "Download: 94.7 Mbps, upload: 50.54 Mbps". `docker/Dockerfile` installs Chromium and the driver and runs `python -m speed_isp` headless. I did not repeat the run; the evidence is the log. |
| 4 | A screenshot of the speed test result is stored for lecture steps 2 and 3 | Pass | `docs/images/step-2-speedtest-ready.png` (41 KB) and `docs/images/step-3-speedtest-result.png` (177 KB) exist. Their content was not inspected visually in this review. |
| 5 | Code reviewed against the Python programming checklist, `RC-*` is Go | Pass | This record. |

## Overall Verdict

Go. Every Mandatory criterion of QC-PY-001 passes after the round 1 fixes, and Go/No-Go rows 1-5 of [MIL-002] pass. Criterion 13 is an Optional Fail and not blocking. Limits of this review: the live run is judged by its log only, and the screenshots were checked for existence, not for content. Mode: autonomous, not independent (AI as stand-in for S01).

Changes made during the review: `Doxyfile` (removed the stray default `FILE_PATTERNS` lines, which caused 156 warnings) and `src/speed_isp/domain/speed.py` (the `@var` lines in the `SpeedResult` docstring replaced by prose, 2 warnings). Tests re-run: 29 passed. ruff and mypy were installed in `.venv` for the check and uninstalled again.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Optional: pin Selenium and pytest, and decide the licence confirmation carried over from [RC-008] | S01 | 2026-11-06 |
| Re-check criteria 7, 9 and 16 in MIL-003 (login with credentials, posting; keep passwords out of logs and consider moving posting into its own class) | S01 | 2026-11-05 |
| Optional: give the bot `__enter__`/`__exit__` so the browser is managed by a context manager | S01 | 2026-11-06 |

---

[MIL-002]: ../../milestones/mil-002-speed-test.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[ADR-0001]: ../../adr/adr-0001-no-design-artifacts-for-a-one-class-script.md
[RC-008]: rc-008-mil-001-code.md
[39813c3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/commit/39813c347ea5fb71ab746471b77a544bb4b7c600

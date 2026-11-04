# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [QC-PY-001], [ADR-0001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version; review of the MIL-001 code deliverable (AI as stand-in for S01) | [2b623e7] |

---

## Artifact Under Review

- Instance reviewed: MIL-001 code deliverable: `src/speed_isp/**`, `tests/**`, `pyproject.toml`, `.gitignore`, `Doxyfile`, `README.md`
- Checklist used: [QC-PY-001] (`QC-PY-001`); recorded deviation: [ADR-0001] (criteria 10 and 17)
- Scope: full review, round 1 (code defects fixed during the review, then re-checked)
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing | Pass | `speed_isp`, `constants.py`, `UPPER_SNAKE` constants, `snake_case` tests. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations | Pass | `PROMISED_DOWN`, `SPEEDTEST_TIMEOUT_SECONDS`; meaning and units in Doxygen comments. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | Round 1: `pyproject.toml` configured no formatter or linter, and the test file used an aliased import. Fixed: `[tool.ruff]` (88 columns, py313) added and the import changed. `ruff check` and `ruff format --check` pass on `src` and `tests`; no suppressions. (ruff and mypy were installed in `.venv` only for the check and removed again.) |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Round 1: `monkeypatch` was unannotated; now `pytest.MonkeyPatch`. `mypy --strict` passes. |
| 5 | No bare `except:`, no swallowed exceptions; `raise ... from` | Pass | No exception handling exists yet. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | None present. |
| 7 | Files, locks and connections are managed with context managers | N-A | No file, lock or connection is opened in this deliverable. Re-check in MIL-002 and MIL-003 (browser driver). |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Module docstrings in every package and test; each constant has a `##` Doxygen comment. `doxygen Doxyfile` exits 0. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` or logging yet. Credentials are read from the environment, none in source. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No class exists yet; the absence of a DCD is the deviation recorded in [ADR-0001]. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | Round 1: `test_credentials_are_not_hard_coded` reloaded the module with the passwords unset and left that state for later tests (order dependence). Fixed: state restored in `finally`. 4 tests pass, no network. Note: `test_service_is_x_or_y` depends on `SPEED_ISP_SERVICE` in the environment; validate the value when the bot uses it. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `[tool.mypy] strict = true` added; mypy reports no issues in 7 files. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Optional. `selenium>=4.20` is a lower bound, not a pin, and Selenium is not imported until MIL-002. Deferred, not blocking. |
| 14 | Each piece of knowledge is defined in one place | Pass | Speeds, URLs, timeouts and the post limit are defined once, in `constants.py`. |
| 15 | Imports point inward; no import cycles | Pass | Layer packages are empty; `constants.py` imports only `os`. |
| 16 | SOLID holds | Pass | No classes yet; one module with one reason to change. Re-check in MIL-002 and MIL-003. |
| 17 | Source is laid out in the clean architecture layers and folders, in `snake_case`, imports inward | Pass | `domain`, `application`, `infrastructure`, `presentation` under `src/speed_isp/`; `tests/unit`, `integration`, `e2e`. Round 1: the empty `tests/integration` and `tests/e2e` would vanish in git; `.gitkeep` files added. No layer is merged, so [ADR-0001] is not needed for this criterion. |
| 18 | File and folder names are English, no space, allowed characters, language casing | Pass | All names checked. |

## MIL-001 Go / No-Go criteria

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` has `requires-python = ">=3.13"`, one runtime dependency (Selenium), a pytest extra | Pass | All present. Note: `[project.scripts]` points to `speed_isp.__main__:main`, which MIL-002 and MIL-003 must create. |
| 2 | `.gitignore` ignores `.venv/`, `__pycache__/`, `.env` | Pass | Lines `.env`, `.venv/`, `__pycache__/` are present (also `.env.*`, `*.egg-info/`, `/docs/doxygen/`). Checked by reading the file; `git check-ignore` was not run because git was not used in this review. |
| 3 | `python -m pytest` runs in a fresh `.venv` | Pass | A new venv was created, `pip install -e ".[test]"` run, `python -m pytest`: 4 passed. Warning only: `license = { file = ... }` is deprecated in setuptools (removal after 2027-02-18). |
| 4 | README follows the template and explains `.venv`, `python -m pip install --upgrade pip`, run and tests | Pass | Template comment and sections present; Setup shows `.venv`, the pip upgrade, run and tests. `check-readme.sh` reports a finding only on the framework's own README. |
| 5 | Repository description and topics on the git host | Pass | Description and 8 topics set on the git host through its API, verified 2026-11-04. |
| 6 | No token or credential is in the working tree changes | Pass | Search of README, src, tests, pyproject, `.gitignore`, Doxyfile and docs for token patterns and assigned passwords found none. A `.env` exists in the working tree but is ignored and is not part of the deliverable. |

## Overall Verdict

Go. Row 5 verified (description and 8 topics set). Every Mandatory criterion of QC-PY-001 passes after the round 1 fixes, and Go/No-Go rows 1-4 and 6 pass; the open item is Go/No-Go row 5 (repository description and topics), Pending until S01 sets it. Criterion 13 is an Optional Fail and not blocking. Mode: autonomous, not independent (AI as stand-in for S01).

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Optional: pin Selenium and replace the deprecated `license = { file = ... }` with an SPDX string once the licence choice is confirmed | S01 | 2026-11-06 |
| Create `speed_isp/__main__.py` with `main` (referenced by `[project.scripts]`) and re-check criteria 7 and 16 for the bot | S01 | 2026-11-05 |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[ADR-0001]: ../../adr/adr-0001-no-design-artifacts-for-a-one-class-script.md
[2b623e7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/commit/2b623e74fbf13b90599da7d0c31a9ec38b19ef6e

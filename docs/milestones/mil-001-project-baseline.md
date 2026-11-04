# MIL-001 Project baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the repository is ready to receive code: configured, documented and publicly described.

## Deliverable

`pyproject.toml`, Python `.gitignore` (including `.env`), `src/` and `tests/` skeletons with `constants.py`, `Doxyfile`, README from the framework template with `.venv` instructions, and the repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` has `requires-python = ">=3.13"`, one runtime dependency (Selenium) and a pytest extra | Present | Missing |
| 2 | `.gitignore` ignores `.venv/`, `__pycache__/`, `.env` | `git check-ignore .env` succeeds | Fails |
| 3 | `python -m pytest` runs in a fresh `.venv` | Exit 0 | Non-zero |
| 4 | README follows the framework template and explains `.venv`, `python -m pip install --upgrade pip`, run and tests | All present | Any missing |
| 5 | Repository description and at least 5 topics are set on the git host | Visible via API | Missing |
| 6 | No token or credential is in the working tree changes | `git grep` finds none | Found |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | First gate |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4 (runnable, tested, one dependency) | [BC-001] |
| Success criteria 1, 2, 5, 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-04 — first day of the project.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add Python .gitignore | Add a Python `.gitignore` that also ignores `.env`, `.venv/` and Doxygen output, so no secret or build artefact is ever committed. | No | |
| 2 | Add pyproject.toml | Configure the project for Python 3.13 or newer with Selenium as the only runtime dependency and pytest as an optional `test` extra, with `src/` layout. | No | |
| 3 | Add src and tests skeleton with constants.py | Create `src/` and `tests/` and `constants.py` holding promised speeds, URLs and selectors; credentials are read from environment variables, never stored. | No | |
| 4 | Add Doxyfile | Add a `Doxyfile` configured for Python sources so the Doxygen comments in `src/` produce HTML documentation. | No | |
| 5 | Write README with .venv instructions | Write the README from the framework template: overview, requirements, how to create and use a local `.venv`, `python -m pip install --upgrade pip`, run and test commands. | No | |
| 6 | Set repository description and topics | Set the description and topics of the repository on the git host through its API using the token in `.env`, which is used personally and never imported into the project. | No | |

---

[BC-001]: ../business-case.md

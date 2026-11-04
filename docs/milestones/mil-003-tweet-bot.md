# MIL-003 Tweet bot (lecture steps 1 and 4)

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [MIL-002] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [2b623e7] |

---

## Purpose

Decide whether the bot can log in to X (or Y) and post a complaint that states measured and promised speeds.

## Deliverable

`tweet_at_provider()` implemented for the mock service Y and for X, a pure function that composes the message, credentials and promised speeds read through `constants.py`, unit tests, and a log and screenshot of a headless run in a Docker container.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The message names measured and promised speeds and is at most 280 characters | Unit test passes | Fails |
| 2 | Credentials come only from environment variables; none appear in the repository | `git grep` finds none | Found |
| 3 | `python -m pytest` passes without browser or network | Exit 0 | Non-zero |
| 4 | A run against Y posts the message, or the missing-credentials stop is recorded in the Project Plan's Open Issues | Evidence in log or plan | Neither |
| 5 | Code reviewed against the Python programming checklist, `RC-*` is Go | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | Needs the class and the measured speeds |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3 and success criterion 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-05 — follows MIL-002.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add account constants and environment loading | Add the promised speeds, the Y login URL and the names of the environment variables for the e-mail and password (lecture step 1) to `constants.py`; read values with `os.environ`, never from files. | No | |
| 2 | Compose the complaint message | Write a pure function that builds the text with measured and promised speeds and the optional provider mention, limited to 280 characters, and test it. | No | |
| 3 | Implement tweet_at_provider for Y and X | Log in with Selenium, open the composer, type the message and submit, with explicit waits and selectors from `constants.py`. Do not bypass CAPTCHAs. This is lecture step 4. | No | |
| 4 | Unit tests for the tweet flow with a fake driver | Test the login and posting steps and the missing-credentials error with a fake driver. | No | |
| 5 | Live tweet run against Y in a Docker container | Run headless in a Docker container with credentials from the environment, save the log and a screenshot; if no credentials exist, stop and record it in the Project Plan's Open Issues. | No | |

---

[BC-001]: ../business-case.md
[MIL-002]: mil-002-speed-test.md
[2b623e7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/commit/2b623e74fbf13b90599da7d0c31a9ec38b19ef6e

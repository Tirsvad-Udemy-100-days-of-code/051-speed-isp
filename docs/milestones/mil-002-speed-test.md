# MIL-002 Speed test (lecture steps 2 and 3)

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [MIL-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [2b623e7] |

---

## Purpose

Decide whether the bot can measure the live download and upload speed on speedtest.net and print it.

## Deliverable

The class `InternetSpeedTwitterBot` in `src/` with `__init__` (Selenium driver, `down`, `up`), `get_internet_speed()` and a `tweet_at_provider()` stub; a `main` entry point that calls them in order; unit tests with a fake driver; a headless live run in a Docker container with its log and screenshot.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The class and both methods exist with the assignment's names and Doxygen comments | Present | Missing |
| 2 | `python -m pytest` passes without browser or network | Exit 0 | Non-zero |
| 3 | A live run in a Docker container prints a download and an upload speed | Both numbers printed | No numbers |
| 4 | A screenshot of the speed test result is stored for lecture steps 2 and 3 | Files exist in `docs/images/` | Missing |
| 5 | Code reviewed against the Python programming checklist, `RC-*` is Go | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Needs `pyproject.toml`, `constants.py` and the test setup |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 and 2 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-05 — follows MIL-001.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create InternetSpeedTwitterBot class | Create the class with a Selenium driver, `down` and `up` properties in `__init__`, and the two methods `get_internet_speed()` and `tweet_at_provider()`, and call them in order from `main`. This is lecture step 2. | No | |
| 2 | Implement get_internet_speed | Open speedtest.net, start the test, wait up to the configured delay (60 to 180 s) for the result and read the download and upload values with XPath selectors kept in `constants.py`. This is lecture step 3. | No | |
| 3 | Unit tests for the bot with a fake driver | Test the class, the parsing of speed values and the waiting logic with a fake driver, so tests need no browser and no network. | No | |
| 4 | Live speed test in a Docker container | Run the bot with a headless browser in a Docker container (`framework/process/gui-testing.md`), save the log and a screenshot of the result to a shared folder. | No | |

---

[BC-001]: ../business-case.md
[MIL-001]: mil-001-project-baseline.md
[2b623e7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/commit/2b623e74fbf13b90599da7d0c31a9ec38b19ef6e

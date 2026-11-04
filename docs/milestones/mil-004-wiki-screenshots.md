# MIL-004 Wiki and screenshots

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [MIL-003] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [2b623e7] |

---

## Purpose

Decide whether the project is documented for S02 and S03: screenshots per lecture step and a wiki in three languages that explains what was learned.

## Deliverable

README with a screenshot for each of the four lecture steps; `docs/wiki/` with the same pages in English, Danish (`-da`) and Bahasa Malaysia (`-ms`), a sidebar and a language line on each page; Doxygen output builds.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Each of lecture steps 1 to 4 has a screenshot in the README | 4 images referenced and present, or a step listed as pending in the Open Issues | Missing |
| 2 | The wiki has the same page set in `en`, `da` and `ms` | File lists match | Page missing |
| 3 | Each wiki page explains what was gained in that step | Section "What we gained" present | Missing |
| 4 | Wiki reviewed against `QC-WIKI-001`, `RC-*` is Go | Go | No-Go |
| 5 | `doxygen Doxyfile` builds without errors | Exit 0 | Errors |
| 6 | `framework/scripts/check-readme.sh` passes | Exit 0 | Non-zero |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] | Needs the finished behaviour to document and photograph |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5; success criteria 3 and 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-06 — follows MIL-003.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Capture a screenshot for each lecture step | Collect a screenshot for steps 1 to 4 from the headless Docker runs and the practice service; a step that needs credentials the AI does not have is recorded in the Open Issues. | No | |
| 2 | Add screenshots to the README | Embed the step screenshots in the README under a section per lecture step. | No | |
| 3 | Write the English wiki | Write `Home`, one page per lecture step with its screenshot and a "What we gained" section, and `_Sidebar.md` as `framework/process/wiki.md` requires. | No | |
| 4 | Write the Danish wiki | Translate every English page to Danish (`-da`) with the same page set and a language line. | No | |
| 5 | Write the Bahasa Malaysia wiki | Translate every English page to Bahasa Malaysia (`-ms`) with the same page set and a language line. | No | |
| 6 | Build and check the Doxygen output | Run `doxygen Doxyfile` and fix warnings so the Doxygen comments in `src/` are complete. | No | |

---

[BC-001]: ../business-case.md
[MIL-003]: mil-003-tweet-bot.md
[2b623e7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/commit/2b623e74fbf13b90599da7d0c31a9ec38b19ef6e

# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [2b623e7] |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 | Review RC-002 round 1 fixes: traced every concern to a Business Case objective (criterion 6); spelled out FURPS+ (QC-LANG-001 criterion 10) | [2b623e7] |

---

## Purpose

Identify who is involved in the Day 51 speed-complaint bot, how much power and interest each has, and what each needs, so that scope, review and documentation serve them. Method: power/interest grid with a mapping of concerns to FURPS+ (Functionality, Usability, Reliability, Performance, Supportability, plus design, implementation, interface and physical constraints).

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Finish the assignment with good quality and learn from it |
| S02 | Udemy coursists | Fellow course participants | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code that uses the assignment's function names, with instructions to run it |
| S03 | GitHub viewers | Repository browsers looking for ideas | Public | LOW | LOW | Monitor | A clear description, topics and README, and no unnecessary runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, writes and accepts every artifact.
- **Keep Informed (S02):** cannot change the project but depends on its readability and runnability; served by README and wiki.
- **Monitor (S03):** occasional visitors; served by repository description, topics and README.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute | Business Case objective |
| --- | --- | --- | --- | --- |
| CN-001 | S01 | The bot measures speed and posts the complaint as the assignment describes | Functionality | [BC-001] objectives 1, 2, 3 |
| CN-002 | S01 | Work is traceable and reviewed step by step | Supportability | none directly; [BC-001] Methodological and Standards Foundation |
| CN-003 | S02 | Code is readable and uses the assignment's function names | Usability | [BC-001] objective 1 |
| CN-004 | S02 | The README explains how to set up the `.venv` and run the project and its tests | Usability | [BC-001] objective 4 |
| CN-005 | S03 | The repository has a clear description, topics and README | Usability | [BC-001] objective 5 and success criterion 6 |
| CN-006 | S03 | The project has no runtime dependencies beyond what is needed | Supportability | [BC-001] objective 4 and success criterion 2 |
| CN-007 | S01 | No credential or token is stored in the repository | Functionality (security) | [BC-001] objective 3 and success criterion 5 |

## Communication Requirements

| Channel | Frequency | Deliverable | Phase |
| --- | --- | --- | --- |
| Chat with S01 | At plan acceptance and at the end of the autonomous run | Plan; summary of pull requests, `RC-*` verdicts, stand-in decisions | All milestones |
| Pull request description | Per milestone | Closed issues, summary of changes | MIL-001 to MIL-004 |
| README and wiki | At release | Instructions, screenshots, lessons learned (en, da, ms) | MIL-004 |

## Conflicting Interests and Mitigations

| Conflict | Mitigation |
| --- | --- |
| S03 wants no runtime dependencies; the assignment requires Selenium (S01, S02) | Selenium is the only runtime dependency; everything else uses the standard library (no dotenv, no requests). Test and documentation tools are optional extras. |
| S01 wants a live tweet; X may demand a CAPTCHA | Use the mock service Y for the demonstration; X is supported but its bot detection is not bypassed. |

## Traceability Analysis

| Stakeholder | Actor / use case | Business Case objective |
| --- | --- | --- |
| S01 | Runs the bot; measures speed, posts the complaint | [BC-001] objectives 1, 2, 3 |
| S02 | Reads and runs the code | [BC-001] objectives 1, 4, 5 |
| S03 | Browses the repository | [BC-001] objectives 4, 5 |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | Accepted (RC-002) | 2026-11-04 |

---

[BC-001]: business-case.md
[2b623e7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/commit/2b623e74fbf13b90599da7d0c31a9ec38b19ef6e

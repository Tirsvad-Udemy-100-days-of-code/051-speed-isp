# ADR-0001 No design class diagram for a one-class script

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [MIL-002], [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [2b623e7] |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 | Review RC-007 round 1 fixes: gave the reason each option was rejected (criterion 2); spelled out abbreviations (criterion 10); added quality-attribute impact (criterion 6); listed MIL-002, MIL-003 and QC-PY-001 as affected artifacts (criterion 7); accepted (AI as stand-in for S01) | [2b623e7] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The code quality checklist for Python (QC-PY-001) expects classes to trace to a Design Class Diagram (DCD) (criterion 10) and the source to be laid out in the layers `domain`, `application`, `infrastructure` and `presentation` (criterion 17). This project ([BC-001]) is a single Day 51 assignment: one class (`InternetSpeedTwitterBot`) with two methods, one pure function that composes the message and a short entry point. Use cases, a domain model, a system sequence diagram, operation contracts and a DCD would be larger than the code they describe, and the only people who need to read the code are the course participants (S02) and repository visitors (S03), who gain more from short code than from diagrams.

Options:

1. Write the full design artifact chain. Rejected: the cost is several times the size of the code and adds nothing a reader cannot see in about 100 lines.
2. Write no design artifacts and record that deviation here, but keep the layer folders. Chosen.
3. Write no design artifacts and also skip the layer folders. Rejected: criterion 17 is then also broken, and the folder structure is cheap and is what S02 and S03 can learn from.

## Decision

Keep the four layer folders so that S02 and S03 see the structure, but write no use case, domain model, system sequence diagram, operation contract or DCD for this project. The classes and functions are traced to the tasks of milestones [MIL-002] and [MIL-003] and to the assignment's own names; this is the recorded deviation from QC-PY-001 criterion 10, and criterion 17 stays met.

## Consequences

**Positive:**

- The repository stays small and readable for S02 and S03.
- The layer rule (imports point inward) is still checked in the code review.

**Negative:**

- A reviewer cannot trace the classes to a DCD; the milestone tasks and the assignment text are the only trace.
- If the project grows beyond the assignment, this ADR must be superseded and the design artifacts written.

**Quality-attribute impact:** maintainability is kept by the layer folders and the small size; traceability (a part of maintainability) is reduced as described above. There is no effect on performance, security or portability.

## Affected Artifacts

- [BC-001] - scope stays as written; no design artifacts are in scope.
- [MIL-002] - its class and function tasks are the trace for the code.
- [MIL-003] - its tasks are the trace for the code.
- [QC-PY-001] - criterion 10 is deviated from by this decision.

---

[BC-001]: ../business-case.md
[MIL-002]: ../milestones/mil-002-speed-test.md
[MIL-003]: ../milestones/mil-003-tweet-bot.md
[QC-PY-001]: ../../framework/qc/code/qc-programming-python.md
[2b623e7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/commit/2b623e74fbf13b90599da7d0c31a9ec38b19ef6e

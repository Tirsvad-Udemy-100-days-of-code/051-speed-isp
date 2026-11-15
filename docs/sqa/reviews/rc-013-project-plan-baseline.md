# Review Record: PP-001 against QC-PP-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial review record; verdict Go (autonomous, not independent) | [5d274b7] |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / education
- Language reviewer: none (the stand-in reads English and knows the education domain)
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Planning Assumptions give the start date 2026-11-04, the plan window and the constraint; the baseline window 2026-11-16 to 2026-11-23 and the move of the end date are recorded with their source. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | The Gateway Schedule lists the five gateways once each with document, decision date and owner; every document exists, including MIL-005. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | The decision dates of MIL-001 to MIL-004 are those their milestones were accepted with; MIL-005 decides on 2026-11-23, its Target Date; the Planning Assumptions record the move of the end date. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage maps every In Scope item of BC-001 to a gateway; a row for the baseline item was added in this change (the earlier items were already mapped). |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Dependencies state the chain MIL-001 to MIL-005; it is acyclic and agrees with the order of the dates. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Dependencies state that a No-Go stops the later gateways and moves their dates by the length of the rework; the baseline adds a CI risk with the rule of three failed rounds. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Owner S01 is a stakeholder ID of SA-001. The project has no governance document, so there is no RACI to contradict; no invented role names are used. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Each planning assumption names its source (a Business Case section, the Stakeholder Analysis or a decision of S01); the move of the end date is recorded with its reason, the baseline of the framework. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan Risks give impact and mitigation for each of the four risks; the CI risk of MIL-005 traces to success criterion 7 of BC-001. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open Issues list the earlier points and add the domain of the unchanged documents and the live-site rule; no remaining statement contradicts another. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | The main deliverable of MIL-005 names the same items as its Deliverable section; the rows of the earlier gateways were not changed and match their milestone documents. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | The Stories column says `none` for every gateway; the Business Case has no use cases or user stories in scope (ADR-0001), so no gateway delivers one. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | The Gantt bar of the baseline uses the dates of the schedule table. The bars and dependency lines of the earlier gateways were not changed here (this is an optional criterion). |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | The earlier gateways link their milestone on the git host (330 to 333, not changed here); the milestone of MIL-005 is linked after the sync. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | PP-001 is the only Project Plan; its Version History records each change in its own row and only the latest row is Accepted. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The Metadata table has `Language | en` and `Domain | education`; neither is a placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code and `education` is a row of the domain list of docs/artifact-registry.md. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | The prose and the table cells are English; only file names, commands and IDs are code. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The registry gives the register `IT Executive English` for this type; the text is written for that reader. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No dictionary (DICT) exists in this project and none is added. The added text uses the terms bot, speed test, complaint, provider, promised speed, lecture step, milestone and baseline in one meaning each, found by reading. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, section headings, IDs and statuses are the framework's English ones. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No file `<name>.<language>.md` exists beside the document. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | The `Domain` row changed from `it` to `education` in this version (the language `en` is unchanged). The Version History row records the change and this review covers it. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The stand-in reads English and knows the education domain and checked the terms; the check is autonomous and not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations added by this change are spelled out where they are first used (SQA, QC, CI, PO) or are established names (README). |

## Overall Verdict

Go — every Mandatory criterion of QC-PP-001 and QC-LANG-001 passes; the domain of the unchanged documents and the live-site rule are recorded as Open Issues. Review of the whole document after the edits of this change.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| No open action | S01 | 2026-11-23 |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[5d274b7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/commit/5d274b7c566f9670b6f792c7832440ea30e0d076

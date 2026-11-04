# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-004], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version; review of the MIL-004 wiki (AI as stand-in for S01) | [15f11de] |

---

## Artifact Under Review

- Instance reviewed: the wiki `docs/wiki/` (18 pages in `en`, `da`, `ms` plus `_Sidebar.md`) delivered by [MIL-004]
- Checklist used: [QC-WIKI-001] (`QC-WIKI-001`); MIL-004 Go/No-Go rows 1, 2, 3, 5 and 6 are checked below as well
- Scope: full review, round 1 (three mechanical defects fixed during the review)
- Language and domain: en, da, ms / it (a wiki is documentation, not an artifact type written in the PO language; `QC-LANG-001` is not applied)
- Language reviewer: none named; the reviewer is a stand-in and not a native reader of Danish or Bahasa Malaysia (see Action Items)
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | `**051-speed-isp**`, then `Home`, Step 1 to 4, `Run and test`; one list only. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | 6 English pages, 6 list entries. Every relative link in all 19 files (sidebar, language lines, Home tables) was resolved mechanically to an existing `.md`; 0 missing. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis | Pass | The wiki has no related wiki and the sidebar has no such section. |
| 5 | A `**Languages**` section is the last section, one line per language in that language, linking to that language's `Home` page | Pass | `English: [Home](Home)`, `Dansk: [Hjem](Home-da)`, `Bahasa Melayu: [Utama](Home-ms)`; last section; all three targets exist. |
| 6 | The sidebar does not repeat the page list per language | Pass | One list. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator | N-A | The sidebar is hand-written; no generator exists for this project. |
| 8 | The wiki has a `Languages` line on each page (criterion 11) | Pass | See criterion 11. |
| 9 | Every wiki exists in English and, as a minimum, in the PO language; further languages on top, never instead of English | Pass | English is the base; `da` and `ms` are additional, so the minimum holds whichever language the registry names as PO language. |
| 10 | Every English page has a page in each other language: the page sets are identical | Pass | 6 pages x 3 languages = 18 files; the name sets match (`Home`, `Step-1-Account-and-Constants`, `Step-2-Create-a-Class`, `Step-3-Get-Internet-Speeds`, `Step-4-Tweet-at-Provider`, `Run-and-Test`, each with `-da` and `-ms`). Heading counts per page match across the three languages. |
| 11 | Every page starts with the language line, current language bold, a link to the same page in each other language | Pass | Line 1 of all 18 pages checked: current language bold, the other two linked to the same page with the right suffix; all targets exist. |
| 12 | A non-English page is named `<Page>-<code>.md` with a BCP 47 code; English has no suffix | Pass | `-da`, `-ms` suffixes; English has none. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Mechanical diff of every fenced block, every inline code span and every http URL, each of the 6 English pages against its `-da` and `-ms` page: identical (36 of 36 comparisons). The console output in `text` fences stays in English. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change | Pass | Checked on the published wiki 2026-11-04 after PR 25 merged: the host lists 19 pages (18 pages plus the sidebar), every page URL returns 200, the three image URLs return 200, the language links are shown on Home. |
| 15 | A change to the layout rules is made in the generator or template and in the checklist's source rules together | N-A | No layout rule was changed. |

## Other MIL-004 Go/No-Go rows

| Row | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Each of lecture steps 1 to 4 has a screenshot in the README | Pass | README section "Lecture steps in pictures" embeds steps 1 to 3 (`docs/images/step-1-y-login.png`, `step-2-speedtest-ready.png`, `step-3-speedtest-result.png`, all present); step 4 is a table row that says it is not yet taken and why. `docs/project-plan.md` Open Issues lists the step 4 screenshot (`docs/images/step-4-tweet-posted.png`) as open until S01 runs the bot with a Y account. The Go column allows "a step listed as pending in the Open Issues", so this passes. |
| 2 | Same page set in `en`, `da`, `ms` | Pass | Criterion 10. |
| 3 | Each wiki page explains what was gained in that step | Pass | `## What we gained` / `## Hvad vi fik ud af det` / `## Apa yang kami peroleh` is present once on each of the 5 step and run pages in each language (15 of 15). `Home` is an index, not a step; it states in its intro that each step page ends with the section. |
| 5 | `doxygen Doxyfile` builds without errors | Pass | Run in the review: exit 0, no warning or error line. |
| 6 | `framework/scripts/check-readme.sh` passes (exit 0) | Pass with a stated qualification | The script exits 1 with one finding: `framework README: checklist qc-project-plan.md is not named`. It concerns the framework's own README under `framework/`, which this project must not edit (AGENTS.md rule 5), and reports nothing about the project's README. The project README passes; the literal "Exit 0" is not met, so the deviation is recorded and needs the decision in the Action Items. |

Image paths: every image URL in the wiki (3 distinct, 9 uses) ends in a file that exists under `docs/images/`. The step 4 page has no image and says so in its "Screenshot of the posted tweet" section, in all three languages.

## Language review (stand-in, not a native reader)

Checked mechanically: page sets, language lines, headings (count and order), code, inline code, URLs, link targets, image targets. Checked by reading: the Danish and Bahasa Malaysia text reads as correct and natural as far as the stand-in can judge; technical terms are kept or glossed consistently (for example `pemacu (driver)`, `headless (tanpa paparan)`).

Doubtful phrases for a native reader:

- da `Home-da`: heading "Hvem er den til"; natural alternative "Hvem er det til".
- da `Step-4-da`: "rejser `ValueError`" (to raise an exception); "kaster" is the more common developer term.
- da: "Selectors" and "headless" are kept as English loanwords; a native reader may prefer "vælgere".
- da `Step-2-da`: "holder på browseren"; a native reader may prefer "rummer".
- ms `Step-2-ms`: "`__init__`nya" (suffix on a code span) reads awkwardly; "`__init__` kelas itu" is smoother.
- ms: "kelayakan log masuk" (credentials), "sepanduk kuki" (cookie banner), "laman" (site), "larian" (run) are standard, but a native reader should confirm the register.
- The language line says "Bahasa Malaysia", the sidebar says "Bahasa Melayu"; both follow the framework's own examples (`framework/process/wiki.md`, `QC-WIKI-001`), so they are left as is; the owner may prefer one name.

## Defects fixed during the review

1. `Step-1-Account-and-Constants-ms.md` line 7: image alt text was English; now `Halaman log masuk perkhidmatan latihan Y`.
2. `Step-2-Create-a-Class-ms.md` line 7: image alt text was English; now `Bot telah membuka speedtest.net dan sedia memulakan ujian`.
3. `Step-3-Get-Internet-Speeds-ms.md` line 7: image alt text was English; now `Ujian kelajuan yang selesai di speedtest.net`.

Only the alt text in square brackets changed; URLs were not touched.

## Overall Verdict

Go. Every Mandatory criterion of [QC-WIKI-001] passes, criterion 14 after the check of the published wiki on 2026-11-04. Mode: autonomous, not independent (AI as stand-in for S01); native-reader action items on the Danish and Malay phrasing remain optional.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Decide whether MIL-004 row 6 counts as met, given that the exit 1 of `check-readme.sh` comes from the framework's own README (no finding on the project README); propose the fix upstream (AGENTS.md rule 5) | S01 | 2026-11-06 |
| Have a reader of Danish and of Bahasa Malaysia confirm or correct the doubtful phrases listed above (optional, non-blocking) | S01 | 2026-11-06 |
| After S01 runs the bot with a Y account, add `docs/images/step-4-tweet-posted.png` to the README and to the step 4 wiki pages in all three languages (carried over from [RC-010]) | S01 | 2026-11-06 |

---

[MIL-004]: ../../milestones/mil-004-wiki-screenshots.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[RC-010]: rc-010-mil-003-code.md
[15f11de]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/commit/15f11de299844b5966aa05cfebdd4f079b60f414

# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001], [MIL-005] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [2b623e7] |
| 2026-11-04 | Deprecated | Jens Tirsvad Nielsen | S01 | Review RC-001 round 1 fixes: justified the qualitative benefits (criterion 1); lowered implementation detail to executive register (QC-LANG-001 criterion 4); spelled out abbreviations (QC-LANG-001 criterion 10) | [2b623e7] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added objective 6, success criterion 7, a scope item, an out-of-scope item, two risks and a constraint for the baseline milestone MIL-005; set the domain to education; reviewed in autonomous mode, not independent | [5d274b7] |

---

## Executive Summary

Internet providers (ISPs) often deliver less speed than the contract promises, and most customers never measure it. This project is a Python bot, built as the Day 51 assignment of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*, that measures the real download and upload speed on speedtest.net with Selenium and posts a public complaint on X (or on the practice service "Y") that states the measured and the promised speeds. The deliverable is a small, readable, runnable repository that other course participants can learn from.

## Methodological and Standards Foundation

The work follows the software quality assurance (SQA) and quality control (QC) framework mounted at `framework/` (documents reviewed against QC checklists, plan-first gate, one pull request per milestone). Product quality is described with ISO/IEC 25010:2023 characteristics. Code follows the `coding-conventions` skill (Python) and the layering of the `clean-architecture` skill, scaled to a small script.

## Problem Statement

- Customers do not know what speed they get compared with what they pay for.
- Manual speed tests and manual complaints are repetitive and are easily skipped.
- A public complaint gets a faster answer than a private support ticket, but writing it by hand each time is tedious.

## Business Opportunity

Automating the measure-and-complain loop turns a one-off frustration into evidence and a repeatable action. For the course participant it is also the practical lesson of Selenium automation and of structuring a multi-step bot as a class.

## Objectives

1. Provide the class `InternetSpeedTwitterBot` with `get_internet_speed()` and `tweet_at_provider()`, as the assignment names them.
2. Measure live download and upload speed on speedtest.net with Selenium and print the result.
3. Log in to X (or Y) with Selenium and post a message that contains the measured and the promised speeds.
4. Keep the repository runnable from its README, covered by automated tests, and with no runtime dependency except Selenium.
5. Document every lecture step with a screenshot in the README and in a three-language wiki (English, Danish, Bahasa Malaysia) that explains what was learned.
6. Bring the finished project to the common baseline of the framework: the adopted framework release, a README that lists only the documents of the repository and names the terms-of-use caveat, licence and project URL metadata, the editor settings of the baseline and an `.env.example` that also names the settings of the program ([MIL-005]).

## Scope

### In Scope

- Central configuration of the promised speeds, addresses and page selectors; credentials are read from the environment.
- The bot class, speed measurement, login and tweet on Y (mock) and X.
- Project configuration, source documentation and a README built from the framework template.
- Automated unit tests that need no browser and no network.
- Wiki pages in en, da and ms, with a screenshot per lecture step.
- Repository description and topics on the git host.
- The baseline milestone [MIL-005]: the framework release, the README without the private framework files in its appendix, project URL metadata, `.editorconfig`, `.env.example`, review records and the Project Plan update. It changes no behaviour of the program.

### Out of Scope

- Scheduling the bot to run repeatedly.
- Solving CAPTCHAs or bypassing X's bot detection.
- Storing or committing any credential or token.
- A graphical user interface.
- Any change to `src/`, `tests/`, `docker/Dockerfile` or the wiki pages in the baseline milestone [MIL-005]. That milestone starts no browser, opens no web page, runs no speed test, signs in to no site, posts nothing and runs no container; the tests use fakes.

## Expected Benefits

### Tangible Benefits

- A completed, reviewed Day 51 assignment in a public repository.
- A reusable, tested pattern for a Selenium bot.

### Intangible Benefits

- Practice with classes, Selenium waits and XPath.
- A clear example other participants can compare their solutions with.

## Strategic Alignment

The project supports the course participant's goal of finishing the 100 Days of Code bootcamp with a portfolio of documented, quality-assured projects (S01), and the sharing of readable solutions with other participants (S02, S03).

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Unit tests pass | 100 % of tests green on Python 3.13 | Test run exits with success |
| 2 | Runtime dependencies | Exactly one (Selenium) | Dependency list in the project configuration |
| 3 | Lecture steps documented | 4 of 4 steps with a screenshot in README and in each wiki language | Review of README and wiki |
| 4 | Wiki languages | 3 languages, same page set | `docs/wiki/` file list |
| 5 | Secrets in repository | 0 | `git grep` for tokens; `.env` ignored |
| 6 | Repository metadata | Description and at least 5 topics set | Git host repository page |
| 7 | The baseline milestone is done (objective 6) | `framework/scripts/check-readme.sh`, `check-languages.sh` and `check-editorconfig.sh` exit with code 0, `python -m pytest` passes, 100 % of the continuous integration (CI) checks of the pull request of [MIL-005] pass | The script exit codes and the pull request status on the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| speedtest.net or X changes its page, so selectors break | Bot stops working | Keep selectors in one central configuration; document the date the selectors were verified |
| X shows a CAPTCHA or e-mail confirmation on repeated logins | Live tweet cannot be automated | Use the mock service Y for the demonstration; do not bypass bot detection |
| Credentials leak into the repository | Account compromise | Read from environment variables only; `.env` in `.gitignore`; no value in tests, docs or logs |
| No Y or X credentials are available for the live run | Screenshots of the login and tweet steps cannot be taken by the AI | Open issue: S01 supplies credentials in the environment, or takes those screenshots |
| A live browser test disturbs the user's desktop | Interrupted work | Run the browser headless in a Docker container (`framework/process/gui-testing.md`) |
| Automating a third-party service (speedtest.net, X) can break its terms of use | The reader's account may be blocked or limited | The README and the wiki say so in a neutral note; the practice service Y is the supported target; the reader reads the terms before running the bot |
| The documents of the baseline milestone [MIL-005] change documents that were accepted earlier, and an AI stand-in for S01 reviews them | A defect is missed because the review is not independent | Every review record of the baseline says `Mode: autonomous, not independent`, `src/` and `tests/` are not changed, the tests run before and after, and the end-of-run summary lists the reviews for challenge |

## Assumptions

- S01 is the Product Owner, developer and reviewer; the AI acts as stand-in reviewer in autonomous mode.
- Python 3.13 or newer is installed ("greater than 3.13" is read as 3.13 or newer).
- The practice service Y at `https://app.100daysofpython.dev/` stays available.
- Docker is available for headless browser runs.

## Constraints

- Python 3.13 or newer, an isolated local environment, and automated tests.
- Separate source, test and documentation folders; source documented with Doxygen comments.
- Avoid runtime dependencies unless needed.
- The wiki exists in English, Danish and Bahasa Malaysia.
- Tokens come from a private local environment file for personal use only; the project code and tests never read or import it.
- The Product Owner (PO) language is English and the PO domain is education (it was IT until [MIL-005]; the documents that [MIL-005] does not change keep the domain `it`, see the Open Issues of [PP-001]).
- The baseline milestone [MIL-005] starts 2026-11-16 and is finished within one week, by 2026-11-23. For that milestone only, an AI stand-in for S01 reviews and accepts the changed documents.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About two days of S01's time, plus AI effort for scaffolding, tests and translation | A finished, shareable assignment and documented learning; no licence or hosting cost |

The benefits are qualitative on purpose: this is a non-commercial learning project with no revenue, so a return on investment (ROI) in money would be invented. The cost is bounded (two days, no cash outlay), and the benefits are checked through the Success Criteria above rather than priced.

## Stakeholders

| Stakeholder ID (from the Stakeholder Analysis) | Interest in this project |
| --- | --- |
| S01 | Finish the assignment with quality; owns, develops and reviews |
| S02 | Readable, runnable code with the assignment's function names and README instructions |
| S03 | Clear repository description, topics and README; no unnecessary runtime dependencies |

## Recommendation

Proceed — the scope is small, the risks have mitigations and the result is directly useful to all three stakeholders.

---

[SA-001]: stakeholder-analysis.md
[2b623e7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/commit/2b623e74fbf13b90599da7d0c31a9ec38b19ef6e
[PP-001]: ./project-plan.md
[MIL-005]: ./milestones/mil-005-framework-baseline.md
[5d274b7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/commit/5d274b7c566f9670b6f792c7832440ea30e0d076

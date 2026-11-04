# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [2b623e7] |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 | Review RC-001 round 1 fixes: justified the qualitative benefits (criterion 1); lowered implementation detail to executive register (QC-LANG-001 criterion 4); spelled out abbreviations (QC-LANG-001 criterion 10) | [2b623e7] |

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

## Scope

### In Scope

- Central configuration of the promised speeds, addresses and page selectors; credentials are read from the environment.
- The bot class, speed measurement, login and tweet on Y (mock) and X.
- Project configuration, source documentation and a README built from the framework template.
- Automated unit tests that need no browser and no network.
- Wiki pages in en, da and ms, with a screenshot per lecture step.
- Repository description and topics on the git host.

### Out of Scope

- Scheduling the bot to run repeatedly.
- Solving CAPTCHAs or bypassing X's bot detection.
- Storing or committing any credential or token.
- A graphical user interface.

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

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| speedtest.net or X changes its page, so selectors break | Bot stops working | Keep selectors in one central configuration; document the date the selectors were verified |
| X shows a CAPTCHA or e-mail confirmation on repeated logins | Live tweet cannot be automated | Use the mock service Y for the demonstration; do not bypass bot detection |
| Credentials leak into the repository | Account compromise | Read from environment variables only; `.env` in `.gitignore`; no value in tests, docs or logs |
| No Y or X credentials are available for the live run | Screenshots of the login and tweet steps cannot be taken by the AI | Open issue: S01 supplies credentials in the environment, or takes those screenshots |
| A live browser test disturbs the user's desktop | Interrupted work | Run the browser headless in a Docker container (`framework/process/gui-testing.md`) |

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

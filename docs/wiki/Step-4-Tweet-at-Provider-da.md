🌐 [English](Step-4-Tweet-at-Provider) · **Dansk** · [Bahasa Malaysia](Step-4-Tweet-at-Provider-ms)

# Trin 4: Skriv til udbyderen

`tweet_at_provider()` sammenligner den målte hastighed med den lovede, og når den er for lav, logger den ind på Y (eller X) og skriver en klage.

Beskeden bygges af en ren funktion, `compose_complaint()`, for eksempel:

```text
Hey @YourProvider, why is my internet speed 97.3down/49.7up when I pay for 150down/10up?
```

## Hvad vi gjorde

- Skrev `compose_complaint()` i `domain`-laget. Den forkorter aldrig teksten i det stille og rejser `ValueError`, når opslaget ville blive længere end 280 tegn.
- Skrev én klasse pr. tjeneste, `YSite` og `XSite`, bag en lille `SocialSite`-grænseflade: `login()` og `post(text)`. Selectors er konstanter.
- Kontrollerede loginoplysningerne, før browseren åbnes. En manglende `Y_EMAIL` eller `Y_PASSWORD` stopper botten med en tydelig besked og afslutningskode 1:

```text
set the environment variables Y_EMAIL and Y_PASSWORD
```

- Forsøgte ikke at omgå en CAPTCHA eller en e-mailbekræftelse på X; hvis login ikke gennemføres, stopper botten.

## Skærmbillede af det udsendte opslag

Skærmbilledet af den udsendte besked, `docs/images/step-4-tweet-posted.png`, skrives, når du kører botten med din egen Y-konto og har sat `SPEED_ISP_SCREENSHOT_DIR`. Det er endnu ikke en del af repositoriet: repositoriets forfatter skal stadig tage det med sine egne loginoplysninger.

## Hvad vi fik ud af det

- **Regler adskilt fra browseren.** Teksten testes uden Selenium.
- **Åben for udvidelser.** En ny tjeneste er en ny klasse bag samme grænseflade; intet andet ændres.
- **Omhu med hemmeligheder.** Loginoplysninger kommer fra miljøet og optræder aldrig i logs eller fejlmeddelelser.
- **Ærlige grænser.** X kan kræve en CAPTCHA; botten melder det og stopper, og mock-tjenesten Y bruges til demonstrationen.

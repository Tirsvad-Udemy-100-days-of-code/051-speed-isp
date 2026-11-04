🌐 [English](Step-2-Create-a-Class) · **Dansk** · [Bahasa Malaysia](Step-2-Create-a-Class-ms)

# Trin 2: Opret en klasse

En bot med flere trin er lettere at holde ryddelig som en klasse. `InternetSpeedTwitterBot` holder på browseren og de målte hastigheder.

![Botten har åbnet speedtest.net og er klar til at starte testen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/raw/branch/main/docs/images/step-2-speedtest-ready.png)

## Hvad vi gjorde

- Oprettede `InternetSpeedTwitterBot` i `src/speed_isp/infrastructure/bot.py`. Dens `__init__` opretter Selenium-driveren og de to egenskaber `down` og `up`.
- Tilføjede opgavens to metoder, `get_internet_speed()` og `tweet_at_provider()`.
- Uden for klassen opretter indgangspunktet objektet og kalder de to metoder i rækkefølge:

```python
bot = InternetSpeedTwitterBot()
speed = bot.get_internet_speed()
bot.tweet_at_provider()
```

## Hvad vi fik ud af det

- **En bot med tilstand.** Driveren og hastighederne følges ad, så den anden metode kan bruge det, den første målte.
- **Læselige trin.** Koden læses som forelæsningen: først hent hastigheden, derefter skriv opslaget.
- **Testbar kode.** Driveren gives udefra, så enhedstest bruger en falsk driver og hverken har brug for browser eller netværk.
- **Lag.** Regler (`domain`), rækkefølgen af trin (`application`), Selenium (`infrastructure`) og kommandolinjen (`presentation`) ligger i hver sin mappe; imports peger indad.

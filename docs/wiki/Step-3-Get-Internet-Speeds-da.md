🌐 [English](Step-3-Get-Internet-Speeds) · **Dansk** · [Bahasa Malaysia](Step-3-Get-Internet-Speeds-ms)

# Trin 3: Hent internethastigheder

`get_internet_speed()` åbner speedtest.net, starter testen, venter på resultatet og aflæser download- og uploadhastigheden.

![Den færdige hastighedstest på speedtest.net](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/raw/branch/main/docs/images/step-3-speedtest-result.png)

Konsoloutput fra en kørsel i en Docker-container:

```text
Speed test started; waiting up to 180 s
Download: 97.32 Mbps, upload: 49.72 Mbps
```

## Hvad vi gjorde

- Afviste cookiebanneret (det mest privatlivsvenlige valg) og klikkede på knappen **GO**, som blev fundet med XPath.
- Ventede med `WebDriverWait`, til siden viser `Result ID`, i stedet for en fast `sleep`. Ventetiden er højst 180 sekunder, angivet i `constants.py`.
- Aflæste tallene med XPath og konverterede dem med `parse_mbps()`.
- Kørte browseren headless i en Docker-container (`docker/Dockerfile`), så testen aldrig overtager dit skrivebord.

## Hvad vi fik ud af det

- **Eksplicitte ventetider.** At vente på en betingelse er hurtigere og sikrere end at gætte på en forsinkelse.
- **XPath-øvelse.** Sider med genererede klassenavne udpeges i stedet via tekst og attributter.
- **Selectors ét sted.** Når speedtest.net ændrer sig, er det kun `constants.py`, der ændres.
- **Headless-kørsler.** En container giver gentagelige kørsler og skærmbilleder uden en synlig browser.

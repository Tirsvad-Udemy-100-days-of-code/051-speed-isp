🌐 [English](Step-1-Account-and-Constants) · **Dansk** · [Bahasa Malaysia](Step-1-Account-and-Constants-ms)

# Trin 1: Konto og konstanter

Botten har brug for to ting, før den kan klage: en konto på X (eller på øvelsestjenesten Y) og den hastighed, din udbyder lover.

![Loginsiden på øvelsestjenesten Y](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/raw/branch/main/docs/images/step-1-y-login.png)

## Hvad vi gjorde

- Brugte øvelsestjenesten Y (`https://app.100daysofpython.dev/`), så ingen rigtig konto på sociale medier er i fare. X understøttes også.
- Lagde de lovede hastigheder og URL'erne i `src/speed_isp/constants.py`:

```python
PROMISED_DOWN: int = 150
PROMISED_UP: int = 10
Y_LOGIN_URL: str = "https://app.100daysofpython.dev/services/y/login"
```

- Læste loginoplysningerne fra miljøvariabler, aldrig fra koden:

```bash
export Y_EMAIL="you@example.com"
export Y_PASSWORD="your-password"
```

## Hvad vi fik ud af det

- **Ét sted til indstillinger.** Konstanter ligger i `constants.py`, så en ændret selector eller hastighed rettes ét sted.
- **Hemmeligheder holdes ude af repositoriet.** Adgangskoder kommer fra miljøet, og `.env` står i `.gitignore`.
- **En sikker legeplads.** En mock-tjeneste lader dig øve login og opslag uden at røre en personlig konto.

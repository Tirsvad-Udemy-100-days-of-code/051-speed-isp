🌐 **English** · [Dansk](Step-1-Account-and-Constants-da) · [Bahasa Malaysia](Step-1-Account-and-Constants-ms)

# Step 1: Account and constants

The bot needs two things before it can complain: an account on X (or on the practice service Y) and the speed your provider promises.

![The login page of the practice service Y](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/raw/branch/main/docs/images/step-1-y-login.png)

## What we did

- Used the practice service Y (`https://app.100daysofpython.dev/`), so no real social media account is at risk. X is supported too.
- Put the promised speeds and the URLs in `src/speed_isp/constants.py`:

```python
PROMISED_DOWN: int = 150
PROMISED_UP: int = 10
Y_LOGIN_URL: str = "https://app.100daysofpython.dev/services/y/login"
```

- Read the credentials from environment variables, never from the code:

```bash
export Y_EMAIL="you@example.com"
read -rs -p "Y password: " Y_PASSWORD && export Y_PASSWORD
```

## What we gained

- **One place for settings.** Constants live in `constants.py`, so a changed selector or speed is edited once.
- **Secrets stay out of the repository.** Passwords come from the environment, and `.env` is in `.gitignore`.
- **A safe playground.** A mock service lets you practise logging in and posting without touching a personal account.

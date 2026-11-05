🌐 **English** · [Dansk](Step-4-Tweet-at-Provider-da) · [Bahasa Malaysia](Step-4-Tweet-at-Provider-ms)

# Step 4: Tweet at the provider

`tweet_at_provider()` compares the measured speed with the promised speed and, when it is too low, logs in to Y (or X) and posts a complaint.

The message is built by a pure function, `compose_complaint()`, for example:

```text
Hey @YourProvider, why is my internet speed 97.3down/49.7up when I pay for 150down/10up?
```

## What we did

- Wrote `compose_complaint()` in the `domain` layer. It never silently shortens the text and raises `ValueError` when the post would be longer than 280 characters.
- Wrote one class per site, `YSite` and `XSite`, behind a small `SocialSite` interface: `login()` and `post(text)`. Selectors are constants.
- Checked the credentials before opening the browser. A missing `Y_EMAIL` or `Y_PASSWORD` stops the bot with a clear message and exit code 1:

```text
set the environment variables Y_EMAIL and Y_PASSWORD
```

- Did not try to get around a CAPTCHA or an e-mail confirmation on X; if the login does not complete, the bot stops.

## Screenshot of the posted tweet

![The complaint as the top post on Y](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/raw/branch/main/docs/images/step-4-tweet-posted.png)

The screenshot, `docs/images/step-4-tweet-posted.png`, comes from a live run in a Docker container with the author's own Y account (the bot writes it when `SPEED_ISP_SCREENSHOT_DIR` is set). The post reads: "Hey, why is my internet speed 93.5down/52.4up when I pay for 150down/10up?"

## What we gained

- **Separate rules from the browser.** The text is tested without Selenium.
- **Open for extension.** A new site is a new class behind the same interface; nothing else changes.
- **Careful with secrets.** Credentials come from the environment and never appear in logs or error messages.
- **Honest limits.** X may ask for a CAPTCHA; the bot reports it and stops, and the mock service Y is used for the demonstration.

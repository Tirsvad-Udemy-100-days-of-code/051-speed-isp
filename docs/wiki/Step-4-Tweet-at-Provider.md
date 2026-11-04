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

The screenshot of the posted message, `docs/images/step-4-tweet-posted.png`, is written when you run the bot with your own Y account and `SPEED_ISP_SCREENSHOT_DIR` set. It is not part of the repository yet: the author of the repository still has to take it with their own credentials.

## What we gained

- **Separate rules from the browser.** The text is tested without Selenium.
- **Open for extension.** A new site is a new class behind the same interface; nothing else changes.
- **Careful with secrets.** Credentials come from the environment and never appear in logs or error messages.
- **Honest limits.** X may ask for a CAPTCHA; the bot reports it and stops, and the mock service Y is used for the demonstration.

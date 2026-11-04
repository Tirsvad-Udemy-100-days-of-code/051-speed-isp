"""!
@file constants.py
@brief All constants of the project: promised speeds, URLs, limits and
       the credentials read from environment variables.

Credentials are never written in the source. They are read from the
environment when the module is imported; an unset variable gives an empty
string and the bot refuses to log in with it.
"""

import os

## Environment variable names of the credentials; shown in error messages, never the values.
Y_EMAIL_ENV: str = "Y_EMAIL"
Y_PASSWORD_ENV: str = "Y_PASSWORD"
TWITTER_EMAIL_ENV: str = "TWITTER_EMAIL"
TWITTER_PASSWORD_ENV: str = "TWITTER_PASSWORD"

## Promised (contract) download speed in Mbps. Change it to your own contract.
PROMISED_DOWN: int = 150
## Promised (contract) upload speed in Mbps.
PROMISED_UP: int = 10

## Service the bot posts to: "Y" (practice service) or "X".
SERVICE: str = os.environ.get("SPEED_ISP_SERVICE", "Y").upper()

## Mock service Y login page.
Y_LOGIN_URL: str = "https://app.100daysofpython.dev/services/y/login"
## Y account e-mail, from the environment.
Y_EMAIL: str = os.environ.get(Y_EMAIL_ENV, "")
## Y account password, from the environment.
Y_PASSWORD: str = os.environ.get(Y_PASSWORD_ENV, "")

## X login page.
TWITTER_LOGIN_URL: str = "https://x.com/i/flow/login"
## X account e-mail, from the environment.
TWITTER_EMAIL: str = os.environ.get(TWITTER_EMAIL_ENV, "")
## X account password, from the environment.
TWITTER_PASSWORD: str = os.environ.get(TWITTER_PASSWORD_ENV, "")
## Optional provider handle to mention, for example "@Comcast"; empty for none.
PROVIDER_HANDLE: str = os.environ.get("SPEED_ISP_PROVIDER", "")

## Speed test page.
SPEEDTEST_URL: str = "https://www.speedtest.net/"
## Seconds to wait for the speed test to finish (60 to 180 depending on the line).
SPEEDTEST_TIMEOUT_SECONDS: int = 180
## Seconds to wait for an element on the social service.
ELEMENT_TIMEOUT_SECONDS: int = 20

## XPath of the "reject all" button of the speedtest.net cookie banner.
SPEEDTEST_REJECT_COOKIES_XPATH: str = "//*[@id='onetrust-reject-all-handler']"
## XPath of the button that starts the speed test.
SPEEDTEST_GO_XPATH: str = "//button[starts-with(@aria-label, 'start speed test')]"
## XPath of an element that only exists when the test has finished.
SPEEDTEST_DONE_XPATH: str = "//*[normalize-space(text())='Result ID']"
## XPath of the measured download speed.
SPEEDTEST_DOWN_XPATH: str = (
    "//p[starts-with(normalize-space(.), 'Download')]/following-sibling::h3"
)
## XPath of the measured upload speed.
SPEEDTEST_UP_XPATH: str = (
    "//p[starts-with(normalize-space(.), 'Upload')]/following-sibling::h3"
)
## Seconds to wait for the cookie banner before assuming there is none.
COOKIE_BANNER_TIMEOUT_SECONDS: int = 5

## True to run Chrome headless (set SPEED_ISP_HEADLESS to 1 or true).
HEADLESS: bool = os.environ.get("SPEED_ISP_HEADLESS", "").lower() in {"1", "true"}
## Path of the Chrome binary; empty to let Selenium find it.
CHROME_BIN: str = os.environ.get("CHROME_BIN", "")
## Path of the chromedriver binary; empty to let Selenium Manager find it.
CHROMEDRIVER: str = os.environ.get("CHROMEDRIVER", "")
## Folder for step screenshots; empty to take none.
SCREENSHOT_DIR: str = os.environ.get("SPEED_ISP_SCREENSHOT_DIR", "")
## Seconds to wait before a screenshot so page animations (fade-in) have finished.
SCREENSHOT_SETTLE_SECONDS: float = 2.0

## Name of the service value for X.
SERVICE_X: str = "X"
## Name of the service value for the practice service Y.
SERVICE_Y: str = "Y"

## Screenshot after opening the Y login page.
SCREENSHOT_Y_LOGIN: str = "step-1-y-login.png"
## Screenshot after opening the X login page.
SCREENSHOT_X_LOGIN: str = "step-1-x-login.png"
## Screenshot after the complaint has been posted.
SCREENSHOT_TWEET_POSTED: str = "step-4-tweet-posted.png"

## Y (verified on the site): login form fields and submit button.
Y_EMAIL_SELECTOR: str = "#email"
Y_PASSWORD_SELECTOR: str = "#password"
Y_SUBMIT_SELECTOR: str = "button[type='submit']"
## Y: inline composer (contenteditable) and post button.
Y_COMPOSER_SELECTOR: str = "#tweet-compose"
Y_POST_SELECTOR: str = "#post-btn"
## Y: button of the cosmetic cookie banner.
Y_COOKIE_BANNER_SELECTOR: str = "button[data-y-dismiss='y-cookie-banner']"

## X selectors (best effort, NOT verified live).
X_USERNAME_SELECTOR: str = "input[autocomplete='username']"
X_NEXT_XPATH: str = "//span[text()='Next']"
X_PASSWORD_SELECTOR: str = "input[name='password']"
X_LOGIN_BUTTON_SELECTOR: str = "[data-testid='LoginForm_Login_Button']"
X_COMPOSER_SELECTOR: str = "[data-testid='tweetTextarea_0']"
X_POST_SELECTOR: str = "[data-testid='tweetButtonInline']"

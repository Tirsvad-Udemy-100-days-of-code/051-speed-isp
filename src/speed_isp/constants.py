"""!
@file constants.py
@brief All constants of the project: promised speeds, URLs, limits and
       the credentials read from environment variables.

Credentials are never written in the source. They are read from the
environment when the module is imported; an unset variable gives an empty
string and the bot refuses to log in with it.
"""

import os

## Promised (contract) download speed in Mbps. Change it to your own contract.
PROMISED_DOWN: int = 150
## Promised (contract) upload speed in Mbps.
PROMISED_UP: int = 10

## Service the bot posts to: "Y" (practice service) or "X".
SERVICE: str = os.environ.get("SPEED_ISP_SERVICE", "Y").upper()

## Mock service Y login page.
Y_LOGIN_URL: str = "https://app.100daysofpython.dev/services/y/login"
## Y account e-mail, from the environment.
Y_EMAIL: str = os.environ.get("Y_EMAIL", "")
## Y account password, from the environment.
Y_PASSWORD: str = os.environ.get("Y_PASSWORD", "")

## X login page.
TWITTER_LOGIN_URL: str = "https://x.com/i/flow/login"
## X account e-mail, from the environment.
TWITTER_EMAIL: str = os.environ.get("TWITTER_EMAIL", "")
## X account password, from the environment.
TWITTER_PASSWORD: str = os.environ.get("TWITTER_PASSWORD", "")
## Optional provider handle to mention, for example "@Comcast"; empty for none.
PROVIDER_HANDLE: str = os.environ.get("SPEED_ISP_PROVIDER", "")

## Speed test page.
SPEEDTEST_URL: str = "https://www.speedtest.net/"
## Seconds to wait for the speed test to finish (60 to 180 depending on the line).
SPEEDTEST_TIMEOUT_SECONDS: int = 180
## Seconds to wait for an element on the social service.
ELEMENT_TIMEOUT_SECONDS: int = 20

## Longest allowed post, in characters.
POST_MAX_LENGTH: int = 280

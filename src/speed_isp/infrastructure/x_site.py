"""!
@file x_site.py
@brief The service X.

The selectors are best effort and have NOT been verified against the live site.
A CAPTCHA or an e-mail confirmation is not bypassed; the login then fails with
LoginError.
"""

import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from speed_isp import constants
from speed_isp.infrastructure.social_site import (
    LoginError,
    Screenshot,
    wait_clickable,
    wait_present,
)

logger = logging.getLogger(__name__)


class XSite:
    """!
    @brief Logs in to X and posts on it (selectors unverified live).
    """

    def __init__(
        self, driver: WebDriver, email: str, password: str, screenshot: Screenshot
    ) -> None:
        """!
        @param driver The Selenium driver.
        @param email The account e-mail.
        @param password The account password.
        @param screenshot Called with a file name to save a screenshot.
        """
        self._driver = driver
        self._email = email
        self._password = password
        self._screenshot = screenshot

    def login(self) -> None:
        """!
        @brief Open the login flow, enter the e-mail and the password.
        @throws LoginError when the composer does not appear after the login.
        """
        self._driver.get(constants.TWITTER_LOGIN_URL)
        self._screenshot(constants.SCREENSHOT_X_LOGIN)
        css = By.CSS_SELECTOR
        username = wait_clickable(self._driver, (css, constants.X_USERNAME_SELECTOR))
        username.send_keys(self._email)
        wait_clickable(self._driver, (By.XPATH, constants.X_NEXT_XPATH)).click()
        password = wait_clickable(self._driver, (css, constants.X_PASSWORD_SELECTOR))
        password.send_keys(self._password)
        wait_clickable(self._driver, (css, constants.X_LOGIN_BUTTON_SELECTOR)).click()
        try:
            wait_present(self._driver, (css, constants.X_COMPOSER_SELECTOR))
        except TimeoutException as error:
            raise LoginError(
                "X login did not complete (CAPTCHA, e-mail confirmation or "
                "changed page)"
            ) from error
        logger.info("Logged in to X")

    def post(self, text: str) -> None:
        """!
        @brief Type the text in the composer and click the post button.
        @param text The text to post.
        """
        css = By.CSS_SELECTOR
        composer = wait_clickable(self._driver, (css, constants.X_COMPOSER_SELECTOR))
        composer.send_keys(text)
        wait_clickable(self._driver, (css, constants.X_POST_SELECTOR)).click()
        logger.info("Posted on X")

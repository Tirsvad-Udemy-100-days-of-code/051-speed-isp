"""!
@file y_site.py
@brief The practice service Y (selectors verified against the site).
"""

import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from speed_isp import constants
from speed_isp.infrastructure.social_site import (
    LoginError,
    Screenshot,
    wait_clickable,
    wait_present,
)

logger = logging.getLogger(__name__)


class YSite:
    """!
    @brief Logs in to the Y mock service and posts on it.
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
        @brief Open the login page, dismiss the cookie banner and log in.
        @throws LoginError when the composer does not appear after the login.
        """
        self._driver.get(constants.Y_LOGIN_URL)
        self._dismiss_cookie_banner()
        self._screenshot(constants.SCREENSHOT_Y_LOGIN)
        css = By.CSS_SELECTOR
        email_field = wait_clickable(self._driver, (css, constants.Y_EMAIL_SELECTOR))
        email_field.send_keys(self._email)
        password_field = wait_clickable(
            self._driver, (css, constants.Y_PASSWORD_SELECTOR)
        )
        password_field.send_keys(self._password)
        wait_clickable(self._driver, (css, constants.Y_SUBMIT_SELECTOR)).click()
        try:
            wait_present(self._driver, (css, constants.Y_COMPOSER_SELECTOR))
        except TimeoutException as error:
            raise LoginError("Y login did not complete") from error
        logger.info("Logged in to Y")

    def post(self, text: str) -> None:
        """!
        @brief Type the text in the composer and click the post button.
        @param text The text to post.
        """
        css = By.CSS_SELECTOR
        composer = wait_clickable(self._driver, (css, constants.Y_COMPOSER_SELECTOR))
        composer.send_keys(text)
        wait_clickable(self._driver, (css, constants.Y_POST_SELECTOR)).click()
        logger.info("Posted on Y")

    def _dismiss_cookie_banner(self) -> None:
        """!
        @brief Click the cosmetic cookie banner button if it is shown.
        """
        banner_button = (By.CSS_SELECTOR, constants.Y_COOKIE_BANNER_SELECTOR)
        try:
            WebDriverWait(self._driver, constants.COOKIE_BANNER_TIMEOUT_SECONDS).until(
                ec.element_to_be_clickable(banner_button)
            ).click()
        except TimeoutException:
            logger.info("No Y cookie banner shown")

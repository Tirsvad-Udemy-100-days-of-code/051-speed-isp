"""!
@file social_site.py
@brief The port of a social site (login and post), its errors and the wait
       helpers the implementations share.
"""

from collections.abc import Callable
from typing import Protocol

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from speed_isp import constants

## Takes a screenshot with the given file name.
Screenshot = Callable[[str], None]


class MissingCredentialsError(RuntimeError):
    """!
    @brief The e-mail or password of the chosen service is not set.
    """


class LoginError(RuntimeError):
    """!
    @brief The login did not complete (wrong credentials, CAPTCHA or e-mail
           confirmation); the bot does not try to get around it.
    """


class SocialSite(Protocol):
    """!
    @brief A site the bot logs in to and posts on.
    """

    def login(self) -> None:
        """!
        @brief Log in with the credentials given to the site.
        @throws LoginError when the login does not complete.
        """
        ...

    def post(self, text: str) -> None:
        """!
        @brief Type the text in the composer and post it.
        @param text The text to post.
        """
        ...


def wait_clickable(driver: WebDriver, locator: tuple[str, str]) -> WebElement:
    """!
    @brief Wait until the element is clickable.
    @param driver The Selenium driver.
    @param locator A (By, value) pair.
    @return The element.
    @throws selenium.common.exceptions.TimeoutException after
            ELEMENT_TIMEOUT_SECONDS.
    """
    wait = WebDriverWait(driver, constants.ELEMENT_TIMEOUT_SECONDS)
    return wait.until(ec.element_to_be_clickable(locator))


def wait_present(driver: WebDriver, locator: tuple[str, str]) -> WebElement:
    """!
    @brief Wait until the element exists on the page.
    @param driver The Selenium driver.
    @param locator A (By, value) pair.
    @return The element.
    @throws selenium.common.exceptions.TimeoutException after
            ELEMENT_TIMEOUT_SECONDS.
    """
    wait = WebDriverWait(driver, constants.ELEMENT_TIMEOUT_SECONDS)
    return wait.until(ec.presence_of_element_located(locator))

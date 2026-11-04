"""!
@file site_factory.py
@brief Chooses the social site from constants.SERVICE and checks its credentials.
"""

from selenium.webdriver.remote.webdriver import WebDriver

from speed_isp import constants
from speed_isp.infrastructure.social_site import (
    MissingCredentialsError,
    Screenshot,
    SocialSite,
)
from speed_isp.infrastructure.x_site import XSite
from speed_isp.infrastructure.y_site import YSite


def create_site(driver: WebDriver, screenshot: Screenshot) -> SocialSite:
    """!
    @brief Build the site named by constants.SERVICE, before any navigation.
    @param driver The Selenium driver.
    @param screenshot Called with a file name to save a screenshot.
    @return The site, ready to log in.
    @throws ValueError when the service is neither "X" nor "Y".
    @throws MissingCredentialsError when its e-mail or password is empty.
    """
    site_class: type[YSite | XSite]
    if constants.SERVICE == constants.SERVICE_Y:
        email, password = constants.Y_EMAIL, constants.Y_PASSWORD
        names = (constants.Y_EMAIL_ENV, constants.Y_PASSWORD_ENV)
        site_class = YSite
    elif constants.SERVICE == constants.SERVICE_X:
        email, password = constants.TWITTER_EMAIL, constants.TWITTER_PASSWORD
        names = (constants.TWITTER_EMAIL_ENV, constants.TWITTER_PASSWORD_ENV)
        site_class = XSite
    else:
        raise ValueError(
            f"unknown service {constants.SERVICE!r}; use "
            f"{constants.SERVICE_X!r} or {constants.SERVICE_Y!r}"
        )
    if not email or not password:
        raise MissingCredentialsError(
            f"set the environment variables {names[0]} and {names[1]}"
        )
    return site_class(driver, email, password, screenshot)

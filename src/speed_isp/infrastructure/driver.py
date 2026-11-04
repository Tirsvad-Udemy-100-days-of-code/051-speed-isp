"""!
@file driver.py
@brief Creates the Selenium Chrome driver from the project constants.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver

from speed_isp import constants


def create_driver() -> WebDriver:
    """!
    @brief Start Chrome, headless inside Docker or when SPEED_ISP_HEADLESS is set.
    @return A ready Selenium driver.
    """
    options = Options()
    options.add_argument("--window-size=1280,900")
    if constants.CHROME_BIN:
        options.binary_location = constants.CHROME_BIN
    if constants.HEADLESS:
        for argument in ("--headless=new", "--no-sandbox", "--disable-dev-shm-usage"):
            options.add_argument(argument)
    service = Service(constants.CHROMEDRIVER) if constants.CHROMEDRIVER else Service()
    return webdriver.Chrome(service=service, options=options)

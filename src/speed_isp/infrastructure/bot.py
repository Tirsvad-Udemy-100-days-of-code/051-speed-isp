"""!
@file bot.py
@brief The Selenium bot of the assignment: InternetSpeedTwitterBot.
"""

import logging
import time
from pathlib import Path

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from speed_isp import constants
from speed_isp.domain.speed import SpeedResult, parse_mbps
from speed_isp.infrastructure.driver import create_driver

logger = logging.getLogger(__name__)


class InternetSpeedTwitterBot:
    """!
    @brief Measures the internet speed and tweets at the provider.

    The Selenium driver and the two speeds are created in the constructor,
    as in the lecture (step 2).
    """

    def __init__(self, driver: WebDriver | None = None) -> None:
        """!
        @param driver A Selenium driver; a Chrome driver is created when None.
        """
        self.driver: WebDriver = driver if driver is not None else create_driver()
        self.down: float = 0.0
        self.up: float = 0.0

    def get_internet_speed(self) -> SpeedResult:
        """!
        @brief Run the speed test on speedtest.net (lecture step 3).
        @return The measured download and upload speed in Mbps.
        @throws selenium.common.exceptions.TimeoutException when the test
                does not finish within SPEEDTEST_TIMEOUT_SECONDS.
        """
        self.driver.get(constants.SPEEDTEST_URL)
        self._reject_cookies()
        self.save_screenshot("step-2-speedtest-ready.png")
        wait = WebDriverWait(self.driver, constants.ELEMENT_TIMEOUT_SECONDS)
        go_button = (By.XPATH, constants.SPEEDTEST_GO_XPATH)
        wait.until(ec.element_to_be_clickable(go_button)).click()
        logger.info(
            "Speed test started; waiting up to %s s",
            constants.SPEEDTEST_TIMEOUT_SECONDS,
        )
        WebDriverWait(self.driver, constants.SPEEDTEST_TIMEOUT_SECONDS).until(
            ec.presence_of_element_located((By.XPATH, constants.SPEEDTEST_DONE_XPATH))
        )
        down_text = self.driver.find_element(
            By.XPATH, constants.SPEEDTEST_DOWN_XPATH
        ).text
        up_text = self.driver.find_element(By.XPATH, constants.SPEEDTEST_UP_XPATH).text
        self.down = parse_mbps(down_text)
        self.up = parse_mbps(up_text)
        logger.info("Download: %s Mbps, upload: %s Mbps", self.down, self.up)
        self.save_screenshot("step-3-speedtest-result.png")
        return SpeedResult(down=self.down, up=self.up)

    def tweet_at_provider(self) -> None:
        """!
        @brief Post the complaint (lecture step 4; implemented in MIL-003).
        """
        logger.info("tweet_at_provider is not implemented yet")

    def save_screenshot(self, name: str) -> None:
        """!
        @brief Save a screenshot when SPEED_ISP_SCREENSHOT_DIR is set.
        @param name File name of the image.
        """
        if not constants.SCREENSHOT_DIR:
            return
        time.sleep(constants.SCREENSHOT_SETTLE_SECONDS)
        folder = Path(constants.SCREENSHOT_DIR)
        folder.mkdir(parents=True, exist_ok=True)
        self.driver.save_screenshot(str(folder / name))

    def close(self) -> None:
        """!
        @brief Close the browser.
        """
        self.driver.quit()

    def _reject_cookies(self) -> None:
        """!
        @brief Decline non-essential cookies if the banner is shown.
        """
        banner_button = (By.XPATH, constants.SPEEDTEST_REJECT_COOKIES_XPATH)
        try:
            WebDriverWait(self.driver, constants.COOKIE_BANNER_TIMEOUT_SECONDS).until(
                ec.element_to_be_clickable(banner_button)
            ).click()
        except TimeoutException:
            logger.info("No cookie banner shown")

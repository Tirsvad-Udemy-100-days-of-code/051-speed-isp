"""!
@file test_speed_bot.py
@brief Tests of InternetSpeedTwitterBot with a hand-written fake driver.
"""

from pathlib import Path
from typing import cast

import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver

from speed_isp import constants
from speed_isp.domain.speed import SpeedResult
from speed_isp.infrastructure.bot import InternetSpeedTwitterBot


class FakeElement:
    """!
    @brief A page element that is displayed and enabled.
    """

    def __init__(self, text: str = "") -> None:
        self.text = text
        self.clicked = False

    def click(self) -> None:
        self.clicked = True

    def is_displayed(self) -> bool:
        return True

    def is_enabled(self) -> bool:
        return True


class FakeDriver:
    """!
    @brief A driver that answers find_element from a dict keyed by XPath.
    """

    def __init__(self, elements: dict[str, FakeElement]) -> None:
        self.elements = elements
        self.visited: list[str] = []
        self.quit_called = False
        self.screenshots: list[str] = []

    def get(self, url: str) -> None:
        self.visited.append(url)

    def find_element(self, by: str, value: str) -> FakeElement:
        if value not in self.elements:
            raise NoSuchElementException(value)
        return self.elements[value]

    def quit(self) -> None:
        self.quit_called = True

    def save_screenshot(self, path: str) -> bool:
        self.screenshots.append(path)
        Path(path).write_bytes(b"png")
        return True


def make_bot(driver: FakeDriver) -> InternetSpeedTwitterBot:
    return InternetSpeedTwitterBot(driver=cast(WebDriver, driver))


def full_page(with_banner: bool = True) -> dict[str, FakeElement]:
    page: dict[str, FakeElement] = {
        constants.SPEEDTEST_GO_XPATH: FakeElement(),
        constants.SPEEDTEST_DONE_XPATH: FakeElement("Result ID"),
        constants.SPEEDTEST_DOWN_XPATH: FakeElement("94.01"),
        constants.SPEEDTEST_UP_XPATH: FakeElement("1,2.5"),
    }
    if with_banner:
        page[constants.SPEEDTEST_REJECT_COOKIES_XPATH] = FakeElement()
    return page


@pytest.fixture(autouse=True)
def fast_timeouts(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(constants, "COOKIE_BANNER_TIMEOUT_SECONDS", 0)
    monkeypatch.setattr(constants, "ELEMENT_TIMEOUT_SECONDS", 1)
    monkeypatch.setattr(constants, "SPEEDTEST_TIMEOUT_SECONDS", 1)
    monkeypatch.setattr(constants, "SCREENSHOT_DIR", "")
    monkeypatch.setattr(constants, "SCREENSHOT_SETTLE_SECONDS", 0)


def test_new_bot_starts_with_zero_speeds() -> None:
    bot = make_bot(FakeDriver({}))
    assert (bot.down, bot.up) == (0.0, 0.0)


def test_get_internet_speed_sets_speeds_and_returns_result() -> None:
    driver = FakeDriver(full_page())
    bot = make_bot(driver)
    result = bot.get_internet_speed()
    assert (bot.down, bot.up) == (94.01, 12.5)
    assert result == SpeedResult(down=94.01, up=12.5)
    assert driver.visited == [constants.SPEEDTEST_URL]


def test_get_internet_speed_clicks_go_and_rejects_banner() -> None:
    page = full_page()
    make_bot(FakeDriver(page)).get_internet_speed()
    assert page[constants.SPEEDTEST_GO_XPATH].clicked
    assert page[constants.SPEEDTEST_REJECT_COOKIES_XPATH].clicked


def test_get_internet_speed_works_without_cookie_banner() -> None:
    result = make_bot(FakeDriver(full_page(with_banner=False))).get_internet_speed()
    assert result.down == 94.01


def test_get_internet_speed_times_out_when_test_never_finishes() -> None:
    page = full_page()
    del page[constants.SPEEDTEST_DONE_XPATH]
    with pytest.raises(TimeoutException):
        make_bot(FakeDriver(page)).get_internet_speed()


def test_close_quits_the_driver() -> None:
    driver = FakeDriver({})
    make_bot(driver).close()
    assert driver.quit_called


def test_save_screenshot_does_nothing_without_directory() -> None:
    driver = FakeDriver({})
    make_bot(driver).save_screenshot("a.png")
    assert driver.screenshots == []


def test_save_screenshot_writes_file_when_directory_set(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    folder = tmp_path / "shots"
    monkeypatch.setattr(constants, "SCREENSHOT_DIR", str(folder))
    driver = FakeDriver({})
    make_bot(driver).save_screenshot("a.png")
    assert (folder / "a.png").read_bytes() == b"png"


def test_get_internet_speed_saves_ready_and_result_screenshots(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setattr(constants, "SCREENSHOT_DIR", str(tmp_path))
    make_bot(FakeDriver(full_page())).get_internet_speed()
    assert (tmp_path / "step-2-speedtest-ready.png").exists()
    assert (tmp_path / "step-3-speedtest-result.png").exists()


def test_tweet_at_provider_is_a_noop_for_now() -> None:
    driver = FakeDriver({})
    bot = make_bot(driver)
    bot.tweet_at_provider()
    assert driver.visited == []

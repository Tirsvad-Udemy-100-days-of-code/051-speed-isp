"""!
@file test_tweet_sites.py
@brief Tests of YSite, XSite, the site choice and tweet_at_provider with a
       fake driver.
"""

import logging
from pathlib import Path
from typing import cast

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver

from speed_isp import constants
from speed_isp.infrastructure.bot import InternetSpeedTwitterBot
from speed_isp.infrastructure.site_factory import create_site
from speed_isp.infrastructure.social_site import LoginError, MissingCredentialsError
from speed_isp.infrastructure.x_site import XSite
from speed_isp.infrastructure.y_site import YSite

EMAIL = "someone@example.test"
PASSWORD = "s3cret-pw-value"


class FakeElement:
    """!
    @brief An element that records clicks and typing in a shared event list.
    """

    def __init__(self, name: str, events: list[str]) -> None:
        self.name = name
        self.events = events

    def click(self) -> None:
        self.events.append(f"click {self.name}")

    def send_keys(self, text: str) -> None:
        self.events.append(f"type {self.name} {text}")

    def is_displayed(self) -> bool:
        return True

    def is_enabled(self) -> bool:
        return True


class FakeDriver:
    """!
    @brief A driver whose page holds the elements whose selector is in `present`.
    """

    def __init__(self, present: set[str]) -> None:
        self.present = present
        self.events: list[str] = []
        self.visited: list[str] = []
        self.screenshots: list[str] = []

    def get(self, url: str) -> None:
        self.visited.append(url)
        self.events.append(f"get {url}")

    def find_element(self, by: str, value: str) -> FakeElement:
        if value not in self.present:
            raise NoSuchElementException(value)
        return FakeElement(value, self.events)

    def save_screenshot(self, path: str) -> bool:
        self.screenshots.append(path)
        return True


Y_PAGE = {
    constants.Y_COOKIE_BANNER_SELECTOR,
    constants.Y_EMAIL_SELECTOR,
    constants.Y_PASSWORD_SELECTOR,
    constants.Y_SUBMIT_SELECTOR,
    constants.Y_COMPOSER_SELECTOR,
    constants.Y_POST_SELECTOR,
}
X_PAGE = {
    constants.X_USERNAME_SELECTOR,
    constants.X_NEXT_XPATH,
    constants.X_PASSWORD_SELECTOR,
    constants.X_LOGIN_BUTTON_SELECTOR,
    constants.X_COMPOSER_SELECTOR,
    constants.X_POST_SELECTOR,
}


@pytest.fixture(autouse=True)
def configured(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(constants, "COOKIE_BANNER_TIMEOUT_SECONDS", 0)
    monkeypatch.setattr(constants, "ELEMENT_TIMEOUT_SECONDS", 0.2)
    monkeypatch.setattr(constants, "SCREENSHOT_DIR", "")
    monkeypatch.setattr(constants, "SCREENSHOT_SETTLE_SECONDS", 0)
    monkeypatch.setattr(constants, "SERVICE", "Y")
    monkeypatch.setattr(constants, "Y_EMAIL", EMAIL)
    monkeypatch.setattr(constants, "Y_PASSWORD", PASSWORD)
    monkeypatch.setattr(constants, "TWITTER_EMAIL", EMAIL)
    monkeypatch.setattr(constants, "TWITTER_PASSWORD", PASSWORD)
    monkeypatch.setattr(constants, "PROVIDER_HANDLE", "@Isp")
    monkeypatch.setattr(constants, "PROMISED_DOWN", 150)
    monkeypatch.setattr(constants, "PROMISED_UP", 10)


def as_driver(driver: FakeDriver) -> WebDriver:
    return cast(WebDriver, driver)


def make_bot(driver: FakeDriver, down: float, up: float) -> InternetSpeedTwitterBot:
    bot = InternetSpeedTwitterBot(driver=as_driver(driver))
    bot.down, bot.up = down, up
    return bot


def test_y_site_login_and_post_call_sequence() -> None:
    driver = FakeDriver(set(Y_PAGE))
    shots: list[str] = []
    site = YSite(as_driver(driver), EMAIL, PASSWORD, shots.append)
    site.login()
    site.post("hello")
    assert driver.events == [
        f"get {constants.Y_LOGIN_URL}",
        f"click {constants.Y_COOKIE_BANNER_SELECTOR}",
        f"type {constants.Y_EMAIL_SELECTOR} {EMAIL}",
        f"type {constants.Y_PASSWORD_SELECTOR} {PASSWORD}",
        f"click {constants.Y_SUBMIT_SELECTOR}",
        f"type {constants.Y_COMPOSER_SELECTOR} hello",
        f"click {constants.Y_POST_SELECTOR}",
    ]
    assert shots == [constants.SCREENSHOT_Y_LOGIN]


def test_y_site_login_works_without_cookie_banner() -> None:
    driver = FakeDriver(Y_PAGE - {constants.Y_COOKIE_BANNER_SELECTOR})
    YSite(as_driver(driver), EMAIL, PASSWORD, lambda name: None).login()
    assert f"click {constants.Y_SUBMIT_SELECTOR}" in driver.events


def test_y_site_login_raises_when_composer_never_appears() -> None:
    driver = FakeDriver(Y_PAGE - {constants.Y_COMPOSER_SELECTOR})
    site = YSite(as_driver(driver), EMAIL, PASSWORD, lambda name: None)
    with pytest.raises(LoginError) as info:
        site.login()
    assert PASSWORD not in str(info.value)
    assert EMAIL not in str(info.value)


def test_x_site_login_and_post_call_sequence() -> None:
    driver = FakeDriver(set(X_PAGE))
    shots: list[str] = []
    site = XSite(as_driver(driver), EMAIL, PASSWORD, shots.append)
    site.login()
    site.post("hello")
    assert driver.events == [
        f"get {constants.TWITTER_LOGIN_URL}",
        f"type {constants.X_USERNAME_SELECTOR} {EMAIL}",
        f"click {constants.X_NEXT_XPATH}",
        f"type {constants.X_PASSWORD_SELECTOR} {PASSWORD}",
        f"click {constants.X_LOGIN_BUTTON_SELECTOR}",
        f"type {constants.X_COMPOSER_SELECTOR} hello",
        f"click {constants.X_POST_SELECTOR}",
    ]
    assert shots == [constants.SCREENSHOT_X_LOGIN]


def test_x_site_login_raises_when_composer_never_appears() -> None:
    driver = FakeDriver(X_PAGE - {constants.X_COMPOSER_SELECTOR})
    site = XSite(as_driver(driver), EMAIL, PASSWORD, lambda name: None)
    with pytest.raises(LoginError):
        site.login()


@pytest.mark.parametrize(
    ("service", "prefix", "env_names"),
    [
        ("Y", "Y", ("Y_EMAIL", "Y_PASSWORD")),
        ("X", "TWITTER", ("TWITTER_EMAIL", "TWITTER_PASSWORD")),
    ],
)
@pytest.mark.parametrize("missing", ["EMAIL", "PASSWORD"])
def test_missing_credentials_raise_before_navigation(
    monkeypatch: pytest.MonkeyPatch,
    service: str,
    prefix: str,
    env_names: tuple[str, str],
    missing: str,
) -> None:
    monkeypatch.setattr(constants, "SERVICE", service)
    monkeypatch.setattr(constants, f"{prefix}_{missing}", "")
    driver = FakeDriver(set())
    bot = make_bot(driver, 1, 1)
    with pytest.raises(MissingCredentialsError) as info:
        bot.tweet_at_provider()
    assert all(name in str(info.value) for name in env_names)
    assert PASSWORD not in str(info.value)
    assert driver.visited == []


def test_missing_credentials_error_is_a_runtime_error() -> None:
    assert issubclass(MissingCredentialsError, RuntimeError)


def test_create_site_chooses_site_from_service(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    driver = as_driver(FakeDriver(set()))
    assert isinstance(create_site(driver, lambda name: None), YSite)
    monkeypatch.setattr(constants, "SERVICE", "X")
    assert isinstance(create_site(driver, lambda name: None), XSite)


def test_tweet_at_provider_posts_to_y_when_speed_is_low() -> None:
    driver = FakeDriver(set(Y_PAGE))
    make_bot(driver, 94.7, 8).tweet_at_provider()
    typed = f"type {constants.Y_COMPOSER_SELECTOR} "
    posted = [e for e in driver.events if e.startswith(typed)]
    assert posted == [
        typed + "Hey @Isp, why is my internet speed 94.7down/8up "
        "when I pay for 150down/10up?"
    ]
    assert driver.events[-1] == f"click {constants.Y_POST_SELECTOR}"


def test_tweet_at_provider_posts_to_x_when_service_is_x(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(constants, "SERVICE", "X")
    driver = FakeDriver(set(X_PAGE))
    make_bot(driver, 94.7, 8).tweet_at_provider()
    assert driver.visited == [constants.TWITTER_LOGIN_URL]
    assert driver.events[-1] == f"click {constants.X_POST_SELECTOR}"


def test_tweet_at_provider_skips_when_speed_is_fine(
    caplog: pytest.LogCaptureFixture,
) -> None:
    driver = FakeDriver(set(Y_PAGE))
    with caplog.at_level(logging.INFO):
        make_bot(driver, 150, 10).tweet_at_provider()
    assert driver.events == []
    assert "no complaint needed" in caplog.text


def test_tweet_at_provider_rejects_unknown_service(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(constants, "SERVICE", "MASTODON")
    driver = FakeDriver(set())
    with pytest.raises(ValueError, match="unknown service"):
        make_bot(driver, 1, 1).tweet_at_provider()
    assert driver.visited == []


def test_tweet_at_provider_saves_login_and_posted_screenshots(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setattr(constants, "SCREENSHOT_DIR", str(tmp_path))
    driver = FakeDriver(set(Y_PAGE))
    make_bot(driver, 1, 1).tweet_at_provider()
    names = [Path(path).name for path in driver.screenshots]
    assert names == [constants.SCREENSHOT_Y_LOGIN, constants.SCREENSHOT_TWEET_POSTED]


def test_no_credential_value_appears_in_logs(
    caplog: pytest.LogCaptureFixture,
) -> None:
    driver = FakeDriver(set(Y_PAGE))
    with caplog.at_level(logging.DEBUG):
        make_bot(driver, 1, 1).tweet_at_provider()
    assert PASSWORD not in caplog.text
    assert EMAIL not in caplog.text

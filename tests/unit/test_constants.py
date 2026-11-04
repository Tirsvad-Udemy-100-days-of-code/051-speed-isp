"""!
@file test_constants.py
@brief Tests of the project constants.
"""

import importlib

import pytest

from speed_isp import constants


def test_promised_speeds_are_positive() -> None:
    assert constants.PROMISED_DOWN > 0
    assert constants.PROMISED_UP > 0


def test_urls_use_https() -> None:
    for url in (
        constants.SPEEDTEST_URL,
        constants.Y_LOGIN_URL,
        constants.TWITTER_LOGIN_URL,
    ):
        assert url.startswith("https://")


def test_service_is_x_or_y() -> None:
    assert constants.SERVICE in {"X", "Y"}


def test_credentials_are_not_hard_coded(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("Y_PASSWORD", raising=False)
    monkeypatch.delenv("TWITTER_PASSWORD", raising=False)
    try:
        reloaded = importlib.reload(constants)
        assert reloaded.Y_PASSWORD == ""
        assert reloaded.TWITTER_PASSWORD == ""
    finally:
        monkeypatch.undo()
        importlib.reload(constants)

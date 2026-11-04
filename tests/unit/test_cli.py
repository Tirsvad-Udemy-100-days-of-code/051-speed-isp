"""!
@file test_cli.py
@brief Tests of the command line entry point with a fake bot.
"""

from typing import ClassVar

import pytest

from speed_isp.domain.speed import SpeedResult
from speed_isp.presentation import cli


class FakeCliBot:
    """!
    @brief A bot that records calls; it can fail while measuring.
    """

    fail = False
    calls: ClassVar[list[str]] = []

    def get_internet_speed(self) -> SpeedResult:
        self.calls.append("get_internet_speed")
        if self.fail:
            raise RuntimeError("boom")
        return SpeedResult(down=1.0, up=1.0)

    def tweet_at_provider(self) -> None:
        self.calls.append("tweet_at_provider")

    def close(self) -> None:
        self.calls.append("close")


@pytest.fixture
def fake_bot(monkeypatch: pytest.MonkeyPatch) -> type[FakeCliBot]:
    FakeCliBot.fail = False
    FakeCliBot.calls = []
    monkeypatch.setattr(cli, "InternetSpeedTwitterBot", FakeCliBot)
    return FakeCliBot


def test_main_runs_steps_in_order_and_closes(fake_bot: type[FakeCliBot]) -> None:
    assert cli.main() == 0
    assert fake_bot.calls == ["get_internet_speed", "tweet_at_provider", "close"]


def test_main_closes_bot_when_measuring_fails(fake_bot: type[FakeCliBot]) -> None:
    fake_bot.fail = True
    with pytest.raises(RuntimeError, match="boom"):
        cli.main()
    assert fake_bot.calls == ["get_internet_speed", "close"]

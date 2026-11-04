"""!
@file test_cli.py
@brief Tests of the command line entry point with a fake bot.
"""

from typing import ClassVar

import pytest

from speed_isp.domain.speed import SpeedResult
from speed_isp.infrastructure.social_site import LoginError, MissingCredentialsError
from speed_isp.presentation import cli


class FakeCliBot:
    """!
    @brief A bot that records calls; it can fail while measuring.
    """

    fail = False
    tweet_error: Exception | None = None
    calls: ClassVar[list[str]] = []

    def get_internet_speed(self) -> SpeedResult:
        self.calls.append("get_internet_speed")
        if self.fail:
            raise RuntimeError("boom")
        return SpeedResult(down=1.0, up=1.0)

    def tweet_at_provider(self) -> None:
        self.calls.append("tweet_at_provider")
        if self.tweet_error is not None:
            raise self.tweet_error

    def close(self) -> None:
        self.calls.append("close")


@pytest.fixture
def fake_bot(monkeypatch: pytest.MonkeyPatch) -> type[FakeCliBot]:
    FakeCliBot.fail = False
    FakeCliBot.tweet_error = None
    FakeCliBot.calls = []
    monkeypatch.setattr(cli, "InternetSpeedTwitterBot", FakeCliBot)
    return FakeCliBot


def test_main_runs_steps_in_order_and_closes(fake_bot: type[FakeCliBot]) -> None:
    assert cli.main() == 0
    assert fake_bot.calls == ["get_internet_speed", "tweet_at_provider", "close"]


@pytest.mark.parametrize(
    "error",
    [
        MissingCredentialsError("set the environment variables A and B"),
        LoginError("login did not complete"),
    ],
)
def test_main_returns_one_and_logs_message_for_expected_errors(
    fake_bot: type[FakeCliBot],
    caplog: pytest.LogCaptureFixture,
    error: Exception,
) -> None:
    fake_bot.tweet_error = error
    assert cli.main() == 1
    assert fake_bot.calls == ["get_internet_speed", "tweet_at_provider", "close"]
    assert str(error) in caplog.text
    assert "Traceback" not in caplog.text
    assert all(record.exc_info is None for record in caplog.records)


def test_main_closes_bot_when_measuring_fails(fake_bot: type[FakeCliBot]) -> None:
    fake_bot.fail = True
    with pytest.raises(RuntimeError, match="boom"):
        cli.main()
    assert fake_bot.calls == ["get_internet_speed", "close"]

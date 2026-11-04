"""!
@file test_run_bot.py
@brief Tests of the run_bot use case with a fake bot.
"""

from speed_isp.application.run_bot import run_bot
from speed_isp.domain.speed import SpeedResult


class FakeBot:
    """!
    @brief A bot that records the order of the calls.
    """

    def __init__(self) -> None:
        self.calls: list[str] = []

    def get_internet_speed(self) -> SpeedResult:
        self.calls.append("get_internet_speed")
        return SpeedResult(down=90.5, up=8.0)

    def tweet_at_provider(self) -> None:
        self.calls.append("tweet_at_provider")


def test_run_bot_measures_before_tweeting() -> None:
    bot = FakeBot()
    run_bot(bot)
    assert bot.calls == ["get_internet_speed", "tweet_at_provider"]


def test_run_bot_returns_measured_speed() -> None:
    assert run_bot(FakeBot()) == SpeedResult(down=90.5, up=8.0)

"""!
@file run_bot.py
@brief The use case: measure the speed first, then tweet at the provider.
"""

from typing import Protocol

from speed_isp.domain.speed import SpeedResult


class SpeedBot(Protocol):
    """!
    @brief What the use case needs from a bot (a port).
    """

    def get_internet_speed(self) -> SpeedResult:
        """!
        @brief Measure the current download and upload speed.
        @return The measured speed.
        """
        ...

    def tweet_at_provider(self) -> None:
        """!
        @brief Post the complaint about the measured speed.
        """
        ...


def run_bot(bot: SpeedBot) -> SpeedResult:
    """!
    @brief Run the two steps of the assignment in order.
    @param bot The bot that does the work.
    @return The measured speed.
    """
    result = bot.get_internet_speed()
    bot.tweet_at_provider()
    return result

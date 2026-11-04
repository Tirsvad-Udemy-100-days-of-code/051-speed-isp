"""!
@file cli.py
@brief Command line entry point: create the bot and run it.
"""

import logging

from speed_isp.application.run_bot import run_bot
from speed_isp.infrastructure.bot import InternetSpeedTwitterBot


def main() -> int:
    """!
    @brief Measure the internet speed and tweet at the provider.
    @return Process exit code, 0 on success.
    """
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    bot = InternetSpeedTwitterBot()
    try:
        run_bot(bot)
    finally:
        bot.close()
    return 0

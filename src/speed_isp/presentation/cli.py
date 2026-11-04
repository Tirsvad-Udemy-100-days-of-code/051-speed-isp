"""!
@file cli.py
@brief Command line entry point: create the bot and run it.
"""

import logging

from speed_isp.application.run_bot import run_bot
from speed_isp.infrastructure.bot import InternetSpeedTwitterBot
from speed_isp.infrastructure.social_site import LoginError, MissingCredentialsError

logger = logging.getLogger(__name__)


def main() -> int:
    """!
    @brief Measure the internet speed and tweet at the provider.
    @return Process exit code, 0 on success, 1 when credentials are missing or
            the login does not complete.
    """
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    bot = InternetSpeedTwitterBot()
    try:
        run_bot(bot)
    except (MissingCredentialsError, LoginError) as error:
        logger.error("%s", error)
        return 1
    finally:
        bot.close()
    return 0

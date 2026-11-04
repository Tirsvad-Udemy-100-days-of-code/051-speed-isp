"""!
@file speed.py
@brief The measured internet speed and the rule that compares it with the
       promised speed.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SpeedResult:
    """!
    @brief A measured download and upload speed.
    Attributes: down is the download speed in Mbps, up the upload speed in Mbps.
    """

    down: float
    up: float

    def is_below(self, promised_down: float, promised_up: float) -> bool:
        """!
        @brief Tell whether either measured speed is under the promised speed.
        @param promised_down Promised download speed in Mbps.
        @param promised_up Promised upload speed in Mbps.
        @return True when the download or the upload speed is too low.
        """
        return self.down < promised_down or self.up < promised_up


def parse_mbps(text: str) -> float:
    """!
    @brief Read a speed such as "94.01" or "1,024.5 Mbps" from page text.
    @param text The text of the page element.
    @return The speed as a number.
    @throws ValueError when the text holds no number.
    """
    cleaned = text.replace(",", "").replace("Mbps", "").strip()
    try:
        return float(cleaned)
    except ValueError as error:
        raise ValueError(f"not a speed: {text!r}") from error

"""!
@file complaint.py
@brief The rule that composes the complaint text sent to the provider.
"""

from speed_isp.domain.speed import SpeedResult

## Longest post allowed on X.
COMPLAINT_MAX_LENGTH: int = 280


def format_speed(value: float) -> str:
    """!
    @brief Format a speed in Mbps without trailing noise (94.7, 150).
    @param value The speed in Mbps.
    @return The speed with at most one decimal.
    """
    return f"{value:.1f}".rstrip("0").rstrip(".")


def compose_complaint(
    result: SpeedResult,
    promised_down: float,
    promised_up: float,
    provider_handle: str = "",
    max_length: int = COMPLAINT_MAX_LENGTH,
) -> str:
    """!
    @brief Compose the complaint with measured and promised speeds.
    @param result The measured speeds.
    @param promised_down Promised download speed in Mbps.
    @param promised_up Promised upload speed in Mbps.
    @param provider_handle Handle to mention, for example "@Comcast"; empty for none.
    @param max_length Longest allowed text in characters.
    @return The complaint text.
    @throws ValueError when the text is longer than max_length.
    """
    handle = provider_handle.strip()
    mention = f" {handle}" if handle else ""
    text = (
        f"Hey{mention}, why is my internet speed "
        f"{format_speed(result.down)}down/{format_speed(result.up)}up "
        f"when I pay for "
        f"{format_speed(promised_down)}down/{format_speed(promised_up)}up?"
    )
    if len(text) > max_length:
        raise ValueError(
            f"complaint is {len(text)} characters, longer than {max_length}"
        )
    return text

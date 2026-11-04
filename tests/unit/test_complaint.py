"""!
@file test_complaint.py
@brief Tests of the complaint text rule.
"""

import pytest

from speed_isp.domain.complaint import compose_complaint, format_speed
from speed_isp.domain.speed import SpeedResult


def test_compose_complaint_without_handle_has_no_mention() -> None:
    text = compose_complaint(SpeedResult(94.7, 8.0), 150, 10)
    assert text == (
        "Hey, why is my internet speed 94.7down/8up when I pay for 150down/10up?"
    )


def test_compose_complaint_with_handle_mentions_provider() -> None:
    text = compose_complaint(SpeedResult(94.7, 8.0), 150, 10, "@Comcast")
    assert text.startswith("Hey @Comcast, why")


def test_compose_complaint_ignores_blank_handle() -> None:
    text = compose_complaint(SpeedResult(1, 1), 150, 10, "   ")
    assert text.startswith("Hey, why")


def test_compose_complaint_fits_default_limit() -> None:
    text = compose_complaint(SpeedResult(94.7, 8.0), 150, 10, "@Comcast")
    assert len(text) <= 280


def test_compose_complaint_raises_when_longer_than_max_length() -> None:
    with pytest.raises(ValueError, match="longer than"):
        compose_complaint(SpeedResult(94.7, 8.0), 150, 10, max_length=10)


def test_compose_complaint_accepts_text_of_exactly_max_length() -> None:
    text = compose_complaint(SpeedResult(94.7, 8.0), 150, 10)
    assert compose_complaint(SpeedResult(94.7, 8.0), 150, 10, max_length=len(text))


def test_compose_complaint_raises_for_very_long_handle() -> None:
    with pytest.raises(ValueError):
        compose_complaint(SpeedResult(1, 1), 150, 10, "@" + "a" * 300)


@pytest.mark.parametrize(
    ("value", "expected"),
    [(94.7, "94.7"), (150.0, "150"), (94.01, "94"), (0.0, "0"), (1234.56, "1234.6")],
)
def test_format_speed_drops_trailing_noise(value: float, expected: str) -> None:
    assert format_speed(value) == expected

"""!
@file test_speed.py
@brief Tests of the speed value object and the speed text parser.
"""

import dataclasses

import pytest

from speed_isp.domain.speed import SpeedResult, parse_mbps


def test_is_below_when_download_is_low() -> None:
    assert SpeedResult(down=100, up=20).is_below(150, 10)


def test_is_below_when_upload_is_low() -> None:
    assert SpeedResult(down=200, up=5).is_below(150, 10)


def test_is_below_false_when_both_meet_promise() -> None:
    assert not SpeedResult(down=150, up=10).is_below(150, 10)


def test_speed_result_is_immutable() -> None:
    result = SpeedResult(down=1, up=2)
    with pytest.raises(dataclasses.FrozenInstanceError):
        result.down = 5  # type: ignore[misc]


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("94.01", 94.01),
        ("1,024.5", 1024.5),
        (" 12 Mbps ", 12.0),
        ("0", 0.0),
    ],
)
def test_parse_mbps_reads_number(text: str, expected: float) -> None:
    assert parse_mbps(text) == expected


@pytest.mark.parametrize("text", ["", "--", "fast"])
def test_parse_mbps_rejects_non_number(text: str) -> None:
    with pytest.raises(ValueError, match="not a speed"):
        parse_mbps(text)

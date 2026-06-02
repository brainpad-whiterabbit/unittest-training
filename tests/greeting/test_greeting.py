from greeting.greeting import get_greeting
from unittest.mock import patch
import datetime
import pytest

MORNING = "Good morning!"
AFTERNOON = "Good afternoon!"
EVENING = "Good evening!"
NIGHT = "Good night!"


@pytest.mark.parametrize(
    ["hour", "minute", "second", "expected_greeting"],
    [
        # 朝の境界値と代表値
        (5, 0, 0, MORNING),
        (9, 30, 0, MORNING),
        (11, 59, 59, MORNING),
        # 昼の境界値と代表値
        (12, 00, 00, AFTERNOON),
        (14, 30, 0, AFTERNOON),
        (17, 59, 59, AFTERNOON),
        # 夕方の境界値と代表値
        (18, 00, 00, EVENING),
        (20, 30, 00, EVENING),
        (21, 59, 59, EVENING),
        # 夜の境界値と代表値
        (22, 00, 00, NIGHT),
        (23, 30, 00, NIGHT),
        (4, 59, 59, NIGHT),
    ],
)
def test_get_greeting_with_mock(hour, minute, second, expected_greeting):
    with patch("greeting.greeting.datetime", wraps=datetime) as mock_datetime:
        mocked_now = datetime.datetime(2024, 1, 1, hour, minute, second)
        mock_datetime.datetime.now.return_value = mocked_now

        assert get_greeting() == expected_greeting

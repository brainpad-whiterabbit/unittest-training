from unittest.mock import patch
from datetime import time
from greeting.greeting import get_greeting
import pytest


@pytest.mark.parametrize(
    "mock_time,expected_greeting",
    [
        # 朝（5:00:00 - 11:59:59）の境界値テスト
        (time(4, 59, 59), "Good night!"),  # 夜の最後
        (time(5, 0, 0), "Good morning!"),  # 朝の開始
        (time(5, 0, 1), "Good morning!"),  # 朝の開始直後
        (time(8, 30, 0), "Good morning!"),  # 朝の中間
        (time(11, 59, 59), "Good morning!"),  # 朝の最後
        (time(12, 0, 0), "Good afternoon!"),  # 昼の開始
        # 昼（12:00:00 - 17:59:59）の境界値テスト
        (time(11, 59, 59), "Good morning!"),  # 朝の最後
        (time(12, 0, 0), "Good afternoon!"),  # 昼の開始
        (time(12, 0, 1), "Good afternoon!"),  # 昼の開始直後
        (time(14, 30, 0), "Good afternoon!"),  # 昼の中間
        (time(17, 59, 59), "Good afternoon!"),  # 昼の最後
        (time(18, 0, 0), "Good evening!"),  # 夕方の開始
        # 夕方（18:00:00 - 21:59:59）の境界値テスト
        (time(17, 59, 59), "Good afternoon!"),  # 昼の最後
        (time(18, 0, 0), "Good evening!"),  # 夕方の開始
        (time(18, 0, 1), "Good evening!"),  # 夕方の開始直後
        (time(20, 0, 0), "Good evening!"),  # 夕方の中間
        (time(21, 59, 59), "Good evening!"),  # 夕方の最後
        (time(22, 0, 0), "Good night!"),  # 夜の開始
        # 夜（22:00:00 - 4:59:59）の境界値テスト
        (time(21, 59, 59), "Good evening!"),  # 夕方の最後
        (time(22, 0, 0), "Good night!"),  # 夜の開始
        (time(22, 0, 1), "Good night!"),  # 夜の開始直後
        (time(23, 0, 0), "Good night!"),  # 夜の中間
        (time(4, 59, 59), "Good night!"),  # 夜の最後
    ],
)
def test_greeting(mock_time, expected_greeting):
    # Act
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value.time.return_value = mock_time
        mock_datetime_module.time = time
        result = get_greeting()

    # Assert
    assert result == expected_greeting


class FakeInvalidTime:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __le__(self, other):
        raise ValueError(f"invalid time {self.hour}:{self.minute}:{self.second}")

    def __lt__(self, other):
        raise ValueError(f"invalid time {self.hour}:{self.minute}:{self.second}")

    def __ge__(self, other):
        raise ValueError(f"invalid time {self.hour}:{self.minute}:{self.second}")

    def __gt__(self, other):
        raise ValueError(f"invalid time {self.hour}:{self.minute}:{self.second}")

    def __repr__(self):
        return f"FakeInvalidTime({self.hour},{self.minute},{self.second})"


@pytest.mark.parametrize(
    "mock_time",
    [
        FakeInvalidTime(25, 0, 0),
        FakeInvalidTime(23, 60, 0),
        FakeInvalidTime(23, 59, 60),
    ],
)
def test_greeting_invalid_time_raises(mock_time):
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value.time.return_value = mock_time
        mock_datetime_module.time = time

        with pytest.raises(ValueError):
            get_greeting()

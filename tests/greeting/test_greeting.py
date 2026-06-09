import datetime as real_datetime
from unittest.mock import MagicMock, patch
from greeting.greeting import get_greeting


# 1. 正常系のテスト
def test_get_greeting_all_cases():
    with patch("greeting.greeting.datetime", MagicMock(wraps=real_datetime)) as mock_dt:
        cases = [
            (8, "Good morning!"),
            (14, "Good afternoon!"),
            (19, "Good evening!"),
            (23, "Good night!"),
        ]
        for hour, expected in cases:
            mock_dt.datetime.now.return_value = real_datetime.datetime(
                2026, 6, 2, hour, 0, 0
            )
            assert get_greeting() == expected


# 2. 境界値のテスト
def test_get_greeting_boundaries():
    with patch("greeting.greeting.datetime", MagicMock(wraps=real_datetime)) as mock_dt:
        boundaries = [
            (5, "Good morning!"),
            (12, "Good afternoon!"),
            (18, "Good evening!"),
            (22, "Good night!"),
        ]
        for hour, expected in boundaries:
            mock_dt.datetime.now.return_value = real_datetime.datetime(
                2026, 6, 2, hour, 0, 0
            )
            assert get_greeting() == expected

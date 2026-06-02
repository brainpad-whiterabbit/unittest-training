import datetime
from unittest.mock import patch
import pytest
from greeting.greeting import get_greeting


@pytest.mark.parametrize(
    "hour, minute, expected",
    [
        # 1. 朝 (5:00 ~ 11:59)
        (5, 0, "Good morning!"),  # 境界値（始まり）
        (11, 59, "Good morning!"),  # 境界値（終わり）
        # 2. 昼 (12:00 ~ 17:59)
        (12, 0, "Good afternoon!"),  # 境界値（始まり）
        (17, 59, "Good afternoon!"),  # 境界値（終わり）
        # 3. 夕 (18:00 ~ 21:59)
        (18, 0, "Good evening!"),  # 境界値（始まり）
        (21, 59, "Good evening!"),  # 境界値（終わり）
        # 4. 夜 (22:00 ~ 4:59)
        (22, 0, "Good night!"),  # 境界値（始まり）
        (4, 59, "Good night!"),  # 境界値（終わり）
    ],
)
def test_get_greeting_by_time(hour, minute, expected):
    test_now = datetime.datetime(2026, 6, 2, hour, minute, 0)

    # モック
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value = test_now

        # 関数を実行
        result = get_greeting()
        assert result == expected

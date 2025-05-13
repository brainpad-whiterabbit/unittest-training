from greeting.greeting import get_greeting
import datetime
from unittest.mock import patch
import pytest

# 1. 同値分割法に基づく代表値テストケース
typical_time_test_cases = [
    pytest.param(
        datetime.datetime(2023, 10, 26, 9, 30, 0),
        "Good morning!",
        id="typical_morning_09:30",
    ),
    pytest.param(
        datetime.datetime(2023, 10, 26, 14, 15, 0),
        "Good afternoon!",
        id="typical_afternoon_14:15",
    ),
    pytest.param(
        datetime.datetime(2023, 10, 26, 19, 0, 0),
        "Good evening!",
        id="typical_evening_19:00",
    ),
    pytest.param(
        datetime.datetime(2023, 10, 26, 23, 0, 0),
        "Good night!",
        id="typical_night_23:00",
    ),
]

# 2. 境界値分析に基づくテストケース
boundary_test_cases = [
    # 夜 (Night) から 朝 (Morning) への境界
    pytest.param(
        datetime.datetime(2023, 10, 26, 4, 59, 59),
        "Good night!",
        id="boundary_04:59:59_night_before_morning",
    ),
    pytest.param(
        datetime.datetime(2023, 10, 26, 5, 0, 0),
        "Good morning!",
        id="boundary_05:00:00_morning_starts",
    ),
    # 朝 (Morning) から 昼 (Afternoon) への境界
    pytest.param(
        datetime.datetime(2023, 10, 26, 11, 59, 59),
        "Good morning!",
        id="boundary_11:59:59_morning_before_afternoon",
    ),
    pytest.param(
        datetime.datetime(2023, 10, 26, 12, 0, 0),
        "Good afternoon!",
        id="boundary_12:00:00_afternoon_starts",
    ),
    # 昼 (Afternoon) から 夕方 (Evening) への境界
    pytest.param(
        datetime.datetime(2023, 10, 26, 17, 59, 59),
        "Good afternoon!",
        id="boundary_17:59:59_afternoon_before_evening",
    ),
    pytest.param(
        datetime.datetime(2023, 10, 26, 18, 0, 0),
        "Good evening!",
        id="boundary_18:00:00_evening_starts",
    ),
    # 夕方 (Evening) から 夜 (Night) への境界
    pytest.param(
        datetime.datetime(2023, 10, 26, 21, 59, 59),
        "Good evening!",
        id="boundary_21:59:59_evening_before_night",
    ),
    pytest.param(
        datetime.datetime(2023, 10, 26, 22, 0, 0),
        "Good night!",
        id="boundary_22:00:00_night_starts",
    ),
    # 日付変更 (深夜0時) の境界 (引き続き夜であることを確認)
    pytest.param(
        datetime.datetime(2023, 10, 26, 23, 59, 59),
        "Good night!",
        id="boundary_23:59:59_night_before_midnight",
    ),
    pytest.param(
        datetime.datetime(2023, 10, 27, 0, 0, 0),
        "Good night!",
        id="boundary_00:00:00_midnight_next_day",
    ),  # 日付を翌日に
    pytest.param(
        datetime.datetime(2023, 10, 27, 0, 0, 1),
        "Good night!",
        id="boundary_00:00:01_after_midnight_next_day",
    ),  # 日付を翌日に
]


@pytest.mark.parametrize(
    "mocked_now_time, expected_greeting", typical_time_test_cases + boundary_test_cases
)
def test_get_greeting_all_cases(mocked_now_time, expected_greeting):
    """
    様々な時刻における get_greeting 関数の出力をテストします。
    同値クラスの代表値と境界値の両方を含みます。
    """
    # Arrange
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value = mocked_now_time

        # Act
        greeting = get_greeting()

        # Assert
        assert greeting == expected_greeting

from greeting.greeting import get_greeting
import datetime
from unittest.mock import patch
import pytest
from typing import NamedTuple


class GreetingTestCase(NamedTuple):
    """
    テストケースのクラス
    """

    mocked_datetime_time: datetime.time
    expected_greeting: str
    id: str


@pytest.mark.parametrize(
    GreetingTestCase._fields,
    [
        # 同値分割法に基づく代表値テストケース
        GreetingTestCase(
            mocked_datetime_time=datetime.time(9, 30, 0),
            expected_greeting="Good morning!",
            id="typical_morning_09:30",
        ),
        GreetingTestCase(
            mocked_datetime_time=datetime.time(14, 15, 0),
            expected_greeting="Good afternoon!",
            id="typical_afternoon_14:15",
        ),
        GreetingTestCase(
            mocked_datetime_time=datetime.time(19, 0, 0),
            expected_greeting="Good evening!",
            id="typical_evening_19:00",
        ),
        GreetingTestCase(
            mocked_datetime_time=datetime.time(23, 0, 0),
            expected_greeting="Good night!",
            id="typical_night_23:00",
        ),
        # 境界値分析に基づくテストケース
        GreetingTestCase(
            mocked_datetime_time=datetime.time(4, 59, 59),
            expected_greeting="Good night!",
            id="boundary_04:59:59_night_before_morning",
        ),
        GreetingTestCase(
            mocked_datetime_time=datetime.time(5, 0, 0),
            expected_greeting="Good morning!",
            id="boundary_05:00:00_morning_starts",
        ),
        GreetingTestCase(
            mocked_datetime_time=datetime.time(11, 59, 59),
            expected_greeting="Good morning!",
            id="boundary_11:59:59_morning_before_afternoon",
        ),
        GreetingTestCase(
            mocked_datetime_time=datetime.time(12, 0, 0),
            expected_greeting="Good afternoon!",
            id="boundary_12:00:00_afternoon_starts",
        ),
        GreetingTestCase(
            mocked_datetime_time=datetime.time(17, 59, 59),
            expected_greeting="Good afternoon!",
            id="boundary_17:59:59_afternoon_before_evening",
        ),
        GreetingTestCase(
            mocked_datetime_time=datetime.time(18, 0, 0),
            expected_greeting="Good evening!",
            id="boundary_18:00:00_evening_starts",
        ),
        GreetingTestCase(
            mocked_datetime_time=datetime.time(21, 59, 59),
            expected_greeting="Good evening!",
            id="boundary_21:59:59_evening_before_night",
        ),
        GreetingTestCase(
            mocked_datetime_time=datetime.time(22, 0, 0),
            expected_greeting="Good night!",
            id="boundary_22:00:00_night_starts",
        ),
        GreetingTestCase(
            mocked_datetime_time=datetime.time(23, 59, 59),
            expected_greeting="Good night!",
            id="boundary_23:59:59_night_before_midnight",
        ),
        GreetingTestCase(
            mocked_datetime_time=datetime.time(0, 0, 0),
            expected_greeting="Good night!",
            id="boundary_00:00:00_midnight_next_day",
        ),
        GreetingTestCase(
            mocked_datetime_time=datetime.time(0, 0, 1),
            expected_greeting="Good night!",
            id="boundary_00:00:01_after_midnight_next_day",
        ),
    ],
)
def test_get_greeting_all_cases(mocked_datetime_time, expected_greeting, id):
    """
    様々な時刻における get_greeting 関数の出力をテストします。
    同値クラスの代表値と境界値の両方を含みます。
    """
    # Arrange
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.time.return_value = mocked_datetime_time

        # Act
        greeting = get_greeting()

        # Assert
        assert greeting == expected_greeting

import datetime
import pytest
from freezegun import freeze_time
from greeting.greeting import get_greeting


@pytest.mark.parametrize(
    "frozen_time, expected_greeting",
    [
        # 朝: 5:00 ~ 11:59:59
        ("2026-06-01 05:00:00", "Good morning!"),
        ("2026-06-01 11:59:59", "Good morning!"),
        # 昼: 12:00 ~ 17:59:59
        ("2026-06-01 12:00:00", "Good afternoon!"),
        ("2026-06-01 17:59:59", "Good afternoon!"),
        # 夜: 18:00 ~ 21:59:59
        ("2026-06-01 18:00:00", "Good evening!"),
        ("2026-06-01 21:59:59", "Good evening!"),
        # 深夜・早朝: 22:00 ~ 4:59:59
        ("2026-06-01 22:00:00", "Good night!"),
        ("2026-06-01 04:59:59", "Good night!"),
    ],
)
def test_get_greeting_by_time(frozen_time, expected_greeting):
    # Arrange（準備）
    # @freeze_time(frozen_time) をコンテキストマネージャ（with）として使い、時間を固定します
    with freeze_time(frozen_time):
        # Act（実行）
        # この with の中で実行された datetime.now() は、すべて frozen_time の時刻になります
        result = get_greeting()

    # Assert（検証）
    assert result == expected_greeting

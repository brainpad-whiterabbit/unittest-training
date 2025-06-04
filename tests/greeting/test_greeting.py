import pytest
from greeting.greeting import get_greeting
import datetime
from freezegun import freeze_time

'''@pytest.mark.parametrize(
    "time_str, expected_greeting",
    [
        ("2025-06-04 11:59:59", "Good morning!"),  # 午前
        ("2025-06-04 12:00:00", "Good afternoon!"), # 午後
        ("2025-06-04 17:59:59", "Good afternoon!"), # 午後
        ("2025-06-04 18:00:00", "Good evening!"),   # 夜
        ("2025-06-04 21:59:59", "Good evening!"),   # 夜
        ("2025-06-04 22:00:00", "Good night!"),   # 夜
    ]
)
def test_get_greeting_at_various_times(time_str, expected_greeting):
    # freezegunを使ってdatetime.datetime.now()が指定した時刻を返すように設定
    with freeze_time(time_str):
        assert get_greeting() == expected_greeting

@pytest.mark.freeze_time('2019-11-27 11:59:59')
def test_get_greeting_morning():
        assert get_greeting() == "Good morning!"

@pytest.mark.freeze_time('2019-11-27 12:0:0')
def test_get_greeting_Good_afternoon():
        assert get_greeting() == "Good afternoon!"

@pytest.mark.freeze_time('2019-11-27 17:59:59')
def test_get_greeting_Good_afternoon2():
        assert get_greeting() == "Good afternoon!"

@pytest.mark.freeze_time('2019-11-27 18:0:0')
def test_get_greeting_Good_evening():
        assert get_greeting() == "Good evening!"

@pytest.mark.freeze_time('2019-11-27 21:59:59')
def test_get_greeting_Good_evening2():
        assert get_greeting() == "Good evening!"

@pytest.mark.freeze_time('2019-11-27 22:0:0')
def test_get_greeting_Good_night():
        assert get_greeting() == "Good night!"'''
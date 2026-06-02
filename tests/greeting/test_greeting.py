from greeting.greeting import get_greeting
import pytest
from freezegun import freeze_time


TEST_CASES = [
    # Good morning! (05:00:00 <= t < 12:00:00)
    ("2023-01-01 05:00:00", "Good morning!"),
    ("2023-01-01 08:30:00", "Good morning!"),
    ("2023-01-01 11:59:59.999999", "Good morning!"),
    
    # Good afternoon! (12:00:00 <= t < 18:00:00)
    ("2023-01-01 12:00:00", "Good afternoon!"),
    ("2023-01-01 15:00:00", "Good afternoon!"),
    ("2023-01-01 17:59:59.999999", "Good afternoon!"),
    
    # Good evening! (18:00:00 <= t < 22:00:00)
    ("2023-01-01 18:00:00", "Good evening!"),
    ("2023-01-01 20:00:00", "Good evening!"),
    ("2023-01-01 21:59:59.999999", "Good evening!"),
    
    # Good night! (22:00:00 <= t または t < 05:00:00)
    ("2023-01-01 22:00:00", "Good night!"),
    ("2023-01-01 23:00:00", "Good night!"),
    ("2023-01-01 23:59:59.999999", "Good night!"),
    ("2023-01-02 00:00:00", "Good night!"),
    ("2023-01-02 02:00:00", "Good night!"),
    ("2023-01-02 04:59:59.999999", "Good night!"),
]
@pytest.mark.parametrize("mock_time_str, expected", TEST_CASES)
def test_get_greeting_with_freezegun(mock_time_str, expected):
    # freeze_timeを使えば、インポート元を気にせず直感的に時刻を固定できます
    with freeze_time(mock_time_str):
        assert get_greeting() == expected
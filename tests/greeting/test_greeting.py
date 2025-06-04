import pytest
from unittest.mock import patch
from datetime import datetime
from greeting.greeting import get_greeting

@pytest.mark.parametrize(
    "mock_time, expected_output",
    [
        (datetime(2025, 1, 1, 5, 0, 0), "Good morning!"),
        (datetime(2025, 1, 1, 12, 0, 0), "Good afternoon!"),
        (datetime(2025, 1, 1, 18, 0, 0), "Good evening!"),
        (datetime(2025, 1, 1, 22, 0, 0), "Good night!"),
        (datetime(2025, 1, 1, 22, 0, 1), "Good night!"),
        (datetime(2025, 1, 1, 4, 59, 59), "Good night!"),
    ]
)
def test_greeting_normal(mock_time, expected_output):
    with patch('greeting.greeting.datetime.datetime') as mock_datetime:
        mock_datetime.now.return_value = mock_time
        assert get_greeting() == expected_output


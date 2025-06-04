from greeting.greeting import get_greeting
from datetime import datetime
from unittest.mock import patch
import pytest


@pytest.mark.parametrize(
    "mock_hour, expected",
    [
        (5, "Good morning!"),
        (11, "Good morning!"),
        (12, "Good afternoon!"),
        (17, "Good afternoon!"),
        (18, "Good evening!"),
        (21, "Good evening!"),
        (22, "Good night!"),
        (4, "Good night!"),
        (0, "Good night!"),
        (23, "Good night!"),
    ],
)
def test_get_greeting_by_hour(mock_hour, expected):
    mock_datetime = datetime(2024, 1, 1, mock_hour, 0, 0)
    with patch("greeting.greeting.datetime") as mocked_datetime:
        mocked_datetime.datetime.now.return_value = mock_datetime
        assert get_greeting() == expected

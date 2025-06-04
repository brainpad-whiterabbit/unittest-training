from greeting.greeting import get_greeting
import datetime
from unittest.mock import patch
import pytest


def test_get_greeting_morning():
    with patch("greeting.greeting.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value = datetime.datetime(2024, 1, 1, 7, 0)
        expected = "Good morning!"
        assert get_greeting() == expected

def test_get_greeting_afternoon():
    with patch("greeting.greeting.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value = datetime.datetime(2024, 1, 1, 15, 0)
        expected = "Good afternoon!"
        assert get_greeting() == expected

def test_get_greeting_evening():
    with patch("greeting.greeting.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value = datetime.datetime(2024, 1, 1, 20, 0)
        expected = "Good evening!"
        assert get_greeting() == expected

def test_get_greeting_night():
    with patch("greeting.greeting.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value = datetime.datetime(2024, 1, 1, 23, 0)
        expected = "Good night!"
        assert get_greeting() == expected

def test_get_greeting_night_midnight():
    with patch("greeting.greeting.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value = datetime.datetime(2024, 1, 2, 3, 0)
        expected = "Good night!"
        assert get_greeting() == expected


def test_get_greeting_irreg():
    with pytest.raises(ValueError):
        with patch("greeting.greeting.datetime") as mock_datetime:
            mock_datetime.datetime.now.return_value = datetime.datetime(2024, 1, 2, 24, 59)
            get_greeting()


def test_get_greeting_edge_at5am():
    with patch("greeting.greeting.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value = datetime.datetime(2024, 1, 1, 5, 0)
        expected = "Good morning!"
        assert get_greeting() == expected


def test_get_greeting_edge_at12pm():
    with patch("greeting.greeting.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value = datetime.datetime(2024, 1, 1, 12, 0)
        expected = "Good afternoon!"
        assert get_greeting() == expected

def test_get_greeting_edge_at18():
    with patch("greeting.greeting.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value = datetime.datetime(2024, 1, 1, 18, 0)
        expected = "Good evening!"
        assert get_greeting() == expected

def test_get_greeting_edge_at22():
    with patch("greeting.greeting.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value = datetime.datetime(2024, 1, 1, 22, 0)
        expected = "Good night!"
        assert get_greeting() == expected

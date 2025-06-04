from greeting.greeting import get_greeting
import datetime
from unittest.mock import patch


def test_get_greeting_morning():
    # Arrange
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.time.return_value = datetime.time(9, 30, 0)
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good morning!"


def test_get_greeting_afternoon():
    # Arrange
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.time.return_value = datetime.time(14, 15, 0)
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good afternoon!"


def test_get_greeting_evening():
    # Arrange
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.time.return_value = datetime.time(19, 0, 0)
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good evening!"


def test_get_greeting_night():
    # Arrange
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.time.return_value = datetime.time(23, 0, 0)
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good night!"


def test_get_greeting_boundary_before_morning_starts():
    # Arrange
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.time.return_value = datetime.time(4, 59, 59)
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good night!"


def test_get_greeting_boundary_at_morning_starts():
    # Arrange
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.time.return_value = datetime.time(5, 0, 0)
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good morning!"


def test_get_greeting_boundary_before_afternoon_starts():
    # Arrange
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.time.return_value = datetime.time(11, 59, 59)
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good morning!"


def test_get_greeting_boundary_at_afternoon_starts():
    # Arrange
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.time.return_value = datetime.time(12, 0, 0)
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good afternoon!"


def test_get_greeting_boundary_before_evening_starts():
    # Arrange
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.time.return_value = datetime.time(17, 59, 59)
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good afternoon!"


def test_get_greeting_boundary_at_evening_starts():
    # Arrange
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.time.return_value = datetime.time(18, 0, 0)
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good evening!"


# 夕方 (Evening) から 夜 (Night) への境界テスト
def test_get_greeting_boundary_before_night_starts():
    # Arrange
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.time.return_value = datetime.time(21, 59, 59)
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good evening!"


def test_get_greeting_boundary_at_night_starts():
    # Arrange
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.time.return_value = datetime.time(22, 0, 0)
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good night!"


def test_get_greeting_boundary_just_before_midnight():
    # Arrange
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.time.return_value = datetime.time(23, 59, 59)
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good night!"


def test_get_greeting_boundary_at_midnight():
    # Arrange
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.time.return_value = datetime.time(0, 0, 0)
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good night!"


def test_get_greeting_boundary_just_after_midnight():
    # Arrange
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.time.return_value = datetime.time(0, 0, 1)
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good night!"

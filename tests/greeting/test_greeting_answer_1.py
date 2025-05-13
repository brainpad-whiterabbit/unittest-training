from greeting.greeting import get_greeting
import datetime
from unittest.mock import patch


def test_get_greeting_morning():
    # Arrange
    mocked_now_time = datetime.datetime(2023, 10, 26, 9, 30, 0)
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value = mocked_now_time
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good morning!"


def test_get_greeting_afternoon():
    # Arrange
    mocked_now_time = datetime.datetime(2023, 10, 26, 14, 15, 0)
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value = mocked_now_time
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good afternoon!"


def test_get_greeting_evening():
    # Arrange
    mocked_now_time = datetime.datetime(2023, 10, 26, 19, 0, 0)
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value = mocked_now_time
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good evening!"


def test_get_greeting_night():
    # Arrange
    mocked_now_time = datetime.datetime(2023, 10, 26, 23, 0, 0)
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value = mocked_now_time
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good night!"


def test_get_greeting_boundary_before_morning_starts():
    # Arrange
    mocked_now_time = datetime.datetime(2023, 10, 26, 4, 59, 59)
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value = mocked_now_time
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good night!"


def test_get_greeting_boundary_at_morning_starts():
    # Arrange
    mocked_now_time = datetime.datetime(2023, 10, 26, 5, 0, 0)
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value = mocked_now_time
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good morning!"


def test_get_greeting_boundary_before_afternoon_starts():
    # Arrange
    mocked_now_time = datetime.datetime(2023, 10, 26, 11, 59, 59)
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value = mocked_now_time
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good morning!"


def test_get_greeting_boundary_at_afternoon_starts():
    # Arrange
    mocked_now_time = datetime.datetime(2023, 10, 26, 12, 0, 0)
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value = mocked_now_time
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good afternoon!"


def test_get_greeting_boundary_before_evening_starts():
    # Arrange
    mocked_now_time = datetime.datetime(2023, 10, 26, 17, 59, 59)
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value = mocked_now_time
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good afternoon!"


def test_get_greeting_boundary_at_evening_starts():
    # Arrange
    mocked_now_time = datetime.datetime(2023, 10, 26, 18, 0, 0)
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value = mocked_now_time
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good evening!"


# 夕方 (Evening) から 夜 (Night) への境界テスト
def test_get_greeting_boundary_before_night_starts():
    # Arrange
    mocked_now_time = datetime.datetime(2023, 10, 26, 21, 59, 59)
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value = mocked_now_time
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good evening!"


def test_get_greeting_boundary_at_night_starts():
    # Arrange
    mocked_now_time = datetime.datetime(2023, 10, 26, 22, 0, 0)
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value = mocked_now_time
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good night!"


def test_get_greeting_boundary_just_before_midnight():
    # Arrange
    mocked_now_time = datetime.datetime(2023, 10, 26, 23, 59, 59)
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value = mocked_now_time
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good night!"


def test_get_greeting_boundary_at_midnight():
    # Arrange
    mocked_now_time = datetime.datetime(2023, 10, 27, 0, 0, 0)
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value = mocked_now_time
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good night!"


def test_get_greeting_boundary_just_after_midnight():
    # Arrange
    mocked_now_time = datetime.datetime(2023, 10, 27, 0, 0, 1)
    with patch("greeting.greeting.datetime") as mock_datetime_module:
        mock_datetime_module.datetime.now.return_value = mocked_now_time
        # Act
        greeting = get_greeting()
        # Assert
        assert greeting == "Good night!"

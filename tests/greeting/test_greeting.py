from greeting.greeting import get_greeting
import pytest
from unittest.mock import patch, Mock

# def test_get_greeting_morning():
#     with patch('datetime.datetime') as mock_datetime:
#         mock_datetime.now.return_value = Mock(hour=7)
#         assert get_greeting() == "Good morning!"


@pytest.mark.parametrize(
    "mock_hour, expected_greeting",
    [
        (7, "Good morning!"),
        (5, "Good morning!"),
        (11, "Good morning!"),

        (14, "Good afternoon!"), 
        (12, "Good afternoon!"), 
        (17, "Good afternoon!"),

        (19, "Good evening!"),   
        (18, "Good evening!"),  
        (21, "Good evening!"),   

        (3, "Good night!"),     
        (23, "Good night!"),    
        (0, "Good night!"),     
        (4, "Good night!"),     
        (22, "Good night!"), 
    ]
)
@patch('greeting.greeting.datetime.datetime')

def test_get_greeting_parametrized(mock_datetime, mock_hour, expected_greeting):
    mock_datetime.now.return_value = Mock(hour=mock_hour)
    assert get_greeting() == expected_greeting
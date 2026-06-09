import pytest

from fizzbuzz.fizzbuzz import fizzbuzz


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (2, "2"),
        (3, "Fizz"),
        (5, "Buzz"),
        (15, "FizzBuzz"),
        (30, "FizzBuzz"),
        (45, "FizzBuzz"),
        (7, "7"),
        (98, "98"),
        (1, "1"),
        (999, "Fizz"),
        (1000, "Buzz"),
    ],
)
def test_fizzbuzz_returns_expected_value(input_value, expected_output):
    assert fizzbuzz(input_value) == expected_output


@pytest.mark.parametrize(
    "input_value, exception, message",
    [
        (0, ValueError, "n must be between 1 and 1000."),
        (-1, ValueError, "n must be between 1 and 1000."),
        (1001, ValueError, "n must be between 1 and 1000."),
        ("a", TypeError, "n must be an integer."),
        (3.0, TypeError, "n must be an integer."),
        (None, TypeError, "n must be an integer."),
    ],
)
def test_fizzbuzz_raises_for_invalid_input(input_value, exception, message):
    with pytest.raises(exception, match=message):
        fizzbuzz(input_value)

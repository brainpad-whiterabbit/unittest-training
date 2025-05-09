import pytest
from level1.fizzbuzz import fizzbuzz


def test_fizzbuzz_fizz():
    # Arrange
    input_value = 3
    expected_output = "Fizz"
    # Act
    result = fizzbuzz(input_value)
    # Assert
    assert result == expected_output


def test_fizzbuzz_buzz():
    # Arrange
    input_value = 5
    expected_output = "Buzz"
    # Act
    result = fizzbuzz(input_value)
    # Assert
    assert result == expected_output


def test_fizzbuzz_fizzbuzz():
    # Arrange
    input_value = 15
    expected_output = "FizzBuzz"
    # Act
    result = fizzbuzz(input_value)
    # Assert
    assert result == expected_output


def test_fizzbuzz_number():
    # Arrange
    input_value = 7
    expected_output = "7"
    # Act
    result = fizzbuzz(input_value)
    # Assert
    assert result == expected_output


def test_fizzbuzz_min_value():
    # Arrange
    input_value = 1
    expected_output = "1"
    # Act
    result = fizzbuzz(input_value)
    # Assert
    assert result == expected_output


def test_fizzbuzz_min_value_plus_one():
    # Arrange
    input_value = 2
    expected_output = "2"
    # Act
    result = fizzbuzz(input_value)
    # Assert
    assert result == expected_output


def test_fizzbuzz_max_value():
    # Arrange
    input_value = 1000
    expected_output = "Buzz"
    # Act
    result = fizzbuzz(input_value)
    # Assert
    assert result == expected_output


def test_fizzbuzz_fizz_max_value_minus_1():
    # Arrange
    input_value = 999
    expected_output = "Fizz"
    # Act
    result = fizzbuzz(input_value)
    # Assert
    assert result == expected_output


def test_fizzbuzz_zero_raises_valueerror():
    # Arrange
    input_value = 0
    # Act & Assert
    with pytest.raises(ValueError) as e:
        fizzbuzz(input_value)
    assert str(e.value) == "n must be between 1 and 1000."


def test_fizzbuzz_over_max_raises_valueerror():
    # Arrange
    input_value = 1001
    # Act & Assert
    with pytest.raises(ValueError) as e:
        fizzbuzz(input_value)
    assert str(e.value) == "n must be between 1 and 1000."


def test_fizzbuzz_typeerror():
    # Arrange
    input_value = "a"
    # Act & Assert
    with pytest.raises(TypeError) as e:
        fizzbuzz(input_value)
    assert str(e.value) == "n must be an integer."

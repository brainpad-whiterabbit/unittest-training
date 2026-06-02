from fizzbuzz.fizzbuzz import fizzbuzz
import pytest


def test_fizzbuzz_example():
    # Arrange
    input_value = 9
    expected_output = "Fizz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


def test_fizzbuzz_example2():
    # Arrange
    input_value = 10
    expected_output = "Buzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


def test_fizzbuzz_example3():
    # Arrange
    input_value = 45
    expected_output = "FizzBuzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


def test_fizzbuzz_example4():
    # Arrange
    input_value = 16
    expected_output = str(16)

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


def test_fizzbuzz_example5():
    # Arrange
    input_value = 0
    expected_output = "n must be between 1 and 1000."

    # Act
    with pytest.raises(ValueError) as excinfo:
        fizzbuzz(input_value)

    # Assert
    assert str(excinfo.value) == expected_output


def test_fizzbuzz_example6():
    # Arrange
    input_value = 1001
    expected_output = "n must be between 1 and 1000."

    # Act
    with pytest.raises(ValueError) as excinfo:
        fizzbuzz(input_value)

    # Assert
    assert str(excinfo.value) == expected_output


def test_fizzbuzz_example7():
    # Arrange
    input_value = "abc"
    expected_output = "n must be an integer."

    # Act
    with pytest.raises(TypeError) as excinfo:
        fizzbuzz(input_value)

    # Assert
    assert str(excinfo.value) == expected_output


def test_fizzbuzz_example8():
    # Arrange
    input_value = 1.5
    expected_output = "n must be an integer."

    # Act
    with pytest.raises(TypeError) as excinfo:
        fizzbuzz(input_value)

    # Assert
    assert str(excinfo.value) == expected_output


def test_fizzbuzz_example9():
    # Arrange
    input_value = 1.5
    expected_output = "n must be an integer."

    # Act
    with pytest.raises(TypeError) as excinfo:
        fizzbuzz(input_value)

    # Assert
    assert str(excinfo.value) == expected_output

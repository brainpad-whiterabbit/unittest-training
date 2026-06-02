from fizzbuzz.fizzbuzz import fizzbuzz
import pytest

def test_fizzbuzz_1():
    # Arrange
    input_value = 1
    expected_output = "1"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output

def test_fizzbuzz_example():
    # Arrange
    input_value = 3
    expected_output = "Fizz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output

def test_fizzbuzz_5():
    # Arrange
    input_value = 5
    expected_output = "Buzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output

def test_fizzbuzz_15():
    # Arrange
    input_value = 15
    expected_output = "FizzBuzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output

def test_fizzbuzz_7():
    # Arrange
    input_value = 7
    expected_output = '7'

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output

def test_fizzbuzz_0():
    # Arrange
    input_value = 0

    # Act + Assert
    with pytest.raises(ValueError):
        fizzbuzz(input_value)

def test_fizzbuzz_1000():
    # Arrange
    input_value = 1000
    expected_output = "Buzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output

def test_fizzbuzz_1001():
    # Arrange
    input_value = 1001

    # Act + Assert
    with pytest.raises(ValueError):
        fizzbuzz(input_value)

def test_fizzbuzz_05():
    # Arrange
    input_value = 0.5

    # Act + Assert
    with pytest.raises(TypeError):
        fizzbuzz(input_value)

def test_fizzbuzz_a():
    # Arrange
    input_value = 'a'

    # Act + Assert
    with pytest.raises(TypeError):
        fizzbuzz(input_value)

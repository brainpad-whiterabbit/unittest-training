from fizzbuzz.fizzbuzz import fizzbuzz
import pytest


def test_fizzbuzz_example():
    # Arrange
    input_value = 3
    expected_output = "Fizz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


def test_fizzbuzz_multiple_5():
    input_value = 5
    expected_output = "Buzz"

    result = fizzbuzz(input_value)

    assert result == expected_output


def test_fizzbuzz_multiple_15():
    input_value = 15
    expected_output = "FizzBuzz"

    result = fizzbuzz(input_value)

    assert result == expected_output

def test_fizzbuzz_multiple_1():
    input_value = 1
    expected_output = "1"

    result = fizzbuzz(input_value)

    assert result == expected_output

def test_fizzbuzz_answer_type():
    input_value = 15

    result = fizzbuzz(input_value)

    assert type(result) is str

def test_fizzbuzz_0():
    input_value = 0
    with pytest.raises(ValueError, match="n must be between 1 and 1000."):
        fizzbuzz(input_value)

def test_fizzbuzz_1001():
    input_value = 1001
    with pytest.raises(ValueError, match="n must be between 1 and 1000."):
        fizzbuzz(input_value)

def test_fizzbuzz_less_than_0():
    input_value = -100
    with pytest.raises(ValueError, match="n must be between 1 and 1000."):
        fizzbuzz(input_value)


def test_fizzbuzz_more_than_1000():
    input_value = 10000
    with pytest.raises(ValueError, match="n must be between 1 and 1000."):
        fizzbuzz(input_value)


def test_fizzbuzz_diferent_type():
    input_value = 0.01
    with pytest.raises(TypeError, match="n must be an integer."):
        fizzbuzz(input_value)
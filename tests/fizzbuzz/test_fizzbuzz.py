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

def test_fizzbuzz_normal_1():
    input_value = 5
    expected_output = "Buzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output

def test_fizzbuzz_normal_2():
    input_value = 15
    expected_output = "FizzBuzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output

def test_fizzbuzz_normal_3():
    input_value = 1
    expected_output = "1"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output

def test_fizzbuzz_normal_4():
    input_value = 1000
    expected_output = "Buzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output

def test_fizzbuzz_edge_1():
    input_value = 0
    with pytest.raises(ValueError):
        fizzbuzz(input_value)

def test_fizzbuzz_edge_2():
    input_value = 1001
    with pytest.raises(ValueError):
        fizzbuzz(input_value)

def test_fizzbuzz_edge_3():
    input_value = "hoge"
    with pytest.raises(TypeError):
        fizzbuzz(input_value)
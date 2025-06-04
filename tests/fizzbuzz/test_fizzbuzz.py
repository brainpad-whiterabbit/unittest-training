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

def test_fizzbuzz_5():
    input_value = 5
    expected_output = "Buzz"

    result = fizzbuzz(input_value)
    assert result == expected_output

def test_fizzbuzz_15():
    input_value = 15
    expected_output = "FizzBuzz"

    result = fizzbuzz(input_value)
    assert result == expected_output

def test_fizzbuzz_1000():
    input_value = 1000
    expected_output = "Buzz"

    result = fizzbuzz(input_value)
    assert result == expected_output

def test_fizzbuzz_1():
    input_value = 1
    expected_output = "1"

    result = fizzbuzz(input_value)
    assert result == expected_output

def test_fizzbuzz_ValueError_0():
    input_value = 0
    with pytest.raises(ValueError):
        fizzbuzz(input_value)
    
def test_fizzbuzz_ValueError_1001():
    input_value = 1001
    with pytest.raises(ValueError):
        fizzbuzz(input_value)

def test_fizzbuzz_TypeError_a():
    input_value = 'a'
    with pytest.raises(TypeError):
        fizzbuzz(input_value)


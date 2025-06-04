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

def test_fizzbuzz_edge_1():
    input_value = 0
    with pytest.raises(ValueError) as e:
        fizzbuzz(input_value)
        
    # assert str(e.value) == "不正な値です"

def test_fizzbuzz_normal_1():
    input_value = 5
    expected_output = "Buzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output



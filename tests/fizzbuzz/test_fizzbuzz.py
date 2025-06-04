from fizzbuzz.fizzbuzz import fizzbuzz


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
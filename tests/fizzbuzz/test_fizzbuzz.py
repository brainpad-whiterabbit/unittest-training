from fizzbuzz.fizzbuzz import fizzbuzz


def test_fizzbuzz_expected_value():
    # Arrange
    cases = [
        (1, "1"),  # plain number, lower boundary of valid range
        (3, "Fizz"),  # divisible by 3 only
        (5, "Buzz"),  # divisible by 5 only
        (15, "FizzBuzz"),  # divisible by both 3 and 5
        (1000, "Buzz"),  # upper boundary of valid range, divisible by 5
    ]

    # Act and Assert
    for input_value, expected_output in cases:
        assert fizzbuzz(input_value) == expected_output


def test_fizzbuzz_value_error():
    # Arrange
    invalid_values = [0, 1001]

    # Act and Assert
    for invalid_value in invalid_values:
        try:
            fizzbuzz(invalid_value)
            assert False, f"Expected ValueError for {invalid_value}"
        except ValueError as exc:
            assert str(exc) == "n must be between 1 and 1000."


def test_fizzbuzz_type_error():
    # Arrange
    invalid_values = ["a", 2.5]

    # Act and Assert
    for invalid_value in invalid_values:
        try:
            fizzbuzz(invalid_value)
            assert False, f"Expected TypeError for {invalid_value!r}"
        except TypeError as exc:
            assert str(exc) == "n must be an integer."

import pytest
from fizzbuzz.fizzbuzz import fizzbuzz


# ==========================================
# 1. 正常系のテスト（期待した文字列が返るケース）
# ==========================================
@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (9, "Fizz"),  # example1
        (10, "Buzz"),  # example2
        (45, "FizzBuzz"),  # example3
        (16, str(16)),  # example4
    ],
)
def test_fizzbuzz_normal_cases(input_value, expected_output):
    # Arrange & Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


# ==========================================
# 2. 異常系のテスト（エラーが発生するケース）
# ==========================================
@pytest.mark.parametrize(
    "input_value, expected_exception, expected_output",
    [
        (0, ValueError, "n must be between 1 and 1000."),  # example5
        (1001, ValueError, "n must be between 1 and 1000."),  # example6
        ("abc", TypeError, "n must be an integer."),  # example7
        (1.5, TypeError, "n must be an integer."),  # example8, 9
    ],
)
def test_fizzbuzz_exception_cases(input_value, expected_exception, expected_output):
    # Arrange & Act
    with pytest.raises(expected_exception) as excinfo:
        fizzbuzz(input_value)

    # Assert
    assert str(excinfo.value) == expected_output

import pytest
from fizzbuzz.fizzbuzz import fizzbuzz


# 正常系テストをパラメータ化
@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (3, "Fizz"),
        (5, "Buzz"),
        (15, "FizzBuzz"),
        (7, "7"),
        (1, "1"),
        (2, "2"),
        (1000, "Buzz"),
        (999, "Fizz"),
    ],
)
def test_fizzbuzz_normal(input_value, expected_output):
    assert fizzbuzz(input_value) == expected_output


# ValueErrorをパラメータ化
@pytest.mark.parametrize("input_value", [0, 1001])
def test_fizzbuzz_valueerror(input_value):
    with pytest.raises(ValueError) as e:
        fizzbuzz(input_value)
    assert str(e.value) == "n must be between 1 and 1000."


# TypeErrorをパラメータ化
@pytest.mark.parametrize(
    "input_value",
    [
        "a",
        3.14,
        [],
        {},
    ],
)
def test_fizzbuzz_typeerror(input_value):
    with pytest.raises(TypeError) as e:
        fizzbuzz(input_value)
    assert str(e.value) == "n must be an integer."

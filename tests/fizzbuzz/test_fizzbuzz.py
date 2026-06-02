from fizzbuzz.fizzbuzz import fizzbuzz
import pytest


# 3の倍数に対するテスト
def test_fizzbuzz_example():
    # Arrange
    input_value = 3
    expected_output = "Fizz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


# 5の倍数に対するテスト
def test_fizzbuzz_5multiple():
    # Arrange
    input_value = 5
    expected_output = "Buzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


# 3の倍数でも5の倍数ではない場合のテスト
def test_fizzbuzz_notmultiple():
    # Arrange
    input_value = 1
    expected_output = str(input_value)

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


# 15の倍数に対するテスト
def test_fizzbuzz_15multiple():
    # Arrange
    input_value = 15
    expected_output = "FizzBuzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


# 範囲外に対するテスト
def test_fizzbuzz_outrange():
    with pytest.raises(ValueError):
        fizzbuzz(1001)


# 小数を入力したことに対するテスト
def test_fizzbuzz_typeerror():
    with pytest.raises(TypeError):
        fizzbuzz(111.1)


# 数値以外を入力したことに対するテスト
def test_fizzbuzz_typeerror2():
    with pytest.raises(TypeError):
        fizzbuzz("aiueo")

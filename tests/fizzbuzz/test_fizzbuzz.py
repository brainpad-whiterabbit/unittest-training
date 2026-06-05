from fizzbuzz.fizzbuzz import fizzbuzz
import pytest

"""
outputの検証
"""


# 3の倍数
def test_fizzbuzz_mult3():
    # Arrange
    input_value = 3
    expected_output = "Fizz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


# 5の倍数
def test_fizzbuzz_mult5():
    # Arrange
    input_value = 5
    expected_output = "Buzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


# 3と5の倍数
def test_fizzbuzz_mult3and5():
    # Arrange
    input_value = 15
    expected_output = "FizzBuzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


# 3と5どちらの倍数でもない
def test_fizzbuzz_no_mult():
    # Arrange
    input_value = 2
    expected_output = "2"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


# 値が境界値（低）
def test_fizzbuzz_1():
    # Arrange
    input_value = 1
    expected_output = "1"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


# 値が境界値（低）
def test_fizzbuzz_1000():
    # Arrange
    input_value = 1000
    expected_output = "Buzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


"""
エラー
"""


# paramがstring
def test_fizzbuzz_typeError_string():
    # Arrange
    input_value = "aaa"

    with pytest.raises(TypeError):
        fizzbuzz(input_value)


# paramがfloat
def test_fizzbuzz_typeError_float():
    # Arrange
    input_value = 1.5

    with pytest.raises(TypeError):
        fizzbuzz(input_value)


# paramがbool
# このテストだけFailした (boolが0/1で判定されているのが問題？)
def test_fizzbuzz_typeError_bool():
    with pytest.raises(TypeError):
        fizzbuzz(True)


# paramが範囲外（値が低すぎる）
def test_fizzbuzz_out_of_range_low():
    # Arrange
    input_value = 0

    with pytest.raises(ValueError):
        fizzbuzz(input_value)


# paramが範囲外（値が高すぎる）
def test_fizzbuzz_out_of_range_high():
    # Arrange
    input_value = 1001

    with pytest.raises(ValueError):
        fizzbuzz(input_value)

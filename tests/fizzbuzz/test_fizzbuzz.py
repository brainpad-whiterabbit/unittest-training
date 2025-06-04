from fizzbuzz.fizzbuzz import fizzbuzz
import pytest


# 3の倍数かつ5の倍数のときFizzBuzzを出力するか?
def test_fizzbuzz_fizzbuzz():
    # Arrange
    input_value = 30
    expected_output = "FizzBuzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


# 3の倍数のときFizzが出るか?
def test_fizzbuzz_fizz():
    result = fizzbuzz(6)
    expected = "Fizz"
    assert result == expected


# 5の倍数のときBuzzが出るか?
def test_fizzbuzz_buzz():
    result = fizzbuzz(10)
    expected = "Buzz"
    assert result == expected


# 3の倍数でも5の倍数でもないとき数字が出るか?
def test_fizzbuzz_num():
    result = fizzbuzz(4)
    expected = "4"
    assert result == expected


# 上限のとき正常終了するか?
def test_fizzbuzz_valueerr_highlimit():
    result = fizzbuzz(1000)
    expected = "Buzz"
    assert result == expected


# 下限のとき正常終了するか?
def test_fizzbuzz_valueerr_lowlimit():
    result = fizzbuzz(1)
    expected = "1"
    assert result == expected


# 1より小さいときにValueErrorが出るか?
def test_fizzbuzz_valueerr_ltlimit():
    with pytest.raises(ValueError):
        fizzbuzz(0)


# 1000より大きいときにValueErrorが出るか?
def test_fizzbuzz_valueerr_gtlimit():
    with pytest.raises(ValueError):
        fizzbuzz(1001)


# Floatを入力した際にTypeErrorが出るか?
def test_fizzbuzz_typeerr_float():
    with pytest.raises(TypeError):
        fizzbuzz(1.0)


# Stringを入力した際にTypeErrorが出るか?
def test_fizzbuzz_typeerr_string():
    with pytest.raises(TypeError):
        fizzbuzz("A")

from fizzbuzz.fizzbuzz import fizzbuzz
import pytest


def test_fizzbuzz_3():
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

def test_fizzbuzz_999():
    input_value = 999
    expected_output = "Fizz"

    result = fizzbuzz(input_value)

    assert result == expected_output

def test_fizzbuzz_1000():
    input_value = 1000
    expected_output = "Buzz"

    result = fizzbuzz(input_value)

    assert result == expected_output

def test_fizzbuzz_15():
    input_value = 15
    expected_output = "FizzBuzz"

    result = fizzbuzz(input_value)

    assert result == expected_output

def test_fizzbuzz_1():
    input_value = 1
    expected_output = "1"

    result = fizzbuzz(input_value)

    assert result == expected_output

def test_fizzbuzz_str_error():
    input_value = "test"
    with pytest.raises(TypeError) as e:
        fizzbuzz(input_value)
        
    # エラーメッセージを検証
    assert str(e.value) == "n must be an integer."

def test_fizzbuzz_0():
    input_value = 0
    with pytest.raises(ValueError) as e:
        fizzbuzz(input_value)
        
    # エラーメッセージを検証
    assert str(e.value) == "n must be between 1 and 1000."

def test_fizzbuzz_m():
    input_value = -1
    with pytest.raises(ValueError) as e:
        fizzbuzz(input_value)
        
    # エラーメッセージを検証
    assert str(e.value) == "n must be between 1 and 1000."

def test_fizzbuzz_1001():
    input_value = 1001
    with pytest.raises(ValueError) as e:
        fizzbuzz(input_value)
        
    # エラーメッセージを検証
    assert str(e.value) == "n must be between 1 and 1000."

def test_fizzbuzz_true():
    input_value = True
    with pytest.raises(TypeError) as e:
        fizzbuzz(input_value)
        
    # エラーメッセージを検証
    assert str(e.value) == "n must be an integer."

def test_fizzbuzz_null():
    input_value = ""
    with pytest.raises(TypeError) as e:
        fizzbuzz(input_value)
        
    # エラーメッセージを検証
    assert str(e.value) == "n must be an integer."

def test_fizzbuzz_float_error():
    input_value = 1.5
    with pytest.raises(TypeError) as e:
        fizzbuzz(input_value)
        
    # エラーメッセージを検証
    assert str(e.value) == "n must be an integer."
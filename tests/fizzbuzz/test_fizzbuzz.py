import pytest  # 例外テストを行うために必要です
from fizzbuzz.fizzbuzz import fizzbuzz


def test_fizzbuzz_example():
    # Arrange（準備）
    input_value = 3
    expected_output = "Fizz"

    # Act（実行）
    result = fizzbuzz(input_value)

    # Assert（検証）
    assert result == expected_output


# === ここから新しく追加するテストケース ===

def test_fizzbuzz_normal_cases():
    """正常系のテスト: さまざまな入力値に対する戻り値を検証します"""
    # 5の倍数の場合
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(1000) == "Buzz"

    # 3と5の公倍数の場合
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"

    # それ以外の数字の場合（文字列としてそのまま返ってくるか）
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(7) == "7"
    assert fizzbuzz(998) == "998"


def test_fizzbuzz_value_error_low():
    """異常系のテスト: 1未満の数が入力された場合に ValueError が発生するか検証します"""
    # Arrange（準備）: 境界値である 0 を設定
    invalid_input = 0

    # Act & Assert（実行と検証）: pytest.raises を使って例外を検出
    with pytest.raises(ValueError) as excinfo:
        fizzbuzz(invalid_input)

    # エラーメッセージの内容が正しいかも検証
    assert str(excinfo.value) == "n must be between 1 and 1000."


def test_fizzbuzz_value_error_high():
    """異常系のテスト: 1000を超える数が入力された場合に ValueError が発生するか検証します"""
    # Arrange（準備）: 境界値である 1001 を設定
    invalid_input = 1001

    # Act & Assert（実行と検証）
    with pytest.raises(ValueError) as excinfo:
        fizzbuzz(invalid_input)

    assert str(excinfo.value) == "n must be between 1 and 1000."


def test_fizzbuzz_type_error_string():
    """異常系のテスト: 整数以外の型（文字列）が入力された場合に TypeError が発生するか検証します"""
    # Arrange（準備）
    invalid_input = "a"

    # Act & Assert（実行と検証）
    with pytest.raises(TypeError) as excinfo:
        fizzbuzz(invalid_input)

    assert str(excinfo.value) == "n must be an integer."


def test_fizzbuzz_type_error_float():
    """異常系のテスト: 整数以外の型（浮動小数点数）が入力された場合に TypeError が発生するか検証します"""
    # Arrange（準備）
    invalid_input = 3.14

    # Act & Assert（実行と検証）
    with pytest.raises(TypeError) as excinfo:
        fizzbuzz(invalid_input)

    assert str(excinfo.value) == "n must be an integer."

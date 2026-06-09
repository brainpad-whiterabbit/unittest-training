import pytest
from fizzbuzz.fizzbuzz import fizzbuzz

# --- 正常系のテスト ---

def test_fizzbuzz_3の倍数のときはFizzを返す():
    # 3の倍数を入れたら "Fizz" になるか
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"

def test_fizzbuzz_5の倍数のときはBuzzを返す():
    # 5の倍数を入れたら "Buzz" になるか
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"

def test_fizzbuzz_15の倍数のときはFizzBuzzを返す():
    # 15の倍数を入れたら "FizzBuzz" になるか
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"

def test_fizzbuzz_それ以外の数値はそのまま文字列で返す():
    # 境界値の 1 や、その他の数値をテスト
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(7) == "7"

def test_fizzbuzz_上限値の1000のとき():
    # 1000は5の倍数なので "Buzz" になるはず
    assert fizzbuzz(1000) == "Buzz"


# --- 異常系のテスト（エラーが出るか） ---

def test_fizzbuzz_範囲外の数値はValueErrorになる():
    # 1. まずエラーが起きる検証を try の中に書く
    try:
        fizzbuzz(0)
        # もしエラーが発生せずにここを通過しちゃったら、テスト失敗にする
        assert False, "ValueErrorが発生しませんでした"
    except ValueError:
        # 2. 狙い通り ValueError が発生したら、ここに来るのでテスト成功（何もしない）
        pass

# --- pytestを使ったパターン ---

def test_fizzbuzz_整数以外はTypeErrorになる():
    # 文字列や小数を入れたときに TypeError が出るかチェック
    with pytest.raises(TypeError):
        fizzbuzz("3")
    with pytest.raises(TypeError):
        fizzbuzz(3.14)
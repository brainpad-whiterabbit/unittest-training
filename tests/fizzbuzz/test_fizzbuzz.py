import pytest
from fizzbuzz.fizzbuzz import fizzbuzz


# 1. 正常系のテスト
@pytest.mark.parametrize(
    "n, expected",
    [
        (3, "Fizz"),  # 3の倍数
        (5, "Buzz"),  # 5の倍数
        (15, "FizzBuzz"),  # 15の倍数
        (7, "7"),  # それ以外
        (1, "1"),  # 境界値（最小）
        (1000, "Buzz"),  # 境界値（最大）
    ],
)
def test_fizzbuzz_valid(n, expected):
    assert fizzbuzz(n) == expected


# 2. 異常系のテスト
@pytest.mark.parametrize(
    "n, exception_type, match_msg",
    [
        (0, ValueError, "n must be between 1 and 1000."),  # 範囲外（小）
        (1001, ValueError, "n must be between 1 and 1000."),  # 範囲外（大）
        ("a", TypeError, "n must be an integer."),  # 型エラー（文字列）
        (3.5, TypeError, "n must be an integer."),  # 型エラー（小数）
    ],
)
def test_fizzbuzz_invalid(n, exception_type, match_msg):
    with pytest.raises(exception_type, match=match_msg):
        fizzbuzz(n)

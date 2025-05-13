def fizzbuzz(n: int) -> str:
    """概要
    FizzBuzz関数: 整数nを引数に取り、3の倍数のときは"Fizz"、5の倍数のときは"Buzz"、
    両方の倍数のときは"FizzBuzz"、どれにも該当しない場合はその数を文字列として出力します。

    Argument:
        n (int): FizzBuzzを実行する上限の整数値。
    Returns:
        str: FizzBuzzの結果を含む文字列。
    Restricted:
        nは1以上1000以下の整数であること。
        引数が範囲内の整数でない場合はValueErrorを発生させること。
        引数が整数でない場合はTypeErrorを発生させること。
    Example:
        >>> fizzbuzz(3)
        'Fizz'
        >>> fizzbuzz(5)
        'Buzz'
        >>> fizzbuzz(15)
        'FizzBuzz'
        >>> fizzbuzz(7)
        '7'
        >>> fizzbuzz(0)
        Traceback (most recent call last):
            ...
        ValueError: n must be between 1 and 1000.
        >>> fizzbuzz(1001)
        Traceback (most recent call last):
            ...
        ValueError: n must be between 1 and 1000.
        >>> fizzbuzz("a")
        Traceback (most recent call last):
            ...
        TypeError: n must be an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1 or n > 1000:
        raise ValueError("n must be between 1 and 1000.")

    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

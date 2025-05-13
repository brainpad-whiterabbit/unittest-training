# get_greeting テスト設計書
(作成日: 2025-05-12)

## 1. 同値分割法に基づくテスト

同値分割法は、ありうる全ての入力（この場合は `datetime.now()` が返しうる時刻）を、同じ挨拶が返されると期待される時間帯（同値クラス）に分割し、各時間帯から代表的な時刻を選んでテストする手法です。

### 1.1. 有効同値クラスのテスト

| テスト名                        | 入力 (モック時刻)     | 期待する出力       | 解説                                                            |
| :------------------------------ | :-------------------- | :----------------- | :-------------------------------------------------------------- |
| `test_greeting_morning_typical`   | `2025-05-12 09:30:00` | `"Good morning!"`  | 朝の時間帯（05:00-11:59）の典型的な時刻。                     |
| `test_greeting_afternoon_typical` | `2025-05-12 14:15:00` | `"Good afternoon!"`| 昼の時間帯（12:00-17:59）の典型的な時刻。                     |
| `test_greeting_evening_typical` | `2025-05-12 19:00:00` | `"Good evening!"`  | 夕方の時間帯（18:00-21:59）の典型的な時刻。                   |
| `test_greeting_night_typical`     | `2025-05-12 23:00:00` | `"Good night!"`    | 夜の時間帯（22:00-04:59）の典型的な時刻 (日付変更前)。          |
| `test_greeting_night_early_typical`| `2025-05-13 02:00:00` | `"Good night!"`    | 夜の時間帯（22:00-04:59）の典型的な時刻 (日付変更後)。          |

### 1.2. 無効同値クラスのテスト

`get_greeting` 関数は直接的な引数を取らず、内部で `datetime.now()` を使用するため、FizzBuzzのような型エラーや範囲外の値エラーを引き起こす入力パターンは通常想定されません。したがって、この分類に基づくテストケースはありません。

## 2. 境界値分析に基づくテスト

境界値分析は、挨拶が切り替わる時刻の境界やその直前/直後の時刻でエラーが発生しやすいという考えに基づき、これらの境界付近の時刻を重点的にテストする手法です。

| テスト名                             | 入力 (モック時刻)     | 期待する出力       | 解説                                                             |
| :----------------------------------- | :-------------------- | :----------------- | :--------------------------------------------------------------- |
| `test_greeting_boundary_night_ends`    | `2025-05-12 04:59:59` | `"Good night!"`    | 朝 (Morning) が始まる直前の時刻 (Nightの終わり)。                    |
| `test_greeting_boundary_morning_starts`| `2025-05-12 05:00:00` | `"Good morning!"`  | 朝 (Morning) が始まる瞬間の時刻。                                  |
| `test_greeting_boundary_morning_ends`  | `2025-05-12 11:59:59` | `"Good morning!"`  | 昼 (Afternoon) が始まる直前の時刻 (Morningの終わり)。              |
| `test_greeting_boundary_afternoon_starts`| `2025-05-12 12:00:00` | `"Good afternoon!"`| 昼 (Afternoon) が始まる瞬間の時刻。                                |
| `test_greeting_boundary_afternoon_ends`| `2025-05-12 17:59:59` | `"Good afternoon!"`| 夕方 (Evening) が始まる直前の時刻 (Afternoonの終わり)。            |
| `test_greeting_boundary_evening_starts`| `2025-05-12 18:00:00` | `"Good evening!"`  | 夕方 (Evening) が始まる瞬間の時刻。                                |
| `test_greeting_boundary_evening_ends`  | `2025-05-12 21:59:59` | `"Good evening!"`  | 夜 (Night) が始まる直前の時刻 (Eveningの終わり)。                  |
| `test_greeting_boundary_night_starts`  | `2025-05-12 22:00:00` | `"Good night!"`    | 夜 (Night) が始まる瞬間の時刻。                                    |
| `test_greeting_boundary_before_midnight`|`2025-05-12 23:59:59` | `"Good night!"`    | 日付が変わる (深夜0時) 直前の時刻 (Night)。                      |
| `test_greeting_boundary_at_midnight`   | `2025-05-13 00:00:00` | `"Good night!"`    | 日付が変わる (深夜0時) 瞬間の時刻 (引き続きNight)。              |
| `test_greeting_boundary_after_midnight`| `2025-05-13 00:00:01` | `"Good night!"`    | 日付が変わった (深夜0時) 直後の時刻 (引き続きNight)。            |

# unittest-training

## 概要
このプロジェクトは、pytestを使った単体テストのトレーニングを目的としたリポジトリです。

## プロジェクト構成
```
.
├── Makefile
├── README.md
├── install.sh
├── pyproject.toml
├── src/
├── tests/
└── uv.lock
```

## テストの実行方法

```bash
make test
```

## テストのカバレッジを確認する方法

```bash
make coverage
```

## コードの静的解析

```bash
make lint
```

## コードのフォーマット

```bash
make format
```

## 必要条件
- Python 3.12以上

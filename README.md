# unittest-training

## 概要
このプロジェクトは、Pythonのユニットテストのトレーニングを目的としたリポジトリです。テスト駆動開発(TDD)の基本を学ぶことができます。

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

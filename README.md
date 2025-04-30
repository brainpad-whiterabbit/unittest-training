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

## セットアップ
1. 必要な依存関係をインストールします。

```bash
make init
```

2. VSCode拡張機能のインストール
左のツールバーから拡張機能のエクスプローラを開き、以下の拡張機能がインストールされていることを確認してください。

- Python: `ms-python.python`
- Ruff: `charliermarsh.ruff`

## テストの実行方法

```bash
make test
```

## コードのフォーマット

```bash
make format
```

## 必要条件
- Python 3.12以上

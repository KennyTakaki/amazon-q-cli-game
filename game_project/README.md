# AWS Service Name Quiz

AWSサービス名クイズゲーム - AWSサービスの接頭辞（AmazonかAWS）を当てるゲーム

## ゲーム概要

このゲームは、AWSサービスの名前の接頭辞が「Amazon」か「AWS」かを当てるクイズゲームです。
サービス名の接頭辞を除いた部分が表示され、プレイヤーは正しい接頭辞を選択します。

## 遊び方

1. スタート画面で「Let's Play」ボタンをクリックしてゲームを開始します。
2. 表示されたサービス名の接頭辞が「Amazon」か「AWS」かを選択します。
3. 正解すると〇、不正解だと×が表示されます。
4. 3回間違えるか、すべての問題に回答するとゲームが終了します。
5. 結果画面で成績を確認し、「Play Again」ボタンで再プレイできます。

## 必要なライブラリ

- Python 3.x
- Pygame

## インストール方法

```bash
pip install pygame
```

## 実行方法

```bash
python main.py
```

## プロジェクト構造

```
game_project/
├── assets/
│   └── images/       # サービスアイコン画像
├── data/
│   └── aws_services.py  # AWSサービスのデータ
├── src/
│   ├── scenes/       # ゲームシーン
│   │   ├── base_scene.py
│   │   ├── start_scene.py
│   │   ├── game_scene.py
│   │   ├── result_scene.py
│   │   └── main_menu.py
│   └── utils/        # ユーティリティ
│       ├── ui.py
│       └── create_dummy_icons.py
├── main.py           # メインエントリーポイント
├── settings.py       # ゲーム設定
└── README.md         # このファイル
```

## カスタマイズ

- `data/aws_services.py` にAWSサービスを追加することでクイズの問題を増やせます
- `settings.py` でゲームの設定を変更できます
- 実際のAWSサービスアイコンを `assets/images/` に追加することで見た目を改善できます

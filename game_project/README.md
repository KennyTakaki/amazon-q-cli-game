# PyGame Game Project

このプロジェクトはPyGameを使用した2Dゲームのテンプレートです。

## ディレクトリ構成

```
game_project/
│
├── main.py              # ゲームのエントリーポイント
├── settings.py          # ゲーム設定（解像度、FPS、色など）
│
├── assets/              # ゲームのアセット
│   ├── images/          # スプライト、背景画像など
│   ├── sounds/          # 効果音
│   ├── music/           # BGM
│   └── fonts/           # フォント
│
├── src/                 # ソースコード
│   ├── entities/        # ゲームエンティティ（プレイヤー、敵など）
│   ├── ui/              # ユーザーインターフェース関連
│   ├── scenes/          # ゲームシーン
│   ├── utils/           # ユーティリティ関数
│   └── managers/        # ゲームマネージャー
│
├── data/                # ゲームデータ
│   ├── levels/          # レベルデータ
│   ├── save/            # セーブデータ
│   └── config/          # 設定ファイル
│
└── tests/               # テストコード
```

## 実行方法

```bash
python main.py
```

## 操作方法

- 左右矢印キー: 移動
- スペース: ジャンプ
- ESC: メニューに戻る

## 依存関係

- Python 3.6以上
- PyGame 2.0.0以上

```bash
pip install pygame
```

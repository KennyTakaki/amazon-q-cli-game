import pygame
import os
from data.aws_services import AWS_SERVICES

def create_dummy_icons():
    """
    AWSサービスのダミーアイコンを作成する
    実際のプロジェクトでは本物のアイコンを使用することを推奨
    """
    # Pygameを初期化
    pygame.init()
    
    # アイコンのサイズ
    icon_size = (150, 150)
    
    # 各サービスのダミーアイコンを作成
    for service in AWS_SERVICES:
        # アイコンのパスを取得
        icon_path = service["icon_path"]
        
        # ディレクトリが存在しない場合は作成
        os.makedirs(os.path.dirname(icon_path), exist_ok=True)
        
        # サービス名の最初の文字を取得
        first_letter = service["service"][0]
        
        # 背景色を決定（AmazonとAWSで色を変える）
        if service["prefix"] == "Amazon":
            bg_color = (255, 153, 0)  # AWS Orange
            text_color = (0, 0, 0)    # Black
        else:
            bg_color = (51, 51, 102)  # AWS Dark Blue
            text_color = (255, 255, 255)  # White
            
        # 新しいサーフェスを作成
        icon = pygame.Surface(icon_size)
        icon.fill(bg_color)
        
        # サービス名の最初の文字を描画
        font = pygame.font.Font(None, 100)
        text = font.render(first_letter, True, text_color)
        text_rect = text.get_rect(center=(icon_size[0] // 2, icon_size[1] // 2))
        icon.blit(text, text_rect)
        
        # アイコンを保存
        pygame.image.save(icon, icon_path)
        
    print(f"{len(AWS_SERVICES)}個のダミーアイコンを作成しました。")

if __name__ == "__main__":
    create_dummy_icons()

import pygame
from settings import *
from src.scenes.base_scene import BaseScene
from src.utils.ui import Button, draw_text, draw_rounded_rect
from src.scenes.game_scene import GameScene

class StartScene(BaseScene):
    """ゲームのスタート画面"""
    
    def __init__(self, game):
        super().__init__(game)
        
        # ボタンの作成
        button_x = WIDTH // 2 - BUTTON_WIDTH // 2
        button_y = HEIGHT * 0.7
        self.play_button = Button(
            button_x, button_y, 
            BUTTON_WIDTH, BUTTON_HEIGHT, 
            "Let's Play", 
            AWS_ORANGE, 
            ORANGE
        )
        
    def handle_events(self, event):
        """イベント処理"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_button.is_clicked(event):
                # メイン画面に遷移
                self.game.change_scene(GameScene(self.game))
                
    def update(self):
        """シーンの状態を更新"""
        mouse_pos = pygame.mouse.get_pos()
        self.play_button.update(mouse_pos)
        
    def render(self, screen):
        """シーンを描画"""
        # 背景
        screen.fill(AWS_DARK_BLUE)
        
        # タイトル
        draw_text(screen, "AWS Service Name Quiz", TITLE_FONT_SIZE, WIDTH // 2, HEIGHT * 0.2, AWS_ORANGE)
        
        # ゲーム説明
        explanation_box = pygame.Rect(WIDTH * 0.1, HEIGHT * 0.3, WIDTH * 0.8, HEIGHT * 0.3)
        draw_rounded_rect(screen, explanation_box, LIGHT_GRAY, radius=15)
        
        instructions = [
            "AWSには「Amazon」または「AWS」で始まるサービスがあります。",
            "サービス名の先頭部分が表示されていないので、",
            "「Amazon」か「AWS」のどちらで始まるか当ててください！",
            "",
            "3回間違えるとゲーム終了です。チャレンジしてみましょう！"
        ]
        
        for i, line in enumerate(instructions):
            draw_text(
                screen, 
                line, 
                SMALL_FONT_SIZE, 
                WIDTH // 2, 
                HEIGHT * 0.35 + i * 30, 
                BLACK
            )
        
        # プレイボタン
        self.play_button.draw(screen)

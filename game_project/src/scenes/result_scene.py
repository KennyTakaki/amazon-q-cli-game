import pygame
from settings import *
from src.scenes.base_scene import BaseScene
from src.utils.ui import Button, draw_text, draw_rounded_rect

class ResultScene(BaseScene):
    """ゲームの結果画面"""
    
    def __init__(self, game, correct_count, mistake_count):
        super().__init__(game)
        
        # 結果を保存
        self.correct_count = correct_count
        self.mistake_count = mistake_count
        self.total_questions = correct_count + mistake_count
        
        # 再プレイボタンの作成
        button_x = WIDTH // 2 - BUTTON_WIDTH // 2
        button_y = HEIGHT * 0.7
        self.replay_button = Button(
            button_x, button_y, 
            BUTTON_WIDTH, BUTTON_HEIGHT, 
            "Play Again", 
            AWS_ORANGE, 
            ORANGE
        )
        
    def handle_events(self, event):
        """イベント処理"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.replay_button.is_clicked(event):
                # スタート画面に遷移
                from src.scenes.start_scene import StartScene
                self.game.change_scene(StartScene(self.game))
                
    def update(self):
        """シーンの状態を更新"""
        mouse_pos = pygame.mouse.get_pos()
        self.replay_button.update(mouse_pos)
        
    def render(self, screen):
        """シーンを描画"""
        # 背景
        screen.fill(AWS_DARK_BLUE)
        
        # タイトル
        draw_text(screen, "ゲーム結果", TITLE_FONT_SIZE, WIDTH // 2, HEIGHT * 0.2, AWS_ORANGE)
        
        # 結果表示用の背景ボックス
        result_box = pygame.Rect(WIDTH * 0.2, HEIGHT * 0.3, WIDTH * 0.6, HEIGHT * 0.3)
        draw_rounded_rect(screen, result_box, WHITE, radius=15)
        
        # スコア表示
        accuracy = 0
        if self.total_questions > 0:
            accuracy = (self.correct_count / self.total_questions) * 100
            
        draw_text(
            screen, 
            f"正解数: {self.correct_count}", 
            NORMAL_FONT_SIZE, 
            WIDTH // 2, 
            HEIGHT * 0.38, 
            BLACK
        )
        
        draw_text(
            screen, 
            f"間違い数: {self.mistake_count}", 
            NORMAL_FONT_SIZE, 
            WIDTH // 2, 
            HEIGHT * 0.45, 
            BLACK
        )
        
        draw_text(
            screen, 
            f"正答率: {accuracy:.1f}%", 
            NORMAL_FONT_SIZE, 
            WIDTH // 2, 
            HEIGHT * 0.52, 
            BLACK
        )
        
        # 評価メッセージ
        message = ""
        if accuracy >= 90:
            message = "素晴らしい！AWSマスターですね！"
        elif accuracy >= 70:
            message = "よくできました！AWSの知識が豊富です！"
        elif accuracy >= 50:
            message = "まずまずの結果です。もう少し練習しましょう！"
        else:
            message = "AWSサービスについてもっと学びましょう！"
            
        draw_text(screen, message, NORMAL_FONT_SIZE, WIDTH // 2, HEIGHT * 0.6, AWS_ORANGE)
        
        # 再プレイボタン
        self.replay_button.draw(screen)

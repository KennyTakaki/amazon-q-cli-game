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
        
        # 再プレイボタンの作成 - 位置を調整
        button_x = WIDTH // 2 - BUTTON_WIDTH // 2
        button_y = HEIGHT * 0.78  # 白い背景の下に配置するために位置を下げる
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
        draw_text(screen, "Game Results", TITLE_FONT_SIZE, WIDTH // 2, HEIGHT * 0.15, AWS_ORANGE)
        
        # 結果表示用の背景ボックス - 評価メッセージも含めるために高さを拡大
        result_box = pygame.Rect(WIDTH * 0.15, HEIGHT * 0.25, WIDTH * 0.7, HEIGHT * 0.45)
        draw_rounded_rect(screen, result_box, WHITE, radius=15)
        
        # スコア表示
        accuracy = 0
        if self.total_questions > 0:
            accuracy = (self.correct_count / self.total_questions) * 100
            
        draw_text(
            screen, 
            f"Correct: {self.correct_count}", 
            SUBTITLE_FONT_SIZE, 
            WIDTH // 2, 
            HEIGHT * 0.35, 
            BLACK
        )
        
        draw_text(
            screen, 
            f"Wrong: {self.mistake_count}", 
            SUBTITLE_FONT_SIZE, 
            WIDTH // 2, 
            HEIGHT * 0.43, 
            BLACK
        )
        
        draw_text(
            screen, 
            f"Accuracy: {accuracy:.1f}%", 
            SUBTITLE_FONT_SIZE, 
            WIDTH // 2, 
            HEIGHT * 0.51, 
            BLACK
        )
        
        # 評価メッセージ - 白い背景の中に配置
        message = ""
        if accuracy >= 90:
            message = "Excellent! You're an AWS Master!"
        elif accuracy >= 70:
            message = "Well done! You have good AWS knowledge!"
        elif accuracy >= 50:
            message = "Not bad. Keep practicing!"
        else:
            message = "Learn more about AWS services!"
            
        draw_text(screen, message, NORMAL_FONT_SIZE, WIDTH // 2, HEIGHT * 0.60, AWS_ORANGE)
        
        # 再プレイボタン - 白い背景の下に配置
        self.replay_button.draw(screen)

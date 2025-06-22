import pygame
import random
import os
from settings import *
from src.scenes.base_scene import BaseScene
from src.utils.ui import Button, draw_text, draw_rounded_rect
from data.aws_services import AWS_SERVICES

class GameScene(BaseScene):
    """ゲームのメイン画面"""
    
    def __init__(self, game):
        super().__init__(game)
        
        # ゲーム状態の初期化
        self.correct_count = 0
        self.mistake_count = 0
        self.total_questions = 0
        
        # サービスリストをシャッフル
        self.services = AWS_SERVICES.copy()
        random.shuffle(self.services)
        self.current_service_index = 0
        
        # ボタンの作成
        button_width = BUTTON_WIDTH
        button_height = BUTTON_HEIGHT
        button_y = HEIGHT * 0.6
        
        # Amazonボタン
        self.amazon_button = Button(
            WIDTH // 4 - button_width // 2,
            button_y,
            button_width,
            button_height,
            "Amazon",
            AWS_ORANGE,
            ORANGE
        )
        
        # AWSボタン
        self.aws_button = Button(
            WIDTH * 3 // 4 - button_width // 2,
            button_y,
            button_width,
            button_height,
            "AWS",
            AWS_DARK_BLUE,
            BLUE
        )
        
        # フィードバック状態
        self.showing_feedback = False
        self.feedback_correct = False
        self.feedback_timer = 0
        self.feedback_start_time = 0
        
        # デフォルトのアイコン画像をロード
        self.default_icon = pygame.Surface((150, 150))
        self.default_icon.fill(LIGHT_GRAY)
        
        # 現在のサービスのアイコンをロード
        self.current_icon = self.default_icon
        self.load_current_service_icon()
        
    def load_current_service_icon(self):
        """現在のサービスのアイコンをロード"""
        if self.current_service_index < len(self.services):
            service = self.services[self.current_service_index]
            icon_path = service["icon_path"]
            
            # 絶対パスに変換
            current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            full_icon_path = os.path.join(current_dir, icon_path)
            
            # アイコンが存在するか確認
            if os.path.exists(full_icon_path):
                try:
                    self.current_icon = pygame.image.load(full_icon_path).convert_alpha()
                    # アイコンのサイズを調整
                    self.current_icon = pygame.transform.scale(self.current_icon, (150, 150))
                except pygame.error:
                    print(f"アイコンの読み込みに失敗しました: {full_icon_path}")
                    self.current_icon = self.default_icon
            else:
                print(f"アイコンが見つかりません: {full_icon_path}")
                self.current_icon = self.default_icon
        
    def handle_events(self, event):
        """イベント処理"""
        if event.type == pygame.MOUSEBUTTONDOWN and not self.showing_feedback:
            if self.amazon_button.is_clicked(event):
                self.check_answer("Amazon")
            elif self.aws_button.is_clicked(event):
                self.check_answer("AWS")
                
    def check_answer(self, selected_prefix):
        """回答をチェック"""
        if self.current_service_index < len(self.services):
            current_service = self.services[self.current_service_index]
            correct_prefix = current_service["prefix"]
            
            # 正解判定
            is_correct = selected_prefix == correct_prefix
            
            # カウンターを更新
            if is_correct:
                self.correct_count += 1
            else:
                self.mistake_count += 1
                
            self.total_questions += 1
            
            # フィードバック表示
            self.showing_feedback = True
            self.feedback_correct = is_correct
            self.feedback_start_time = pygame.time.get_ticks()
            
            # 次のサービスへ
            self.current_service_index += 1
            self.load_current_service_icon()
            
            # 終了条件をチェック
            if self.mistake_count >= MAX_MISTAKES or self.current_service_index >= len(self.services):
                # 少し待ってから結果画面へ
                pygame.time.set_timer(pygame.USEREVENT, FEEDBACK_DURATION)
                
    def update(self):
        """シーンの状態を更新"""
        mouse_pos = pygame.mouse.get_pos()
        
        # ボタンの状態を更新
        self.amazon_button.update(mouse_pos)
        self.aws_button.update(mouse_pos)
        
        # フィードバック表示のタイマー処理
        if self.showing_feedback:
            current_time = pygame.time.get_ticks()
            if current_time - self.feedback_start_time > FEEDBACK_DURATION:
                self.showing_feedback = False
                
                # 終了条件をチェック
                if self.mistake_count >= MAX_MISTAKES or self.current_service_index >= len(self.services):
                    # 結果画面へ遷移
                    from src.scenes.result_scene import ResultScene
                    self.game.change_scene(ResultScene(self.game, self.correct_count, self.mistake_count))
        
    def render(self, screen):
        """シーンを描画"""
        # 背景
        screen.fill(WHITE)
        
        # スコア表示
        score_text = f"Correct: {self.correct_count}  Wrong: {self.mistake_count}/{MAX_MISTAKES}"
        draw_text(screen, score_text, NORMAL_FONT_SIZE, WIDTH // 2, HEIGHT * 0.1, BLACK)
        
        # 現在のサービス情報を表示
        if self.current_service_index < len(self.services):
            current_service = self.services[self.current_service_index]
            
            # サービスアイコンを表示
            icon_rect = self.current_icon.get_rect(center=(WIDTH // 2, HEIGHT * 0.3))
            screen.blit(self.current_icon, icon_rect)
            
            # サービス名を表示（接頭辞なし）
            service_name = current_service["service"]
            draw_text(screen, service_name, SUBTITLE_FONT_SIZE, WIDTH // 2, HEIGHT * 0.45, BLACK)
            
            # 説明テキスト
            draw_text(screen, "Which prefix?", NORMAL_FONT_SIZE, WIDTH // 2, HEIGHT * 0.52, DARK_GRAY)
            
            # ボタンを描画
            if not self.showing_feedback:
                self.amazon_button.draw(screen)
                self.aws_button.draw(screen)
        
        # フィードバック表示
        if self.showing_feedback:
            feedback_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT * 0.65, 300, 150)
            
            if self.feedback_correct:
                # 正解フィードバック
                draw_rounded_rect(screen, feedback_rect, GREEN, radius=15)
                draw_text(screen, "Correct!", TITLE_FONT_SIZE, WIDTH // 2, HEIGHT * 0.72, WHITE)
            else:
                # 不正解フィードバック
                draw_rounded_rect(screen, feedback_rect, RED, radius=15)
                draw_text(screen, "Wrong!", TITLE_FONT_SIZE, WIDTH // 2, HEIGHT * 0.72, WHITE)

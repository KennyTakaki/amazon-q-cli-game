import pygame
from settings import *
from src.scenes.base_scene import BaseScene

class MainMenu(BaseScene):
    """メインメニュー（スタート画面に直接遷移）"""
    
    def __init__(self, game):
        super().__init__(game)
        # 初期化後にスタート画面に遷移するようにする
        self.initialized = False
        
    def handle_events(self, event):
        pass
        
    def update(self):
        # 初期化後の最初のフレームでスタート画面に遷移
        if not self.initialized:
            self.initialized = True
            # 循環インポートを避けるためにここでインポート
            from src.scenes.start_scene import StartScene
            self.game.change_scene(StartScene(self.game))
        
    def render(self, screen):
        screen.fill(BLACK)

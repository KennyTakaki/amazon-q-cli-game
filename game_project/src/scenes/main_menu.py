import pygame
from settings import *
from src.scenes.base_scene import BaseScene
from src.scenes.start_scene import StartScene

class MainMenu(BaseScene):
    """メインメニュー（スタート画面に直接遷移）"""
    
    def __init__(self, game):
        super().__init__(game)
        # スタート画面に直接遷移
        self.game.change_scene(StartScene(self.game))
        
    def handle_events(self, event):
        pass
        
    def update(self):
        pass
        
    def render(self, screen):
        screen.fill(BLACK)

import pygame

class BaseScene:
    """すべてのシーンの基底クラス"""
    
    def __init__(self, game):
        self.game = game
        
    def handle_events(self, event):
        """イベント処理"""
        pass
        
    def update(self):
        """シーンの状態を更新"""
        pass
        
    def render(self, screen):
        """シーンを描画"""
        pass

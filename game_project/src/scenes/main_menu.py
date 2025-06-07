import pygame
from settings import *
from src.ui.menu import Button
from src.scenes.game_level import GameLevel

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont(None, 48)
        
        # メニューボタン
        button_width = 200
        button_height = 50
        button_x = WIDTH // 2 - button_width // 2
        
        self.start_button = Button(
            button_x, 
            HEIGHT // 2 - 50, 
            button_width, 
            button_height, 
            "Start Game", 
            self.start_game
        )
        
        self.quit_button = Button(
            button_x, 
            HEIGHT // 2 + 50, 
            button_width, 
            button_height, 
            "Quit", 
            self.quit_game
        )
    
    def handle_events(self, event):
        self.start_button.handle_event(event)
        self.quit_button.handle_event(event)
    
    def update(self):
        pass
    
    def render(self, screen):
        # タイトル
        title_text = self.font.render(TITLE, True, WHITE)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(title_text, title_rect)
        
        # ボタン
        self.start_button.draw(screen)
        self.quit_button.draw(screen)
    
    def start_game(self):
        # ゲームレベルシーンに切り替え
        self.game.change_scene(GameLevel(self.game))
    
    def quit_game(self):
        self.game.quit()

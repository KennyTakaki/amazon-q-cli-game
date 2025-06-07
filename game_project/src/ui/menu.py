import pygame
from settings import *

class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.font = pygame.font.SysFont(None, 32)
        self.normal_color = BLUE
        self.hover_color = YELLOW
        self.text_color = WHITE
        self.is_hovered = False
    
    def handle_event(self, event):
        # マウス位置の取得
        mouse_pos = pygame.mouse.get_pos()
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        
        # クリック処理
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.action:
                self.action()
    
    def draw(self, surface):
        # ボタンの背景
        color = self.hover_color if self.is_hovered else self.normal_color
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, WHITE, self.rect, 2)  # 枠線
        
        # テキスト
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

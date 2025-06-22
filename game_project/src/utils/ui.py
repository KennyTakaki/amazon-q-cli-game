import pygame
from settings import *

class Button:
    """ボタンクラス"""
    
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=WHITE, radius=BUTTON_RADIUS):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.radius = radius
        self.is_hovered = False
        
    def draw(self, surface):
        """ボタンを描画する"""
        color = self.hover_color if self.is_hovered else self.color
        
        # 角丸の矩形を描画
        pygame.draw.rect(surface, color, self.rect, border_radius=self.radius)
        
        # テキストを描画
        font = pygame.font.Font(None, NORMAL_FONT_SIZE)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def update(self, mouse_pos):
        """ボタンの状態を更新する"""
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        
    def is_clicked(self, event):
        """ボタンがクリックされたかどうかを判定する"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.is_hovered
        return False


def draw_text(surface, text, size, x, y, color=WHITE, align="center"):
    """テキストを描画する"""
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    
    if align == "center":
        text_rect.center = (x, y)
    elif align == "left":
        text_rect.midleft = (x, y)
    elif align == "right":
        text_rect.midright = (x, y)
        
    surface.blit(text_surface, text_rect)
    return text_rect


def draw_rounded_rect(surface, rect, color, radius=10, border=0, border_color=None):
    """角丸の矩形を描画する"""
    if border_color is None:
        border_color = color
        
    if border > 0:
        # 外側の矩形（ボーダー）
        pygame.draw.rect(surface, border_color, rect, border_radius=radius)
        
        # 内側の矩形
        inner_rect = pygame.Rect(
            rect.left + border,
            rect.top + border,
            rect.width - border * 2,
            rect.height - border * 2
        )
        pygame.draw.rect(surface, color, inner_rect, border_radius=radius)
    else:
        # ボーダーなしの場合は単純に矩形を描画
        pygame.draw.rect(surface, color, rect, border_radius=radius)

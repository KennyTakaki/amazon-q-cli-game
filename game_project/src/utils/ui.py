import pygame
import os
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
        draw_text(surface, self.text, NORMAL_FONT_SIZE, self.rect.centerx, self.rect.centery, self.text_color)
        
    def update(self, mouse_pos):
        """ボタンの状態を更新する"""
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        
    def is_clicked(self, event):
        """ボタンがクリックされたかどうかを判定する"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.is_hovered
        return False


def draw_text(surface, text, size, x, y, color=WHITE, align="center"):
    """テキストを描画する - シンプルな実装"""
    # デフォルトフォントを使用
    font = pygame.font.Font(None, size)
    
    # テキストが空でないことを確認
    if not text:
        text = " "
    
    # ASCII文字のみを使用（日本語文字を一時的に置き換え）
    safe_text = ""
    for char in text:
        if ord(char) < 128:  # ASCII文字のみ
            safe_text += char
        else:
            # 日本語文字は一時的に置き換え
            if "正解" in text:
                safe_text = "Correct!"
            elif "不正解" in text:
                safe_text = "Wrong!"
            elif "このサービスの接頭辞は" in text:
                safe_text = "Prefix?"
            elif "ゲーム結果" in text:
                safe_text = "Results"
            elif "正解数" in text:
                safe_text = f"Correct: {text.split(':')[1] if ':' in text else ''}"
            elif "間違い数" in text:
                safe_text = f"Wrong: {text.split(':')[1] if ':' in text else ''}"
            elif "正答率" in text:
                safe_text = f"Accuracy: {text.split(':')[1] if ':' in text else ''}"
            elif "素晴らしい" in text:
                safe_text = "Excellent! AWS Master!"
            elif "よくできました" in text:
                safe_text = "Well done! Good knowledge!"
            elif "まずまず" in text:
                safe_text = "Not bad. Keep practicing!"
            elif "もっと学びましょう" in text:
                safe_text = "Learn more about AWS services!"
            else:
                safe_text = "AWS Quiz"
            break
    
    text_surface = font.render(safe_text, True, color)
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

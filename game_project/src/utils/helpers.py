import pygame
import os
import json
from settings import *

def load_json(file_path):
    """JSONファイルを読み込む"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"JSONファイルの読み込みに失敗しました: {file_path}")
        print(e)
        return {}

def save_json(file_path, data):
    """JSONファイルに保存する"""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        print(f"JSONファイルの保存に失敗しました: {file_path}")
        print(e)
        return False

def draw_text(surface, text, font, color, x, y, align="topleft"):
    """テキストを描画する"""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    
    # 位置合わせ
    if align == "center":
        text_rect.center = (x, y)
    elif align == "midtop":
        text_rect.midtop = (x, y)
    elif align == "midbottom":
        text_rect.midbottom = (x, y)
    elif align == "topleft":
        text_rect.topleft = (x, y)
    elif align == "topright":
        text_rect.topright = (x, y)
    elif align == "bottomleft":
        text_rect.bottomleft = (x, y)
    elif align == "bottomright":
        text_rect.bottomright = (x, y)
    
    surface.blit(text_surface, text_rect)
    return text_rect

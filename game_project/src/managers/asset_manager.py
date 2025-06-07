import pygame
import os
from settings import *

class AssetManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.music = {}
        self.fonts = {}
        
        # オーディオが利用可能かどうか
        self.audio_available = pygame.mixer.get_init() is not None
    
    def load_image(self, name, file_name, scale=1):
        """画像をロードしてキャッシュする"""
        if name not in self.images:
            path = os.path.join(IMAGE_DIR, file_name)
            try:
                image = pygame.image.load(path).convert_alpha()
                if scale != 1:
                    w, h = image.get_size()
                    image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
                self.images[name] = image
            except pygame.error as e:
                print(f"画像の読み込みに失敗しました: {path}")
                print(e)
                # 代替画像（エラー表示用）
                self.images[name] = self._create_error_image()
        return self.images[name]
    
    def load_sound(self, name, file_name):
        """効果音をロードしてキャッシュする"""
        if not self.audio_available:
            # オーディオが利用できない場合はダミーのサウンドオブジェクトを返す
            return DummySound()
            
        if name not in self.sounds:
            path = os.path.join(SOUND_DIR, file_name)
            try:
                self.sounds[name] = pygame.mixer.Sound(path)
            except pygame.error as e:
                print(f"効果音の読み込みに失敗しました: {path}")
                print(e)
                self.sounds[name] = DummySound()
        return self.sounds[name]
    
    def load_music(self, name, file_name):
        """BGMのパスをキャッシュする"""
        if not self.audio_available:
            return None
            
        if name not in self.music:
            path = os.path.join(MUSIC_DIR, file_name)
            if os.path.exists(path):
                self.music[name] = path
            else:
                print(f"BGMファイルが見つかりません: {path}")
        return self.music.get(name)
    
    def load_font(self, name, file_name, size):
        """フォントをロードしてキャッシュする"""
        key = f"{name}_{size}"
        if key not in self.fonts:
            path = os.path.join(FONT_DIR, file_name)
            try:
                self.fonts[key] = pygame.font.Font(path, size)
            except pygame.error as e:
                print(f"フォントの読み込みに失敗しました: {path}")
                print(e)
                # デフォルトフォントを使用
                self.fonts[key] = pygame.font.SysFont(None, size)
        return self.fonts[key]
    
    def _create_error_image(self, width=32, height=32):
        """エラー表示用の画像を作成"""
        image = pygame.Surface((width, height))
        image.fill((255, 0, 255))  # マゼンタ
        pygame.draw.line(image, (0, 0, 0), (0, 0), (width, height), 2)
        pygame.draw.line(image, (0, 0, 0), (0, height), (width, 0), 2)
        return image

class DummySound:
    """オーディオが利用できない場合のダミーサウンドクラス"""
    def play(self, *args, **kwargs):
        pass
    
    def stop(self):
        pass
    
    def set_volume(self, volume):
        pass

# シングルトンインスタンス
asset_manager = AssetManager()

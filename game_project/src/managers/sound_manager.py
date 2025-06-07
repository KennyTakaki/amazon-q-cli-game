import pygame
from src.managers.asset_manager import asset_manager

class SoundManager:
    def __init__(self):
        self.current_music = None
        self.music_volume = 0.5
        self.sound_volume = 1.0
        self.sounds_enabled = True
        self.music_enabled = True
        
        # オーディオが利用可能かどうか
        self.audio_available = pygame.mixer.get_init() is not None
    
    def play_sound(self, name):
        """効果音を再生"""
        if not self.sounds_enabled or not self.audio_available:
            return
            
        sound = asset_manager.load_sound(name, f"{name}.wav")
        sound.set_volume(self.sound_volume)
        sound.play()
    
    def play_music(self, name, loops=-1):
        """BGMを再生"""
        if not self.music_enabled or not self.audio_available:
            return
            
        if self.current_music == name:
            return
            
        self.current_music = name
        music_path = asset_manager.load_music(name, f"{name}.mp3")
        
        if music_path:
            try:
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.set_volume(self.music_volume)
                pygame.mixer.music.play(loops)
            except pygame.error as e:
                print(f"BGMの再生に失敗しました: {e}")
                self.current_music = None
    
    def stop_music(self):
        """BGMを停止"""
        if not self.audio_available:
            return
        pygame.mixer.music.stop()
        self.current_music = None
    
    def pause_music(self):
        """BGMを一時停止"""
        if not self.audio_available:
            return
        pygame.mixer.music.pause()
    
    def unpause_music(self):
        """BGMを再開"""
        if not self.audio_available:
            return
        pygame.mixer.music.unpause()
    
    def set_music_volume(self, volume):
        """BGMの音量を設定 (0.0 ~ 1.0)"""
        self.music_volume = max(0.0, min(1.0, volume))
        if self.audio_available:
            pygame.mixer.music.set_volume(self.music_volume)
    
    def set_sound_volume(self, volume):
        """効果音の音量を設定 (0.0 ~ 1.0)"""
        self.sound_volume = max(0.0, min(1.0, volume))
    
    def toggle_sounds(self):
        """効果音のオン/オフを切り替え"""
        self.sounds_enabled = not self.sounds_enabled
        return self.sounds_enabled
    
    def toggle_music(self):
        """BGMのオン/オフを切り替え"""
        self.music_enabled = not self.music_enabled
        if self.music_enabled and self.current_music and self.audio_available:
            self.play_music(self.current_music)
        else:
            self.stop_music()
        return self.music_enabled

# シングルトンインスタンス
sound_manager = SoundManager()

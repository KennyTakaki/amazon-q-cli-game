#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys
import os

# 現在のディレクトリをパスに追加
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from settings import *
from src.scenes.main_menu import MainMenu
from src.utils.create_dummy_icons import create_dummy_icons

class Game:
    def __init__(self):
        # Pygameの初期化
        pygame.init()
        
        # オーディオ初期化（失敗しても続行）
        try:
            pygame.mixer.init()
            self.audio_enabled = True
        except pygame.error:
            print("警告: オーディオデバイスが見つかりません。サウンドは無効化されます。")
            self.audio_enabled = False
        
        # 画面設定
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        
        # ダミーアイコンを作成（実際のプロジェクトでは本物のアイコンを使用）
        create_dummy_icons()
        
        # 現在のシーン
        self.current_scene = MainMenu(self)
        
    def run(self):
        # メインゲームループ
        while True:
            # イベント処理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                self.current_scene.handle_events(event)
            
            # 更新
            self.current_scene.update()
            
            # 描画
            self.screen.fill(BLACK)
            self.current_scene.render(self.screen)
            pygame.display.flip()
            
            # FPS制御
            self.clock.tick(FPS)
    
    def change_scene(self, scene):
        self.current_scene = scene
    
    def quit(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()

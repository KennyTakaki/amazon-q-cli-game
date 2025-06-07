import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # 仮のプレイヤー画像（後で実際の画像に置き換え）
        self.image = pygame.Surface((32, 32))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # 移動関連の変数
        self.vel_x = 0
        self.vel_y = 0
        self.is_jumping = False
        
    def update(self):
        # 重力
        self.vel_y += GRAVITY
        
        # 移動
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # 画面外に出ないように
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel_y = 0
            self.is_jumping = False
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.vel_x = -PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                self.vel_x = PLAYER_SPEED
            if event.key == pygame.K_SPACE and not self.is_jumping:
                self.vel_y = -JUMP_POWER
                self.is_jumping = True
        
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                self.vel_x = 0

import pygame
from settings import *
from src.entities.player import Player

class GameLevel:
    def __init__(self, game):
        self.game = game
        
        # スプライトグループ
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        
        # プレイヤー作成
        self.player = Player(WIDTH // 2, HEIGHT // 2)
        self.all_sprites.add(self.player)
        
        # 仮のプラットフォーム（後でレベルデータから読み込む）
        self.create_platform(0, HEIGHT - 40, WIDTH, 40)
        self.create_platform(WIDTH // 2 - 50, HEIGHT - 200, 100, 20)
        self.create_platform(WIDTH // 4 - 50, HEIGHT - 300, 100, 20)
        self.create_platform(WIDTH * 3 // 4 - 50, HEIGHT - 300, 100, 20)
    
    def create_platform(self, x, y, width, height):
        platform = pygame.sprite.Sprite()
        platform.image = pygame.Surface((width, height))
        platform.image.fill(GREEN)
        platform.rect = platform.image.get_rect()
        platform.rect.x = x
        platform.rect.y = y
        self.all_sprites.add(platform)
        self.platforms.add(platform)
    
    def handle_events(self, event):
        self.player.handle_event(event)
        
        # ESCキーでメインメニューに戻る
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            from src.scenes.main_menu import MainMenu
            self.game.change_scene(MainMenu(self.game))
    
    def update(self):
        self.all_sprites.update()
        
        # プレイヤーとプラットフォームの衝突判定
        if self.player.vel_y > 0:  # 落下中のみ判定
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                # 一番上のプラットフォームの上に乗る
                self.player.rect.bottom = hits[0].rect.top
                self.player.vel_y = 0
                self.player.is_jumping = False
    
    def render(self, screen):
        self.all_sprites.draw(screen)
        
        # スコア表示など
        font = pygame.font.SysFont(None, 36)
        score_text = font.render("Score: 0", True, WHITE)
        screen.blit(score_text, (10, 10))

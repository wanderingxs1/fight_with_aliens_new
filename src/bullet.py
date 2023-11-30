import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理飞船发射的子弹的类"""
    def __init__(self, ai_game):
        """在飞船当前位置创建一个子弹"""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # 首先创建一个普通子弹的正方形，然后再把他移动到正确的位置
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)


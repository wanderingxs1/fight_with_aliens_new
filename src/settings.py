import pygame.image


class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230, 230, 230)
        # 标题设置
        self.caption = "Alien Invasion"
        # 标题图片
        self.caption_image = pygame.image.load("images/github头像.jpg")
        # 飞船设置
        self.ship_speed = 0.05
        # 子弹设置
        self.bullet_speed = 0.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

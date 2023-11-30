import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船和它的位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.settings

        # 加载飞船图像并且获得其对应矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 将图片矩形和屏幕矩形位置关联起来
        # 也就是每个新的飞船都放在屏幕矩形的下边中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 飞船的x向坐标，浮点数（因为self.rect.x只能存储整数
        self.x = float(self.rect.x)

        # 飞船的左右移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """移动飞船左右位置"""
        if self.moving_left and self.rect.left >= 0:
            self.x -= self.setting.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        self.rect.x = self.x

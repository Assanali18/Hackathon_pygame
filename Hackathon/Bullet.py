import pygame, var
from pygame.locals import *
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direct):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('images/bullet.png'), (24, 12))
        self.x, self.y = x, y
        self.direct = direct
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
    def move(self):
        self.rect.move_ip(self.direct, 0)
        var.screen.blit(self.image, self.rect)
        if self.rect.left > 800:
            self.kill()


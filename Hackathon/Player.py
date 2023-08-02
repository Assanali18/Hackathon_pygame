import pygame, var
from pygame.locals import *
from var import screenWidth 


class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.transform.scale(image, (40, 40))
        self.playerX = int(screenWidth * 0.3)
        self.playerY = int((var.screenHeight - self.image.get_height()) * 0.5)
        self.rect = self.image.get_rect(topleft = (self.playerX, self.playerY)) 
        self.velocity = 0

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            self.rect.move_ip(0, -6)
        if not pressed_keys[K_SPACE]:
            self.rect.move_ip(0, 4)



        var.screen.blit(self.image, self.rect)

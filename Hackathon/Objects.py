
from Player import Player
from Base import Base
from Mario import Mario
import pygame, var

# Objects
Bird = Player(var.skin)
Base = Base()
mario = Mario()

# Sprites
bullet = pygame.sprite.Group()
bullet_mario = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(Bird)
trigger = pygame.sprite.Group()

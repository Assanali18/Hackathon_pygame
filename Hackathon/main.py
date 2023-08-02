######### RUN THIS FILE #########
import pygame  
from start_game import * 

if __name__ == "__main__":
    pygame.init()
    fps_clock = pygame.time.Clock() 
    fps_clock.tick(240)
    pygame.display.set_caption('Adventures of Flappy Bird')
    while True:
        startGame()   
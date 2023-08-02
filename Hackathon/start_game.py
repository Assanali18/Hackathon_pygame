import pygame, sys, var, Objects, Play
from pygame.locals import * 
from Functions import * 

pygame.init()

def startGame():
    # Base set
    tittle = pygame.transform.scale(pygame.image.load('images/tittles/tittle.png'), (500, 100))
    skin_button = pygame.transform.scale(pygame.image.load('images/buttons/skin_but.png'), (150, 50))
    start_button = pygame.transform.scale(pygame.image.load('images/buttons/start_but.png'), (150, 50))
    brend = pygame.image.load('images/tittles/brend.png')
    titleX = int((var.screenWidth - tittle.get_width()) * 0.5)
    titleY = int(var.screenHeight*0.2)
    pygame.mixer.music.load('music/menu_music.mp3')
    pygame.mixer.music.play(-1)

    # Start conditions
    var.firstLevel = True
    var.secondLevel = False
    var.thirdLevel = False
    var.scrollSpeed = 6
    var.speedEnemies = 6
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            tap = pygame.mouse.get_pressed()
            if tap[0] == 1:
                # Button of play game     
                mousepos = pygame.mouse.get_pos()
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP) or 430<=mousepos[0]<=580 and 420<= mousepos[1]<=470:
                    pygame.mixer.music.pause()
                    Play.game()
                # Button of skrin change
                elif 230<=mousepos[0]<=380 and 420<= mousepos[1]<=470:
                    skinScreen()
        # background
        var.screen.blit(var.background, (0,0))
        # tittle
        var.screen.blit(tittle, (titleX, titleY))
        # current skin
        var.screen.blit(var.skin, (titleX+220, titleY+160) )
        # Skin button
        var.screen.blit(skin_button, (titleX+70, titleY + 300 ))
        # Start button
        var.screen.blit(start_button, (titleX + 270, titleY + 300 ))
        # Brend title
        var.screen.blit(brend, (titleX + 120, titleY + 400 ))
        
        Objects.Base.move()
        pygame.display.update()
        var.fps_clock.tick(var.framePerSecond)

        






                
                
        
import pygame, var, sys, start_game as sg, Objects, Play
from pygame.locals import *


# Front render score
def renderScore():
    scoreFont = pygame.font.Font(r"front/bionicle-training-card-font-2-4.ttf", 26)
    display = scoreFont.render(f"Score {int(var.score)}", True, (84, 120, 48))
    var.screen.blit(display, (10, 10))


# Check collisions and game over
def crashTest():
    if pygame.sprite.spritecollideany(Objects.Bird, Objects.trigger) or Objects.Bird.rect.top <= 0 or Objects.Bird.rect.bottom >= 550:
       gameover()
def gameover():
    pygame.mixer.music.load('music/hit.mp3')
    pygame.mixer.music.play()

    # Game over screen set
    gameOverX = int((var.screenWidth - var.gameOver.get_width()) * 0.5)
    gameOverY = int(var.screenHeight*0.2)
    var.screen.blit(var.background, (0, 0))
    var.screen.blit(var.gameOver, (gameOverX-20, gameOverY))

    # Board
    var.screen.blit(var.board, (gameOverX+10, gameOverY+150))
    restart_button = pygame.transform.scale(pygame.image.load('images/buttons/restart.png'), (150, 50))
    var.screen.blit(restart_button, ( 300, 470 ))
    var.screen.blit(Objects.Base.image, (0, var.baseY))

    # Score render
    max_score = checkMax(var.score)
    scoreFont = pygame.font.Font(r"front/bionicle-training-card-font-2-4.ttf", 40)
    display = scoreFont.render(f"{int(var.score)}", True, (84, 120, 48))
    display_max_score = scoreFont.render(f"{int(max_score)}", True, (84, 120, 48))
    var.screen.blit(display, (455, 330 ))
    var.screen.blit(display_max_score, (275, 330 ))
    var.score = 0

    while True:
        for event in pygame.event.get():   
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            tap = pygame.mouse.get_pressed()
            if tap[0] == 1:     
                mousepos = pygame.mouse.get_pos()
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP) or (320<=mousepos[0]<=470 and 470<=mousepos[1]<=520):
                    var.game_over = False
                    sg.startGame()
            
        pygame.display.update()
        var.fps_clock.tick(var.framePerSecond)


# Skin Change function
def skinScreen():
    start_button = pygame.transform.scale(pygame.image.load('images/buttons/start_but.png'), (150, 50))

    while True:
        var.screen.blit(var.background, (0,0))
        var.screen.blit(var.skin1, (175,250))
        var.screen.blit(var.skin2, (275,250))
        var.screen.blit(var.skin3, (375,250))
        var.screen.blit(var.skin4, (475,250))
        var.screen.blit(var.firstSkin, (575,250))
        var.screen.blit(start_button, (325,400))
        var.screen.blit(var.skin, (375,150))

        for event in pygame.event.get():   
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                tap = pygame.mouse.get_pressed()
                if tap[0] == 1:
                    mousepos = pygame.mouse.get_pos()
                    if 325<=mousepos[0]<=475 and 400 <= mousepos[1] <= 450:
                        pygame.mixer.music.pause()
                        Play.game()

                    elif 175<=mousepos[0]<=225 and 250 <= mousepos[1] <= 300:
                        var.skin = var.skin1 
                    elif 275<=mousepos[0]<=325 and 250 <= mousepos[1] <= 300:
                        var.skin = var.skin2
                    elif 375<=mousepos[0]<=425 and 250 <= mousepos[1] <= 300:
                        var.skin = var.skin3
                    elif 475<=mousepos[0]<=525 and 250 <= mousepos[1] <= 300:
                        var.skin = var.skin4
                    elif 575<=mousepos[0]<=625 and 250 <= mousepos[1] <= 300:
                        var.skin = var.firstSkin

        pygame.display.update()
        var.fps_clock.tick(30)


# Mini Base
def checkMax(score):
    data = []
    with open("best.txt", 'r+') as f:
        for line in f:
            data.append(float(line))
    if max(float(data[-1]), score) is score:
        with open("best.txt", 'w') as f:
            f.write(str(score))
        return score
    else: return data[-1]
    

# Kill enemies
def killEnemy():
    if var.secondLevel or var.thirdLevel:
        for target in Objects.trigger:
            if pygame.sprite.spritecollideany(target, Objects.bullet):
                pygame.sprite.spritecollideany(target, Objects.bullet).kill()
                var.score += 1
                target.kill()


# Win Window
def winwindow():
    var.screen.blit(var.background, (0, 0))
    winFont = pygame.font.Font(r"front/bionicle-training-card-font-2-4.ttf", 100)
    display = winFont.render('UFF TYAGI', True, (84, 120, 48))
    var.screen.blit(display, (190, 100))

    # Board
    var.screen.blit(var.board, (230, 270))
    restart_button = pygame.transform.scale(pygame.image.load('images/buttons/restart.png'), (190, 50))
    var.screen.blit(restart_button, ( 300, 470 ))
    var.screen.blit(Objects.Base.image, (0, var.baseY))

    # Score render
    max_score = checkMax(var.score)
    scoreFont = pygame.font.Font(r"front/bionicle-training-card-font-2-4.ttf", 40)
    display = scoreFont.render(f"{int(var.score)}", True, (84, 120, 48))
    display_max_score = scoreFont.render(f"{int(max_score)}", True, (84, 120, 48))
    var.screen.blit(display, (455, 330 ))
    var.screen.blit(display_max_score, (275, 330 ))
    var.score = 0

    while True:
        for event in pygame.event.get():   
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            tap = pygame.mouse.get_pressed()
            if tap[0] == 1:     
                mousepos = pygame.mouse.get_pos()
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP) or (320<=mousepos[0]<=470 and 470<=mousepos[1]<=520):
                    var.game_over = False
                    sg.startGame()
            
        pygame.display.update()
        var.fps_clock.tick(var.framePerSecond)


# Create Levels
def createSecondLevel():
    var.secondLevel = True
def createThirdLevel():
    Objects.all_sprites.add(Objects.mario)
    Objects.trigger.add(Objects.mario)



    




    









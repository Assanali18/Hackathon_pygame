import pygame, var, random
from Functions import *
from threading import Timer

class Pipe(pygame.sprite.Sprite):   
    def __init__(self, y_top, y_bottom, image):
        super().__init__()
        self.image = image
        self.y_top = y_top
        self.y_bottom = y_bottom
        self.upperPipes = [
            {'x': var.screenWidth + 200, 'y': y_top}
        ]
        self.lowerPipes = [
            {'x': var.screenWidth + 200, 'y': y_bottom}
        ]
        if self.image == var.imagePipe[0]:
            self.rect = self.image.get_rect(topleft = (self.upperPipes[0]['x'],self.upperPipes[0]['y'] ) )
        else:
            self.rect = self.image.get_rect(topleft = (self.lowerPipes[0]['x'],self.lowerPipes[0]['y'] ))


    def move(self):
        global score
        self.rect.move_ip(-var.scrollSpeed, 0)
        if self.image == var.imagePipe[0]:
            var.screen.blit(self.image, self.rect)
        else:
            var.screen.blit(self.image, self.rect)
        addScore(self.rect.topleft[0])

        if self.rect.left < -self.image.get_width():
            self.kill()



# Get random pipe
def getRandomPipe():
    if var.firstLevel:
        gapY = random.randrange(0, int(var.baseY * 0.65 - var.pipeGap))
        gapY += int(var.baseY * 0.2)
        pipeX = var.screenWidth + 60

        pipes = [
            {'x': pipeX, 'y': gapY - var.pipeHeight},  # upper pipe
            {'x': pipeX, 'y': gapY + var.pipeGap},  # lower pipe
        ]
        return pipes
    elif var.secondLevel:
        gapY = random.randrange(0, int(var.baseY+50))
        pipeX = var.screenWidth + 60

        pipes = [
            {'x': pipeX, 'y': gapY},  # upper pipe
            {'x': pipeX, 'y': gapY},  # lower pipe
        ]
        return pipes

# Create new pipes
def createPipes(newPipe, time_now):
    if var.firstLevel:
        if time_now - var.last_pipe > var.pipe_frequency:
            bottom_pipe = Pipe(newPipe[0]['y'], newPipe[1]['y'], var.imagePipe[1])
            top_pipe = Pipe(newPipe[0]['y'], newPipe[1]['y'], var.imagePipe[0])
            Objects.trigger.add(bottom_pipe)
            Objects.trigger.add(top_pipe)
            Objects.all_sprites.add(bottom_pipe)
            Objects.all_sprites.add(top_pipe)
            var.last_pipe = time_now

# Add score function
def addScore(upperPipes):
    playerMidPos = (Objects.Bird.playerX + Objects.Bird.image.get_width())/2
    pipeMidPos = (upperPipes + Objects.Bird.image.get_width())/2
    if pipeMidPos <= playerMidPos <= pipeMidPos+1 and var.secondLevel == False:
        var.score += 0.5
    # Change speed
    if var.score == 30 :
        var.scrollSpeed = 10
    if var.score ==8:
        var.scrollSpeed = 8

    # Level switch
    if var.secondLevel or var.thirdLevel:
        killEnemy()
    if var.score == 20:
        var.firstLevel = False
        Timer(5, createSecondLevel).start()
    if var.score == 50 and not var.thirdLevel:
        var.secondLevel = False
        Timer(5, createThirdLevel).start()
        var.thirdLevel = True
    

# Create enemies
def createEnemies(newPipe,time_now):
    if time_now - var.last_pipe > 700:
            bottom_pipe = Pipe(newPipe[0]['y'], newPipe[1]['y'], var.imageEnemies)
            Objects.trigger.add(bottom_pipe)
            Objects.all_sprites.add(bottom_pipe)
            var.last_pipe = time_now
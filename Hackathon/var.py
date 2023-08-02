import pygame
# Screen set
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Velocity
framePerSecond = 30
scrollSpeed = 30
fps_clock = pygame.time.Clock()

# Pipes set
pipe_frequency = 1500
pipeGap = screenHeight / 4-45
baseY = screenHeight * 0.75
pipeHeight = 500
pipeWidth = 70
last_pipe = pygame.time.get_ticks()
imagePipe = (
pygame.transform.rotate(pygame.transform.scale(pygame.image.load('images/textures/pipe.png'), (pipeWidth, pipeHeight)), 180),
pygame.transform.scale(pygame.image.load('images/textures/pipe.png'), (pipeWidth,  pipeHeight))
)
imageEnemies = pygame.transform.scale( pygame.image.load('images/enemy.png'), (40, 40))
mario_image = pygame.image.load('images/mario.png')
speedEnemies = 6
score = 0



# Skins
skin = pygame.transform.scale(pygame.image.load('images/bird.png'), (50, 50))
firstSkin = pygame.transform.scale(pygame.image.load('images/bird.png'), (50, 50))
skin1 = pygame.transform.scale(pygame.image.load('images/Skins/skin1.png'), (50, 50))
skin2 = pygame.transform.scale(pygame.image.load('images/Skins/skin2.png'), (50, 50))
skin3 = pygame.transform.scale(pygame.image.load('images/Skins/skin3.png'), (50, 50))
skin4 = pygame.transform.scale(pygame.image.load('images/Skins/skiin4.png'), (50, 50))


# images
background = pygame.transform.scale(pygame.image.load(r'images/textures/bg.png'), (screenWidth, screenHeight))
gameOver = pygame.transform.scale(pygame.image.load('images/tittles/gameOver.png'), (400, 100))
board = pygame.image.load('images/tittles/board.png')

# levels
firstLevel = True
secondLevel = False
thirdLevel = False
import pygame, var
class Base(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.baseX = 0
        self.image = pygame.transform.scale(pygame.image.load('images/textures/ground.png'), (var.screenWidth*2, 300) ) 
        self.rect = self.image.get_rect(topleft = (self.baseX, var.baseY))
        
    def move(self):
        var.screen.blit(self.image, self.rect)
        self.rect.move_ip(-var.scrollSpeed, 0)
        if abs(self.rect.left) > var.screenWidth:
            self.rect.topleft = (0,var.baseY)

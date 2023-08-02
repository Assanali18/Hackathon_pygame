import pygame, var, Objects
from Bullet import Bullet


class Mario(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.mario_image = var.mario_image
        self.rect = self.mario_image.get_rect(topleft =(600, 300) )
        self.direct = True

    def move(self):
        if self.direct:
            self.rect.move_ip(0, -6)
            if -5<= self.rect.top <=5:
                self.direct = False
        if not self.direct:
            self.rect.move_ip(0, 6)
            if  var.screenHeight-160 <= self.rect.top:
                self.direct = True

        # Create bullets of Mario
        bulletMario()

        # Check collideany of Mario and bird's bullets
        if pygame.sprite.spritecollideany(Objects.mario, Objects.bullet):
                var.score += 1
                pygame.sprite.spritecollideany(Objects.mario, Objects.bullet).kill()
        var.screen.blit(self.mario_image, self.rect)


# Function of collideany
def bulletMario():
    if Objects.mario.rect.top-25 in range(Objects.Bird.rect.top-10, Objects.Bird.rect.bottom+10):
        Objects.bullet_mario = Bullet(Objects.mario.rect.topleft[0], Objects.mario.rect.top+15, -15)
        Objects.all_sprites.add(Objects.bullet_mario)
        # Objects.bullet_mario.add(Objects.bullet_mario)
        Objects.trigger.add(Objects.bullet_mario)
        
        
        
        

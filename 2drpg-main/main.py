#import
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

#window
win_width = 800
win_height = 600
window = display.set_mode((win_width, win_height))

#image
background = display.set_mode((win_width, win_height))

#fps
background = scale(load('background.jpg'), (win_width, win_height))
clock = time.Clock()
FPS = 60




#GameSprite + класи
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = scale(load(player_image), (player_width, player_height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed



#objects
ground = GameSprite('background.jpg', 0, 560, 800, 110, 0)


mplayer = Player('mplayer.png', 200, 490, 80, 70, 5)            



#Ігровий цикл
run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False


    if not finish:
        
        
        window.blit(background,(0, 0))


        mplayer.reset()
        mplayer.update()

        if not sprite.collide_rect(mplayer, ground):
            mplayer.rect.y += 1












        display.update()
        clock.tick(FPS)

'''
Alien Invasion
Ethan Mason
11/11
this code is respnsible for making the bullet that is fried from arsenal as well as controlling bullet speed and direction
'''
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion'):
        super().__init__()
        
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.rotate(pygame.transform.scale(self.image, 
            (self.settings.bullet_w, self.settings.bullet_h)
            ),-90)
        
        self.rect = self.image.get_rect()
        self.rect.midleft = game.ship.rect.midright
        self.y = float(self.rect.y)

    def update(self):
        self.rect.x += self.settings.bullet_speed

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
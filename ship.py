'''
Alien Invasion
Ethan Mason
11/11
this code is responsible for placing the ship on screen as well as what boundries it has with movement and size
'''
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    #all code for the ship being on screen as well as its movements and boundries
    
    
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.rotate(pygame.transform.scale(self.image, 
            (self.settings.ship_w,self.settings.ship_h)
            ), -90)
        
        self.rect = self.image.get_rect()
        self.rect.midleft = self.boundries.midleft
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
        self.arsenal = arsenal

    def update(self) -> None:
        # updating the position of the ship
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        #puts ship speed in control of the setting its assigned to as well as limits the ship to boundries
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.top > self.boundries.top:
            self.rect.y -= temp_speed
        if self.moving_left and self.rect.bottom < self.boundries.bottom:
            self.rect.y += temp_speed


    def draw(self) -> None:
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        return self.arsenal.fire_bullet()
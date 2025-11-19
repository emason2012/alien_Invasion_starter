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
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_w,self.settings.ship_h)
            )
        self.image = pygame.transform.rotate(self.image, 90)
        
        self.rect = self.image.get_rect()
        self._center_ship()
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def _center_ship(self):
        self.rect.midright = self.boundries.midright
        self.y = float(self.rect.y)

    def update(self) -> None:
        # updating the position of the ship
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        temp_speed = self.settings.ship_speed
    
        if self.moving_right and self.rect.top > self.boundries.top:
            self.y -= temp_speed

        if self.moving_left and self.rect.bottom < self.boundries.bottom:
            self.y += temp_speed

        self.rect.y = self.y

    def draw(self) -> None:
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_groups):
        if pygame.sprite.spritecollideany(self, other_groups):
            self._center_ship()
            return True
        return False
    
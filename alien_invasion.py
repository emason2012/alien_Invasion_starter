'''
Alien Invasion
Ethan Mason
11/11
this code is respnsible for running the game Alien Invasion in which you are a rocket ship shootingat the different aliens coming down towards you on the screen
'''

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal

class AlienInvasion:
    #controls base functions of the game such as display, sounds, and fps
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
        (self.settings.screen_w,self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        self.ship = Ship(self, Arsenal(self))
    
    
    def run_game(self) -> None:
        #Game Loop
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self) -> None:
        #updates the screen for ship location
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self) -> None:
        #does initial check for any input from a keyboard such as q to quit or arrow keys for moveement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keyup_events(self, event) -> None:
        #checks for when a key is lifted after beubg pressed/ not being pressed
        if event.key == pygame.K_UP:
            self.ship.moving_right = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_left = False


    def _check_keydown_events(self, event) -> None:
        #checks for when a key is pressed down
        if event.key == pygame.K_UP:
            self.ship.moving_right = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

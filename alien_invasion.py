import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        '''Initialize the game and create its resources'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.fullscreen_status = 1
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)

    def run_game(self):
        '''Start the main loop of the game'''
        while True:
            self._check_events()            
            self._update_screen()
            self.ship.update()
            self.clock.tick(60)
    
    def _check_events(self):
        '''Responds to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)                    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events (event)                       

    def _check_keydown_events(self,event):
        """ Respond to keypresses """                
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit    
        elif event.key == pygame.K_f:
            self._toggle_fullscreen()
    def _check_keyup_events(self, event):
        """ Responding to keyreleases """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _toggle_fullscreen(self):
        self.fullscreen_status *= -1
        if self.fullscreen_status == 1:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), pygame.RESIZABLE)
        if self.fullscreen_status == -1:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height

    def _update_screen(self):
        '''Update images on screen and flip to the new screen'''
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()


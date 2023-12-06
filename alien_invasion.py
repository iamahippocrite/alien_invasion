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

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        

    def run_game(self):
        '''Start the main loop of the game'''
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit
            
            #Redraw the screen each pass of the loop
            self.screen.fill(self.settings.bg_colour)
            self.ship.blitme()

            #Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()


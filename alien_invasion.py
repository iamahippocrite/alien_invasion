import pygame

import sys


class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        '''Initialize the game and create its resources'''
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        '''Start the main loop of the game'''
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit
            #Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
    
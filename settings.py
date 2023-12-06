class Settings:
    '''A class to store all the settings of Alien Invasion'''

    def __init__(self) -> None:
        '''Initialize the games settings'''
        #Screen settings
        self.screen_width = 1200 #Default is 1200
        self.screen_height = 800 #Default is 800
        self.bg_colour = (230, 230, 230) #Default is (230, 230, 230)

        #Ship settings
        self.ship_speed = 5 #Default is 1.5        
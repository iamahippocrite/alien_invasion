"""This is a module for the Settings Class."""


class Settings:
    """A class to store all the settings of Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the games settings."""
        # Screen settings
        self.screen_width = 1920  # Default is 1200
        self.screen_height = 1080  # Default is 800
        self.bg_colour = (230, 230, 230)  # Default is (230, 230, 230)

        # Ship settings
        self.ship_speed = 10  # Default is 1.5

        # Bullet settings
        self.bullet_speed = 12.0  # Default is 2.0
        self.bullet_width = 15  # Default is 3
        self.bullet_height = 30  # Default is 15
        self.bullet_colour = (98, 11, 40)  # Default is (60, 60, 60)
        self.bullets_allowed = 3  # Default is 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

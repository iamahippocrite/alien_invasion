"""This module is for the class GameStats."""


class GameStats:
    """Tracks statistics for Alien Invasion."""

    def __init__(self, ai_game) -> None:
        """Initialize Statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Reset the stats that can change during the game."""
        self.ships_left = self.settings.ship_limit

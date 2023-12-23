#Creator: Israel Showell
#Date: 12-22-2023
#Project: Alien Invasion Game

class GameStats():

    """Tracks stats for Alien Invasion"""

    def __init__(self, game_settings):
        """Initialize stats"""
        self.game_settings = game_settings
        self.reset_stats()

        #High Score, doesn't get reset
        self.high_score = 0

        #Starts the game in an inactive mode
        self.game_active = False

    def reset_stats(self):
        """Initialize stats that can change during the game."""
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
        self.level = 1




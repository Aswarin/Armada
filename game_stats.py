class GameStats():
    """Track game stats such as player lives and score"""

    def __init__(self, game_settings):
        """initialise statistics"""
        self.game_active = False
        self.game_settings = game_settings
        self.reset_stats()
        self.score = 0
        self.high_score = 0
        self.level = 1


    def reset_stats(self):
        """initialise all statistics that may change during a game"""
        self.player_lives = self.game_settings.ship_lives
class Settings():
    """A class to store all settings for alien attack."""

    def __init__(self):
        """initialise the game's settings."""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        #player ship settings
        self.ship_lives = 2

        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullet_limit = 3

        #alien settings
        self.alien_descend_speed = 10
        self.alien_points = 50
       

        #speed up factor after every level
        self.speed_increase = 1.1

        self.initialize_dynamic_settings()

    
    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed = 2.5
        self.bullet_speed = 4
        self.alien_speed = 1
        self.alien_direction = 1
        self.score_increase = 1.5


    def increase_speed(self):
        """increase speed settings"""
        self.ship_speed *= self.speed_increase
        self.bullet_speed *= self.speed_increase
        self.alien_speed *= self.speed_increase
        self.alien_points = int(self.score_increase * self.alien_points)
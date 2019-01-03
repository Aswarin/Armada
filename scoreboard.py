import pygame.font
from pygame.sprite import Group
from player_ship import Ship

class Scoreboard():
    """A class to store and show the scoring information"""

    def __init__(self, game_settings, screen, stats):
        """create scorekeeping variables"""
        self.screen = screen
        self.game_settings = game_settings
        self.stats = stats
        self.screen_rect = screen.get_rect()
        
        #font settings for scores
        self.text_colour = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #prepare initial score
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives()


    def prep_score(self):
        """turn score into a rendered image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_colour, 
            self.game_settings.bg_colour)
            
        #Display score at top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        """Turn the highscore into a rendered image"""
        high_score = int(self.stats.high_score)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_colour, self.game_settings.bg_colour)

        #center the highscore at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def show_score(self):
        """Draw the score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)


    def prep_level(self):
        """Turn the level into a rendered image"""
        self.level_image = self.font.render(str(self.stats.level), True,
            self.text_colour, self.game_settings.bg_colour)

        #position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_lives(self):
        """Show how many ships aare left"""
        self.ships = Group()
        for ship_number in range(self.stats.player_lives):
            ship = Ship(self.game_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represetn one alien in the fleet"""

    def __init__(self, game_settings, screen):
        """create the alien and its starting position"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        #load the image and create a rectangle for it
        self.image = pygame.image.load('images/alien_image.png')
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 

        #store the aliens exact position
        self.x = float(self.rect.x)


    def blitme(self):
        """Draw the alien at it's current location"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """move the alien right"""
        self.x += (self.game_settings.alien_direction * self.game_settings.alien_speed)
        self.rect.x = self.x

    def check_edges(self):
        """Return true if an alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True

            



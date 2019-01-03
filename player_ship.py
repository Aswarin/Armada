import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, game_settings, screen):
        """create the ship and its starting position"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        #load the ship image and its rectangle (rect)
        self.image = pygame.image.load('images/player_ship_image.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #movement flag to detect whether to stop moving
        self.moving_right = False
        self.moving_left = False

        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store a decimal value for the ships center
        self.center = float(self.rect.centerx)

    def update(self):
        """update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed

        #update the rectangle from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """center the ship after dying"""
        self.center = self.screen_rect.centerx

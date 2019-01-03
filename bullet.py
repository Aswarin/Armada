import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    
    def __init__(self, game_settings, screen, ship):
        """create a bullet object at the ships current position"""
        super().__init__()
        self.screen = screen

        #create a bullet at position (0, 0) then set the correct position
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width,
            game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store the bullets position as a float
        self.y = float(self.rect.y)

        self.colour = game_settings.bullet_colour
        self.speed = game_settings.bullet_speed

    
    def update(self):
        """move the bullet"""
        #move the float value of the bullet
        self.y -=self.speed
        #update the rect postion
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)
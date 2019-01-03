import pygame.font

class Button():

    def __init__(self, game_settings, screen, message):
        """create the button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #set the dimensions of the button and colour of the button
        self.width, self.height = 250, 50
        self.button_colour = (0,0,128)
        self.text_colour = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        #build the buttons rectangular object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #the button's message
        self.prepare_message(message)


    def prepare_message(self, message):
        """Turn the message into a rendered image and place it on the button"""
        self.message_image = self.font.render(message, True, self.text_colour,
            self.button_colour)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center


    def draw_button(self):
        """Draw a blank button then add the message"""
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)
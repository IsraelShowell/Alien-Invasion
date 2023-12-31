#Creator: Israel Showell
#Date: 12-23-2023
#Project: Alien Invasion Game

import pygame.font


class Button():

    def __init__(self, game_settings, screen, msg):
        """Initialize the button's attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #Set dimensions and properties of the button
        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('calibri', 48)

        #Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #Button message is prepared once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turns msg into a rendered image and centers the text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        #Draws a blank button and then the message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
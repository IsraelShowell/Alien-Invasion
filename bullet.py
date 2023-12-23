#Creator: Israel Showell
#Date: 12-20-2023
#Project: Alien Invasion Game



import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, game_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        #Creates a bullet rectangle at (0,0) and then sets the correct position
        #This builds a rectangle from scratch since the bullet isn't based on a image
        self.rect = pygame.Rect(0,0,game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        #Sets the bullet color and speed to match those saved in the settings.py module
        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor


    def update(self):
        """Moves the bullet up the screen"""
        #Updates the decimal position of the bullet
        self.y -= self.speed_factor

        #Updates the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

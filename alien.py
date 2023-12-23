#Creator: Israel Showell
#Date: 12-22-2023
#Project: Alien Invasion Game

import pygame

from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, game_settings, screen):
        """Initialize the alien and set its starting position"""

        super(Alien, self).__init__()
        self.screen = screen

        #The alien's screen is now equal to the imported screen
        self.screen = screen

        #Pretty much says, the alien's game settings, are now equal to the game_settings in the parameters
        self.game_settings = game_settings

        #Imports the image of the alien
        self.image = pygame.image.load('Images/alien.bmp')

        #The alien's rectangle is now the same shape as the image's size
        self.rect = self.image.get_rect()
    
        #Starts each alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Stores values for alien's exact position
        self.center = float(self.rect.centerx)



    def blitme(self):

        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return true if alien has it an edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move alien to the right"""
        self.x += (self.game_settings.alien_speed_factor * self.game_settings.fleet_direction)
        self.rect.x = self.x





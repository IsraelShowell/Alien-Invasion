#Creator: Israel Showell
#Date: 12-19-2023
#Project: Alien Invasion Game

import pygame

from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, game_settings, screen):

        """Initalize the ship and set its starting position (pos)"""
        super(Ship, self).__init__()
        #The ship's screen is now equal to the imported screen
        self.screen = screen

        #Pretty much says, the ship's game settings, are now equal to the game_settings in the parameters
        self.game_settings = game_settings

        #Imports the image of the ship
        self.image = pygame.image.load('Images/ship.bmp')

        #The ships rectangle is now the same shape as the image's size
        self.rect = self.image.get_rect()

        #The ships's screen rectangle is given the parameter screen's rectangle size
        self.screen_rect = screen.get_rect()
    
        #Stores values for ship's center
        self.center = float(self.rect.centerx)

        #Movement flag
        self.moving_right = False
        self.moving_left = False
      #  self.moving_up = False
      #  self.moving_down = False

        

        #Spawn each new ship at the bottom left of the screen
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom



    def update(self):
        """Update ship's position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor

        #I figured moving the ship up within the bounds of the screen myself
        #This allows the player to go up to halfway of the screen
        #if self.moving_up and self.rect.top > (self.game_settings.screen_h / 2):
        #if self.moving_up and self.rect.top > self.game_settings.screen_h:
         #   self.rect.centery -= self.game_settings.ship_speed_factor

        #I figured moving the ship down within the bounds of the screen myself
        #if self.moving_down and self.rect.bottom < self.game_settings.screen_h:
         #   self.rect.centery += self.game_settings.ship_speed_factor
        
        #Stores the integer part of self.center and is used to display the ship
        self.rect.centerx = self.center

    def blitme(self):

        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centers the ship on the screen"""
        self.center = self.screen_rect.centerx


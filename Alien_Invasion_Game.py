#Creator: Israel Showell
#Date: 12-19-2023
#Project: Alien Invasion Game

import sys

import pygame

from settings import Settings

from ship import Ship

from alien import Alien

from button import Button

from scoreboard import Scoreboard

import game_functions as gf

from pygame.sprite import Group

from game_stats import GameStats

def run_game():

    #Initializes the game, settings, and ship
    pygame.init()

    #Creates an instance of the Settings class in settings.py
    game_settings = Settings()

    #Creates a screen object, w is for width, and h is for height.
    screen = pygame.display.set_mode((game_settings.screen_w, game_settings.screen_h))

    #Sets the screen's name
    pygame.display.set_caption("Alien Invasion")

    #Makes the play button
    play_button = Button(game_settings, screen, "Play")

    #Creates ship after screen is made
    ship = Ship(game_settings, screen)

    #Creates a group to store the bullets in
    bullets = Group()
    
    #Creates a group to store the aliens in
    aliens = Group()

    #Creates a fleet of aliens
    gf.create_fleet(game_settings, screen, ship, aliens)

    #Creates an instance of to store game statistics
    stats = GameStats(game_settings)

    #Creates an instance of Scoreboard to track scores
    sb = Scoreboard(game_settings, screen, stats)

    #Main Loop of the Game
    while True:
        gf.check_events(game_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(game_settings, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(game_settings, screen, ship, aliens, bullets, stats, sb, play_button)


run_game()

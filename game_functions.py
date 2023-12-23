#Creator: Israel Showell
#Date: 12-19-2023
#Project: Alien Invasion Game


import sys

import pygame

from bullet import Bullet

from alien import Alien

from time import sleep

def check_events(game_settings, screen, stats, sb, play_button, ship, aliens, bullets):
     """Checks for events from mouse and keyboard"""
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
              sys.exit()
         elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)
         elif event.type == pygame.KEYUP:
             check_keyup_events(event, ship)
         elif event.type == pygame.MOUSEBUTTONDOWN:
             mouse_x, mouse_y = pygame.mouse.get_pos()
             check_play_button(game_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(game_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Starts a new game when the player clicks play"""

    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:

        #Hides the mouse cursor, resets the stats, and sets the game state to active
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        #Resets the game settings
        #game_settings.initialize_dynamic_settings()

        #Reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #Empty the lists for aliens and bullets
        aliens.empty()
        bullets.empty()

        #Create a new fleet and center the ship
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship


def check_keydown_events(event, game_settings, screen, ship, bullets):
    """Checks for keydown events from the user"""
    if event.key == pygame.K_RIGHT:
         ship.moving_right = True
    elif event.key == pygame.K_LEFT:
         ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

   # if event.key == pygame.K_UP:
   #      ship.moving_up = True
    #elif event.key == pygame.K_DOWN:
    #     ship.moving_down = True
    if event.key == pygame.K_SPACE:
        fire_bullets(game_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """Checks for keyup events from the user"""
    if event.key == pygame.K_RIGHT:
         ship.moving_right = False
    elif event.key == pygame.K_LEFT:
         ship.moving_left = False

    if event.key == pygame.K_UP:
         ship.moving_up = False
    elif event.key == pygame.K_DOWN:
         ship.moving_down = False

def update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets):
    """Updates position of bullets and removes old bullets"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    #Calls function to check collisions
    check_bullet_alien_collisions(game_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(game_settings, screen, stats, sb, ship, aliens, bullets):
    """Responds to alien bullet collisions"""

    #Checks for bullets that have hit any aliens
    #If so, delete both alien and bullet
    #So this is saying, what 2 sprites am I trying to detect, and should I delete the first one you gave me and the second one
    #Using this idea, I will try and make a super bullet power-up
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    #Checks for collisions and adds to the score
    if collisions:
        for aliens in collisions.values():
            stats.score += game_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_scores(stats, sb)

    if len(aliens) == 0:
        #Destroys existing bullets, speeds up the game, and creates a new fleet
        bullets.empty()
        game_settings.increase_speed()

        #Increases the level
        stats.level += 1
        sb.prep_level()

        create_fleet(game_settings, screen, ship, aliens)


def update_screen(game_settings, screen, ship, aliens, bullets, stats, sb, play_button):

    #Redraws screen after each pass of the loop
        screen.fill(game_settings.bg_color)

        #Redraws all bullets behind ship and aliens
        for bullet in bullets.sprites():
            bullet.draw_bullet()

        #Draws the ship and alien(s) at its current position
        ship.blitme()
        aliens.draw(screen)

        sb.show_score()

        if not stats.game_active:
            play_button.draw_button()

        #Makes the most recently drawn screen visible
        pygame.display.flip()


def fire_bullets(game_settings, screen, ship, bullets):
    if len(bullets) < game_settings.bullets_allowed:
            new_bullet = Bullet(game_settings, screen, ship)
            bullets.add(new_bullet)

def get_number_of_aliens_x_axis(game_settings, alien_width):
    """Determine number of aliens that fit in a row"""
    available_space_x_axis = game_settings.screen_w - (2 * alien_width)
    number_of_aliens_x_axis = int(available_space_x_axis / (2 * alien_width))
    return number_of_aliens_x_axis

def get_number_rows(game_settings, ship_height, alien_height):
    """Determines the number of rows that can fit on the screen"""
    available_space_y = (game_settings.screen_h - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows

def create_alien(game_settings, screen, aliens, alien_number, row_number):
    
    #Create an alien and find the number of aliens in a row
    #Spacing between each alien is equal to one alien width
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width) * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(game_settings, screen, ship, aliens):
    """Creates a full fleet of aliens"""
    alien = Alien(game_settings, screen)
    number_of_aliens_x_axis = get_number_of_aliens_x_axis(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)

    #Creates the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_of_aliens_x_axis):
            create_alien(game_settings, screen, aliens, alien_number, row_number)
 
            
def ship_hit(game_settings, stats, sb, screen, ship, aliens, bullets):
    """Responds to ship being hit by alien"""
    if stats.ships_left > 0:

        #Decrement ships_left
        stats.ships_left -= 1

        #Update the ship scoreboard
        sb.prep_ships

        #Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()


        #Create a new fleet and center the ship
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()

        #Pause
        sleep(0.5)
    else:
         stats.game_active = False
         pygame.mouse.set_visible(True)
         #stats.score = 0
         #sb.stats.score = 0

def update_aliens(game_settings, stats, sb, screen, ship, aliens, bullets):
    """Checks if fleet is at an edge, and updates all positions of the alien fleet"""
    check_fleet_edges(game_settings, aliens)
    aliens.update()

    #Checks to see if any aliens are at the bottom of the screen
    check_aliens_bottom(game_settings, stats, sb, screen, ship, aliens, bullets)

    #Looks for alien and ship collisons 
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, stats, sb, screen, ship, aliens, bullets)
        print("Ship hit!")
    check_aliens_bottom(game_settings, stats, sb, screen, ship, aliens, bullets)

def check_fleet_edges(game_settings, aliens):
    """Respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break


def change_fleet_direction(game_settings, aliens):
    """Makes the entire fleet drop down and change direction"""
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1


def check_aliens_bottom(game_settings, stats, sb, screen, ship, aliens, bullets):
    """Checks if any aliens have reached the bottom"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(game_settings, stats, sb, screen, ship, aliens, bullets)
            break



def check_high_scores(stats, sb):
    """Checks to see if there is a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
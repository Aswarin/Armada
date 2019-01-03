import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_events(game_settings, screen, stats, score, play_button, ship, aliens, bullets):
    """Respond to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_events_check(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            keyup_events_check(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, screen, stats, score, play_button, ship,
                aliens, bullets, mouse_x, mouse_y)


def check_play_button(game_settings, screen, stats, score, play_button, ship, aliens, 
        bullets, mouse_x, mouse_y):
    """start a new game when the player clicks play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #reset the game settings
        game_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        #reset the game stats
        stats.reset_stats()
        stats.game_active = True
        #reset the score
        score.prep_score()
        score.prep_high_score()
        score.prep_level()
        score.prep_lives()
        #empty all aliens and bullets
        aliens.empty()
        bullets.empty()
        #create a new fleet and center the ship
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()


def keydown_events_check(event, game_settings, screen, ship, bullets):
    """respond to key presses"""
    if event.key == pygame.K_RIGHT:
        #move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #move the ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)


def keyup_events_check(event, ship):
    """respond to key releases"""
    if event.key == pygame.K_RIGHT:
         ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def fire_bullet(game_settings, screen, ship, bullets):
    #create a new bullet and add it to the bullets group
    if len(bullets) < game_settings.bullet_limit:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)        


def update_screen(game_settings, screen, stats, score, ship, aliens, bullets, play_button):
    """update images on the screen and flip (update) to the new screen"""
    screen.fill(game_settings.bg_colour)
    #redraw all bullets behind the ship and enemies
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    score.show_score()
    #display the play button if the game isn't active
    if not stats.game_active:
        play_button.draw_button()
    #make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(game_settings, screen, stats, score, ship, aliens, bullets):
    """update position and get rid of bullets that have left the screen"""
    #update bullet positions.
    bullets.update()
    #check if a collision happens between an alien and a bullet if True remove both
    if len(aliens) == 0:
        #Destroy all bullets, speed up the game and create a new fleet.
        bullets.empty()
        game_settings.increase_speed()
        create_fleet(game_settings,screen, ship, aliens)
        stats.level += 1
        score.prep_level()
    #get rid of bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(game_settings, screen, stats, score, ship, aliens, bullets)


def check_bullet_alien_collision(game_settings, screen, stats, score, ship, aliens, bullets):
    """respond to any collisions between aliens and bullets"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += game_settings.alien_points * len(aliens)
            score.prep_score()
            check_high_score(stats, score)


def create_fleet(game_settings, screen, ship, aliens):
    """create the fleet of attacking aliens"""
    #create the alien fleet
    alien = Alien(game_settings, screen)
    number_of_aliens_x = get_number_of_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_of_alien_rows(game_settings, ship.rect.height, alien.rect.height)
    #create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_of_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)


def get_number_of_aliens_x(game_settings, alien_width):
    """calculate the number of aliens that will go along the x axis"""
    available_xspace = game_settings.screen_width - 2 * alien_width
    number_of_aliens_x = int(available_xspace / (2 * alien_width))
    return number_of_aliens_x


def create_alien(game_settings, screen, aliens, alien_number, row_number):
    """create an alien and add it to the row"""
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1.5 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_of_alien_rows(game_settings, ship_height, alien_height):
    """determine the number of aliens rows that will fit on the screen"""
    available_space_y = (game_settings.screen_height - (3 * alien_height) - ship_height)
    number_of_rows = int(available_space_y / (2 * alien_height))
    return number_of_rows


def ship_hit(game_settings, screen, stats, score, ship, aliens,bullets):
    """respond to the ship being hit"""
    if stats.player_lives > 0:
        #player loses a life
        stats.player_lives -=1
        score.prep_lives()
        #empty all bullets and aliens (reset the game)
        aliens.empty()
        bullets.empty()
        #create new aliens and center the ship
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()
        #pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(game_settings, screen, stats, score, ship, aliens, bullets):
    """update the position of all aliens"""
    check_alien_edges(game_settings, aliens)
    check_alien_bottom(game_settings, screen, stats, score, ship, aliens, bullets)
    aliens.update()
    #check if an alien hits the player ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, screen, stats, score, ship, aliens, bullets)
        print("Your ship has been hit!")


def check_alien_edges(game_settings, aliens):
    """respond if they aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_alien_direction(game_settings,aliens)
            break


def change_alien_direction(game_settings, aliens):
    """drop the aliens and change their direction"""
    for alien in aliens.sprites():
        alien.rect.y += game_settings.alien_descend_speed
    game_settings.alien_direction *= -1


def check_alien_bottom(game_settings, screen, stats, score, ship, aliens, bullets):
    """check if aliens have reached the bottom of the screen and act accordingly"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #act as though it was hit
            ship_hit(game_settings, screen, stats, score, ship, aliens, bullets)
            break           


def check_high_score(stats, score):
    """check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.prep_high_score()
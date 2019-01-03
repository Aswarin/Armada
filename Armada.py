import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from player_ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    #initialise game, settings and screen object
    pygame.init()
    game_settings = Settings()
    stats = GameStats(game_settings)
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Armada!")
    score = Scoreboard(game_settings, screen, stats)

    #play button
    play_button = Button(game_settings, screen, "Press to Play!")

    #Make a ship
    ship = Ship(game_settings, screen)

    #make a group to store the bullets and another to store the alien fleet
    bullets = Group()
    aliens = Group()

    #make an alien
    gf.create_fleet(game_settings, screen, ship, aliens)
    
    #main loop for the game
    while True:

        #checking for events
        gf.check_events(game_settings, screen, stats, score, play_button, ship, aliens, bullets)

        if stats.game_active:
            #update the ship position after checking events 
            ship.update()
            gf.update_bullets(game_settings, screen, stats, score, ship, aliens, bullets)

            #update the aliens to make them move
            gf.update_aliens(game_settings, screen, stats, score, ship, aliens, bullets)

        #update the screen and make the newly updated screen visible
        gf.update_screen(game_settings, screen, stats, score, ship, aliens, bullets,
            play_button)




run_game()
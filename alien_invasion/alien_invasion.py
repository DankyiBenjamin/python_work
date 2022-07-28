import pygame
from pygame.sprite import Group
from settings import Settings
from ship1 import Ship1
import game_functions as gf

def run_game():
	# Initialize pygame,settings, and screen object.

	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	# Make a ship
	ship = Ship1(ai_settings,screen)
	bullets = Group()

	# Start the main loop for the game
	while True:
		# watch for keyboard and mouse events.
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		# to verify that the bullects are actually being removed
		#  print the remaining bullects to the screen
		# print(len(bullets))
		gf.update_screen(ai_settings,screen,ship, bullets)


run_game()
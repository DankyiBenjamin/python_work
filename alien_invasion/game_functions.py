import sys

import pygame
from bullet import Bullet


def check_keydown_events(event,ai_settings, screen,ship, bullets):
	""" Respond to keypresses"""
	if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
		# Move the ship to the right.
		ship.moving_right = True
	elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
		# Move the ship to the left
		ship.moving_left = True
	elif event.key == pygame.K_UP or event.key == pygame.K_w:
		# Move the ship up
		ship.moving_up = True
	elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
		# Move the ship down
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
		

def fire_bullet(ai_settings,screen,ship,bullets):
	""" Fire bullet if limit is not reached """
	# Create a new bullet and add it to the bullets group.
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen,ship)
		bullets.add(new_bullet)



def check_keyup_events(event,ship):
	# Respond to key releases
	if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
		ship.moving_right = False
	if event.key == pygame.K_LEFT or event.key == pygame.K_a:
		ship.moving_left = False
	if event.key == pygame.K_UP or event.key == pygame.K_w:
		# Stop the movement of the rocket
		ship.moving_up = False
	if event.key == pygame.K_DOWN or event.key == pygame.K_s:
		ship.moving_down = False


def check_events(ai_settings,screen,ship,bullets):
	""" Respond to keypresse and mouse events. """
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event , ai_settings, screen, ship, bullets)
				
			elif event.type == pygame.KEYUP:
				check_keyup_events(event,ship)
				




def update_screen(ai_settings,screen,ship,bullets):
	""" Update images onthe screen and flip to the new screen."""

	

	# Redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	# Redraw all bullets behind the ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()

	# Make the most recently drawn screen visible
	pygame.display.flip()
	

def update_bullets(bullets):
	""" Update the position of old bullets and get rid of old bullets """
	# Update bullet position
	bullets.update()

	# Get rid of bullets that disappears
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)


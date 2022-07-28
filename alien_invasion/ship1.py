import pygame

class Ship1():

	def __init__(self,ai_settings,screen):
		""" Initialize the ship and set its starting position"""
		self.screen = screen
		self.ai_settings = ai_settings

		# load the ship image nd get its rect
		self.image = pygame.image.load('images/rocket_640.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		self.rect.bottom = self.screen_rect.bottom

		# Store a decimal value for the ship,s center
		self.center = float(self.rect.centerx)
		self.centerup = float(self.rect.centery)
		# Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		


	def update(self):
		""" Update the ship movement based on the movement flag."""
		# Update the ship's center value, not the rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > 0:
			# Check if the rect is near the upper edge of the screen and stop it
			self.centerup -= self.ai_settings.ship_speed_factor
			
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			# Use this if statement to check if the rect is near the bottom edge 
			# And stop it
			self.centerup += self.ai_settings.ship_speed_factor


		# Update rect object from self.center
		self.rect.centerx = self.center 
		self.rect.centery =self.centerup



	def blitme(self):
		""" Draw the ship at the current position."""
		self.screen.blit(self.image,self.rect)
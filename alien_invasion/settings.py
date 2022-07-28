class Settings():
	""" A class to store all settings for Alien Invasion."""

	def __init__(self):
		""" Initialize the game's settings"""
		# Screen settings
		self.screen_width = 1100
		self.screen_height = 700
		self.bg_color = (135, 206, 230)
		# ship setting
		self.ship_speed_factor = 2.5


		# Bullet settings
		self.bullet_speed_factor = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3


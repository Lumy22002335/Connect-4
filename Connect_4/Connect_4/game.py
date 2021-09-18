import pygame
from button import Button

class Game:
	def __init__(self):
		self.quit = False

	def render(self, screen):
		screen.fill((20, 40, 0))

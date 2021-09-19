import pygame
from button import Button

class Game:
	def __init__(self):
		self.quit = False

		self.red_chip = pygame.image.load("Red_Chip.png")
		self.yellow_chip = pygame.image.load("Yellow_Chip.png")

		self.back_button = Button((-25, 405), (215, 67), pygame.image.load("Back_Default.png"), pygame.image.load("Back_Highlight.png"), lambda: self.back())

	def render(self, screen):
		screen.fill((40, 20, 0))
		self.back_button.draw(screen)

	def event_handler(self, event):
		if event.type == pygame.MOUSEBUTTONUP:
			if self.back_button.rect.collidepoint(event.pos):
				self.back_button.on_click()

		else:
			self.back_button.event_handler(event)

	def back(self):
		self.quit = True

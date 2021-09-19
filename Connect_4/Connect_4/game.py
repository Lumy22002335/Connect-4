import pygame
from button import Button

class Game:
	def __init__(self):
		self.quit = False

		self.red_chip = pygame.image.load("Red_Chip.png")
		self.yellow_chip = pygame.image.load("Yellow_Chip.png")

		self.back_button = Button((-25, 405), (215, 67), pygame.image.load("Back_Default.png"), pygame.image.load("Back_Highlight.png"), lambda: self.back())

		self.turn = 1

		self.grid_start = (206, 35)

		self.grid = []
		for y in range(0, 6):
			row = []
			for x in range(0, 7):
				row.append(0)
			self.grid.append(row)

	def render(self, screen):
		screen.fill((40, 20, 0))
		self.back_button.draw(screen)

		draw_y = self.grid_start[1]
		for y in range(0, 6):
			draw_x = self.grid_start[0]
			for x in range(0, 7):
				pygame.draw.rect(screen, (255, 255, 255), (draw_x, draw_y, 64, 64), 2)
				draw_x += 64
			draw_y += 64

	def event_handler(self, event):
		if event.type == pygame.MOUSEBUTTONUP:
			if self.back_button.rect.collidepoint(event.pos):
				self.back_button.on_click()

		else:
			self.back_button.event_handler(event)

	def back(self):
		self.quit = True

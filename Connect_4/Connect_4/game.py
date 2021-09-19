import pygame
from button import Button

class Game:
	def __init__(self):
		self.quit = False

		self.red_chip = pygame.image.load("Red_Chip.png")
		self.yellow_chip = pygame.image.load("Yellow_Chip.png")

		self.back_button = Button((-25, 405), (215, 67), pygame.image.load("Back_Default.png"), pygame.image.load("Back_Highlight.png"), lambda: self.back())

		self.turn = 1

		self.mouse_grid_pos = (0, 0)

		self.grid_start = (206, 35)

		self.grid = []
		for y in range(0, 6):
			row = []
			for x in range(0, 7):
				row.append(0)
			self.grid.append(row)

	def get_free_tile(self, x):
		for y in range(5, -1, -1):
			if self.grid[y][x] == 0:
				return y

	def render(self, screen):
		screen.fill((40, 20, 0))
		self.back_button.draw(screen)

		draw_y = self.grid_start[1]
		for y in range(0, 6):
			draw_x = self.grid_start[0]
			for x in range(0, 7):
				if self.mouse_grid_pos[0] == x and self.get_free_tile(x) == y:
					if self.mouse_grid_pos[1] >= 0 and self.mouse_grid_pos[1] <= 5:
						if self.turn == 1:
							pygame.draw.rect(screen, (255, 225, 0), (draw_x, draw_y, 64, 64), 0)
						else:
							pygame.draw.rect(screen, (200, 0, 0), (draw_x, draw_y, 64, 64), 0)

				pygame.draw.rect(screen, (255, 255, 255), (draw_x, draw_y, 64, 64), 2)

				if self.grid[y][x] == 1:
					screen.blit(self.yellow_chip, (draw_x, draw_y))
				elif self.grid[y][x] == 2:
					screen.blit(self.red_chip, (draw_x, draw_y))
				draw_x += 64
			draw_y += 64

	def update(self):
		x, y = pygame.mouse.get_pos()
		self.mouse_grid_pos = ((x - 206) // 64, (y - 38) // 64)

	def event_handler(self, event):
		if event.type == pygame.MOUSEBUTTONUP:
			if self.back_button.rect.collidepoint(event.pos):
				self.back_button.on_click()

			if self.mouse_grid_pos[0] < 0 or self.mouse_grid_pos[0] > 6 or self.mouse_grid_pos[1] < 0 or self.mouse_grid_pos[1] > 5:
				return

			if self.grid[0][self.mouse_grid_pos[0]] == 0:
				self.grid[self.get_free_tile(self.mouse_grid_pos[0])][self.mouse_grid_pos[0]] = self.turn

			if self.turn == 1:
				self.turn = 2
			else:
				self.turn = 1

		else:
			self.back_button.event_handler(event)

	def back(self):
		self.quit = True

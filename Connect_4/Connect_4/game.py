import pygame
from button import Button

class Game:
	def __init__(self):
		self.quit = False

		self.red_chip = pygame.image.load("Red_Chip.png")
		self.yellow_chip = pygame.image.load("Yellow_Chip.png")

		self.red_win = pygame.image.load("Red_Win.png")
		self.yellow_win = pygame.image.load("Yellow_Win.png")
		self.tie = pygame.image.load("Tie.png")
		self.yellow_big = pygame.image.load("Yellow_Chip_Big.png")
		self.red_big = pygame.image.load("Red_Chip_Big.png")

		self.back_button = Button((-25, 405), (215, 67), pygame.image.load("Back_Default.png"), pygame.image.load("Back_Highlight.png"), lambda: self.back())

		self.turn = 1

		self.win_condition = 0

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

	def check_win_condition(self):

		# Check horizontal
		for y in range(0, 6):
			for x in range(0, 4):
				if self.grid[y][x] == self.turn and self.grid[y][x + 1] == self.turn and self.grid[y][x + 2] == self.turn and self.grid[y][x + 3] == self.turn:
					self.win_condition = self.turn

		# Check vertical 
		for x in range(0, 7):
			for y in range(0, 3):
				if self.grid[y][x] == self.turn and self.grid[y + 1][x] == self.turn and self.grid[y + 2][x] == self.turn and self.grid[y + 3][x] == self.turn:
					self.win_condition = self.turn

		# Check diagonals
		for y in range(0, 3):
			for x in range(0, 4):
				if self.grid[y][x] == self.turn and self.grid[y + 1][x + 1] == self.turn and self.grid[y + 2][x + 2] == self.turn and self.grid[y + 3][x + 3] == self.turn:
					self.win_condition = self.turn

		for y in range(3, 6):
			for x in range(0, 4):
				if self.grid[y][x] == self.turn and self.grid[y - 1][x + 1] == self.turn and self.grid[y - 2][x + 2] == self.turn and self.grid[y - 3][x + 3] == self.turn:
					self.win_condition = self.turn

		# Check tie
		for x in range(0, 7):
			if self.grid[0][x] == 0:
				return
		if self.win_condition == 0:
			self.win_condition = 3

	def render(self, screen):
		screen.fill((40, 20, 0))
		self.back_button.draw(screen)

		if self.win_condition == 1:
			screen.blit(self.yellow_win, (168, 32))
			screen.blit(self.yellow_big, (302, 154))
			return
		elif self.win_condition == 2:
			screen.blit(self.red_win, (168, 32))
			screen.blit(self.red_big, (302, 154))
			return
		elif self.win_condition == 3:
			screen.blit(self.tie, (168, 32))
			screen.blit(self.yellow_big, (544, 154))
			screen.blit(self.red_big, (60, 154))
			return

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

				self.check_win_condition()

				if self.turn == 1:
					self.turn = 2
				else:
					self.turn = 1

		else:
			self.back_button.event_handler(event)

	def back(self):
		self.quit = True

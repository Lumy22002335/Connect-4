import pygame
from button import Button

class Menu:
    def __init__(self):
        self.start = False
        self.quit = False
        self.credits = False

        self.red_circle = pygame.image.load("Red_Chip_Big.png")
        self.yellow_circle = pygame.image.load("Yellow_Chip_Big.png")

        self.title = pygame.image.load("Title.png")

        self.buttons = []
        self.buttons.append(Button((322, 230), (215, 67), pygame.image.load("Play_Default.png"), pygame.image.load("Play_Highlight.png"), lambda: self.play()))
        self.buttons.append(Button((322, 290), (215, 67), pygame.image.load("Quit_Default.png"), pygame.image.load("Quit_Highlight.png"), lambda: self.exit()))
        self.buttons.append(Button((322, 350), (215, 67), pygame.image.load("Credits_Default.png"), pygame.image.load("Credits_Highlight.png"), lambda: self.display_credits()))
    
    def render(self, screen):
        screen.fill((40, 20, 0))
        screen.blit(self.title, (228, 0))
        screen.blit(self.red_circle, (20, 125))
        screen.blit(self.yellow_circle, (584, 125))
        for b in self.buttons:
            b.draw(screen)

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            for b in self.buttons:
                if b.rect.collidepoint(event.pos):
                    b.on_click()
        else:
            for b in self.buttons:
                b.event_handler(event)

    def play(self):
        self.start = True

    def exit(self):
        self.quit = True

    def display_credits(self):
        self.credits = True



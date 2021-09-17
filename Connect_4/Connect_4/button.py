import pygame

class Button:
    def __init__(self, position, size, default_image, highlighted_image, on_click):
        self.rect = pygame.Rect(position, size)
        self.default_image = default_image
        self.highlighted_image = highlighted_image
        self.current_image = default_image
        self.on_click = on_click



    def draw(self, screen):
        screen.blit(self.current_image, self.rect)

    def event_handler(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.current_image = self.highlighted_image
            else:
                self.current_image = self.default_image

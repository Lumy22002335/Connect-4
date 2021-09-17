import pygame
import sys
from menu import Menu

pygame.init()

screen = pygame.display.set_mode((860, 480))

scene = Menu()

def main():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEMOTION:
                scene.event_handler(event)

        scene.render(screen)

        pygame.display.flip()

main()

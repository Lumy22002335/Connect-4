import pygame
import sys
from menu import Menu
from game import Game


def main():

    pygame.init()

    screen = pygame.display.set_mode((860, 480))

    scene = Menu()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEMOTION:
                scene.event_handler(event)

        scene.render(screen)

        if isinstance(scene, Menu):
            if scene.start:
                scene = Game()
            elif scene.credits:
                scene = Credits()

        if scene.quit:
            if isinstance(scene, Menu):
                exit()
            else:
                scene = Menu()

        pygame.display.flip()

main()

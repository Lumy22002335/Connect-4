import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((860, 480))

def main():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

main()

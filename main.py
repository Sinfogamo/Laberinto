# -*- encoding: utf-8 -*-
import pygame
import sys
from Models.Sahara import Sahara

WHITE = (255, 255, 255)
GREEN = (48, 163, 71)
width = 900
heigth = 600
animal_size = 50
CONTAINER = (width, heigth)


def run_game(window, sahara):
    while True:
        window.fill(GREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        sahara.drawAnimals()
        pygame.display.flip()
    pygame.quit()


def run():
    pygame.init()
    window = pygame.display.set_mode(CONTAINER)
    pygame.display.set_caption("Lions and impalas")
    sahara = Sahara(window)
    run_game(window, sahara)


if __name__ == '__main__':
    run()

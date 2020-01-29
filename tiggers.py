# -*- encoding: utf-8 -*-
import pygame, sys
from Lion import Lion

WHITE = (255, 255, 255)
GREEN = (48, 163, 71)
RED_LOCATION = (204, 78, 78);
width = 900 
heigth = 600
animal_size = 50
CONTAINER = (width, heigth)
FRAME_PIXELS = 20

def run_game(window, LionImg, lion1, lion2, lion3, lion4): 
    while True:
        window.fill(GREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        window.blit(LionImg, lion1.lion)
        window.blit(LionImg, lion2.lion)
        window.blit(LionImg, lion3.lion)
        window.blit(LionImg, lion4.lion)
        # pygame.draw.rect(window, RED_LOCATION, lion1.paintLook)
        # pygame.draw.rect(window, RED_LOCATION, lion2.paintLook)
        lion1.pintarCuadros()
        lion2.pintarCuadros()
        lion3.pintarCuadros()
        lion4.pintarCuadros()
        
        pygame.display.flip()
    pygame.quit()         

def run():
    pygame.init()
    window = pygame.display.set_mode(CONTAINER)
    pygame.display.set_caption("Lions and impalas")
    
    # images animals and longitud
    lion1 = Lion(window)
    lion2 = Lion(window)
    lion3 = Lion(window)
    lion4 = Lion(window)
    
    # print(lion1.pintarCuadros())
    # print(lion2.pintarCuadros())
    # print('Lion positon 0 {} position 1 {}'.format(lion.widthContainer, lion.heigthContainer))
    
    run_game(window, lion1.Image, lion1, lion2, lion3, lion4)

if __name__ == '__main__':
    run()


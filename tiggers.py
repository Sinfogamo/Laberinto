# -*- encoding: utf-8 -*-
import pygame, sys, random

WHITE = (255, 255, 255)
GREEN = (48, 163, 71)
width = 900 
heigth = 600
CONTAINER = (width, heigth)
animal_lenght = (70, 70)

def run_game(window, lion, impala, 
                     lion1, lion2, 
                     imp1, imp2, imp3, imp4, imp5): 
    while True:
        window.fill(GREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        window.blit(lion, lion1)
        window.blit(lion, lion2)
        window.blit(impala, imp1)
        window.blit(impala, imp2)
        window.blit(impala, imp3)
        window.blit(impala, imp4)
        window.blit(impala, imp5)
        pygame.display.flip()
    pygame.quit()         

def draw_animals(animal):
    animalrect = animal.get_rect()
    animalrect.x = get_position(width - 70)
    animalrect.y = get_position(heigth - 70)
    
    return animalrect

def run():
    pygame.init()
    window = pygame.display.set_mode(CONTAINER)
    pygame.display.set_caption("Lions and impalas")
    # images animals and longitud
    lion = pygame.image.load("./resourses/lion.png")
    lion = pygame.transform.scale(lion, animal_lenght)
    impala = pygame.image.load("./resourses/impala.png")
    impala = pygame.transform.scale(impala, animal_lenght)

    lion1 = draw_animals(lion)
    lion2 = draw_animals(lion)
    imp1 = draw_animals(impala)
    imp2 = draw_animals(impala)
    imp3 = draw_animals(impala)
    imp4 = draw_animals(impala)
    imp5 = draw_animals(impala)
   
    run_game(window, lion, impala, lion1, lion2, imp1, imp2, imp3, imp4, imp5) 

def get_position(lenght):
    position = random.sample(range(1, lenght), 5)
    return position[0]

if __name__ == '__main__':
    run()


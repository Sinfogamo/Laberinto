from Models.Animal import Animal
import pygame
import time


class Lion(Animal):
    def __init__(self, window):
        super().__init__(window, './resourses/lion.png', (204, 78, 78))

    def detect_proximity(self, name, impalas, fn):
        self.scope = []
        for idx, impala in impalas.items():
            for cuadro in self.squares:
                self._validateAddress(self.animalLook)
                if cuadro.colliderect(impala.animal):
                    if self.animal.x > impala.animal.x:
                        self.animal.x -= 1
                    elif self.animal.x < impala.animal.x:
                        self.animal.x += 1
                    elif self.animal.y > impala.animal.y:
                        self.animal.y -= 1
                    elif self.animal.y < impala.animal.y:
                        self.animal.y += 1
                    elif self.animal.x == impala.animal.x and self.animal.y == impala.animal.y:
                        print(f'{name} {self.physical_condition} cazó {idx}')
                        return fn()

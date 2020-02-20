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
                    if idx == "Lion":
                        # self.move_lion(impala)
                        print(f'{name} colliciono con {idx}')
                        print(
                            f'{name}:{self.physical_condition} {idx}:{impala.physical_condition}')
                        if self.physical_condition == "Grande" and impala.physical_condition == "Grande":
                            # Pelearse
                            self.move_lion(impala)
                        if self.physical_condition == "Mediano" and impala.physical_condition == "Mediano":
                            self.move_lion(impala)
                        # Pelearse
                        if self.physical_condition == "Cachorro" and impala.physical_condition != "Cachorro":
                            pass
                        # huir del Leon Grande
                    else:
                        if self.physical_condition != "Cachorro" and impala.size_animal != "Grande":
                            print(
                                f'{name} {self.physical_condition} detecta a {idx} {impala.size_animal}')
                            if self.animal.x > impala.animal.x:
                                self.animal.x -= 1
                            elif self.animal.x < impala.animal.x:
                                self.animal.x += 1
                            elif self.animal.y > impala.animal.y:
                                self.animal.y -= 1
                            elif self.animal.y < impala.animal.y:
                                self.animal.y += 1
                            elif self.animal.x == impala.animal.x and self.animal.y == impala.animal.y:
                                print(
                                    f'{name} {self.physical_condition} cazó {idx}')
                                return fn()

    def move_lion(self, impala):
        if self.animal.x > impala.animal.x:
            self.animal.x -= 1
        elif self.animal.x < impala.animal.x:
            self.animal.x += 1
        elif self.animal.y > impala.animal.y:
            self.animal.y -= 1
        elif self.animal.y < impala.animal.y:
            self.animal.y += 1

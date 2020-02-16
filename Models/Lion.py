from Models.Animal import Animal
import pygame


class Lion(Animal):
    def __init__(self, window):
        super().__init__(window, './resourses/lion.png', (204, 78, 78))

    def drawRect(self):
        for idx in self.scope:
            pygame.draw.rect(self._window, self._location, [
                idx[0], idx[1], self._size, self._size])

    def detect_proximity(self, name, impalas):
        for idx, impala in impalas.items():
            for cuadro in self.squares:
                if cuadro.colliderect(impala.animal):
                    print(f'{name} {self.physical_condition} persive a {idx}')

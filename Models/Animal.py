import pygame
import sys
import random


class Animal:
    def __init__(self, window, img, color):
        pygame.init()
        self._window = window
        self._location = color
        self.squares = []
        self.scope = []
        self._size = 90
        self.widthContainer = 900
        self.heigthContainer = 600
        self.Image = pygame.image.load(img)
        self.Image = pygame.transform.scale(
            self.Image, (self._size, self._size))
        self._drawAnimalPosition()

    def _drawAnimalPosition(self):
        self.animal = self.Image.get_rect()
        self.animal.x = self._getPosition(self.widthContainer - self._size)
        self.animal.y = self._getPosition(self.heigthContainer - self._size)
        physical_condition = ["Viejo", "Joven", "Pequeño"]
        random.shuffle(physical_condition)
        self.physical_condition = physical_condition[0]
        # Get Lion Look
        animalLook = self._randomAddress(self.animal.x, self.animal.y)
        # print(animalLook)
        # validate direction and draw
        self._validateAddress(animalLook)
        self.get_squares()

    def _getPosition(self, limit):
        position = random.sample(range(1, limit), 3)
        return position[0]

    def _randomAddress(self, x, y):
        self._frente = x + self._size
        self._atras = x - self._size
        self._arriba = y - self._size
        self._abajo = y + self._size
        lookList = [self._frente, self._atras, self._arriba, self._abajo]
        # lookList = [self._arriba, self._abajo]
        random.shuffle(lookList)
        if lookList[0] == self._frente:
            self.orientation = "front"
        elif lookList[0] == self._atras:
            self.orientation = "behind"
        elif lookList[0] == self._abajo:
            self.orientation = "down"
        else:
            self.orientation = "above"
        return lookList[0]

    def _validateAddress(self, look):
        self.paintLook = []
        if look == self._frente:
            # dibujar hacia adelante
            ejeX = self._frente
            ejeY = self.animal.y
            mas = 0
            for i in range(1, 3):
                if i == 1:
                    self._drawLook(ejeX, ejeY)
                else:
                    mas += self._size
                    self._drawLook(ejeX + mas, ejeY + mas)
                    self._drawLook(ejeX + mas, ejeY)
                    self._drawLook(ejeX + mas, ejeY - mas)
        elif look == self._atras:
            # dibujar hacia atras
            ejeX = self._atras
            ejeY = self.animal.y
            mas = 0
            for i in range(1, 3):
                if i == 1:
                    self._drawLook(ejeX, ejeY)
                else:
                    mas += self._size
                    self._drawLook(ejeX - mas, ejeY + mas)
                    self._drawLook(ejeX - mas, ejeY)
                    self._drawLook(ejeX - mas, ejeY - mas)
        elif look == self._arriba:
            # dibujar hacia arriba
            ejeX = self.animal.x
            ejeY = self._arriba
            mas = 0
            for i in range(1, 3):
                if i == 1:
                    self._drawLook(ejeX, ejeY)
                else:
                    mas += self._size
                    self._drawLook(ejeX + mas, ejeY - mas)
                    self._drawLook(ejeX, ejeY - mas)
                    self._drawLook(ejeX - mas, ejeY - mas)
        elif look == self._abajo:
            # dibujar hacia abajo
            ejeX = self.animal.x
            ejeY = self._abajo
            mas = 0
            for i in range(1, 3):
                if i == 1:
                    self._drawLook(ejeX, ejeY)
                else:
                    mas += self._size
                    self._drawLook(ejeX + mas, ejeY + mas)
                    self._drawLook(ejeX, ejeY + mas)
                    self._drawLook(ejeX - mas, ejeY + mas)

    def _drawLook(self, x, y):
        self.scope.append((x, y))

    # def drawRect(self):
    #     for idx in self.scope:
    #         # print("Eje X: {} Eje Y: {}".format(idx[0], idx[1]))
    #         pygame.draw.rect(self._window, self._location, [
    #             idx[0], idx[1], self._size, self._size])

    def get_squares(self):
        for idx in self.scope:
            cuadro = pygame.draw.rect(self._window, self._location, [
                idx[0], idx[1], self._size, self._size])
            self.squares.append(cuadro)

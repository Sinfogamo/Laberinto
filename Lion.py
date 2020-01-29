import pygame, sys, random

class Lion:
    def __init__(self, window):
        pygame.init()
        self.alcance = []
        self._window = window
        self._RED_LOCATION = (204, 78, 78);
        self._scope = []
        self._size = 80
        self.widthContainer = 900
        self.heigthContainer = 600
        self.Image = pygame.image.load("./resourses/lion.png")
        self.Image = pygame.transform.scale(self.Image, (self._size, self._size))
        self._drawLionPosition()
        
    def _drawLionPosition(self):
        self.lion = self.Image.get_rect()
        self.lion.x = self._getPosition(self.widthContainer - self._size)
        self.lion.y = self._getPosition(self.heigthContainer - self._size)
        # Get Lion Look
        lionLook = self._randomAddress(self.lion.x, self.lion.y)
        print(lionLook)
        # validate direction and draw
        self._validateAddress(lionLook)
        
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
        return lookList[0]

    def _validateAddress(self, look):
        self.paintLook = []
        if look == self._frente:
            # dibujar hacia adelante 
            ejeX = self._frente
            ejeY = self.lion.y
            mas = 0
            for i in range(1, 3):
                if i == 1 :
                    self._drawLook(ejeX, ejeY)
                # elif i == 2:
                #     mas += self._size
                #     self._drawLook(ejeX + mas, ejeY - mas)
                #     self._drawLook(ejeX + mas, ejeY)
                #     self._drawLook(ejeX + mas, ejeY + mas)
                else:
                    mas += self._size
                    self._drawLook(ejeX + mas, ejeY + mas)
                    self._drawLook(ejeX + mas, ejeY)
                    self._drawLook(ejeX + mas, ejeY - mas)
        elif look == self._atras:
            # dibujar hacia atras 
            ejeX = self._atras
            ejeY = self.lion.y
            mas = 0
            for i in range(1, 3):
                if i == 1 :
                    self._drawLook(ejeX, ejeY)
                # elif i == 2:
                #     mas += self._size
                #     self._drawLook(ejeX - mas, ejeY + mas)
                #     self._drawLook(ejeX - mas, ejeY)
                #     self._drawLook(ejeX - mas, ejeY - mas)
                else:
                    mas += self._size
                    self._drawLook(ejeX - mas, ejeY + mas)
                    self._drawLook(ejeX - mas, ejeY)
                    self._drawLook(ejeX - mas, ejeY - mas)
        elif look == self._arriba:
            # dibujar hacia arriba 
            ejeX = self.lion.x
            ejeY = self._arriba
            mas = 0
            for i in range(1, 3):
                if i == 1 :
                    self._drawLook(ejeX, ejeY)
                # elif i == 2:
                #     mas += self._size
                #     self._drawLook(ejeX + mas, ejeY - mas)
                #     self._drawLook(ejeX, ejeY - mas)
                #     self._drawLook(ejeX - mas, ejeY - mas)
                else:
                    mas += self._size
                    self._drawLook(ejeX + mas, ejeY - mas)
                    self._drawLook(ejeX, ejeY - mas)
                    self._drawLook(ejeX - mas, ejeY - mas)
        elif look == self._abajo:
            # dibujar hacia abajo 
            ejeX = self.lion.x
            ejeY = self._abajo
            mas = 0
            for i in range(1, 3):
                if i == 1 :
                    self._drawLook(ejeX, ejeY)
                # elif i == 2:
                #     mas += self._size
                #     self._drawLook(ejeX + mas, ejeY + mas)
                #     self._drawLook(ejeX, ejeY + mas)
                #     self._drawLook(ejeX - mas, ejeY + mas)
                else:
                    mas += self._size
                    self._drawLook(ejeX + mas, ejeY + mas)
                    self._drawLook(ejeX, ejeY + mas) 
                    self._drawLook(ejeX - mas, ejeY + mas) 
    
    def _drawLook(self, x, y):
        self.alcance.append( (x, y) )
        
        
    def pintarCuadros(self):
        # print(self.paintLook)
        # pygame.draw.rect(self._window, self._RED_LOCATION, self.paintLook)
        for idx in self.alcance:
            print("Eje X: {} Eje Y: {}".format(idx[0], idx[1]))
            pygame.draw.rect(self._window, self._RED_LOCATION, [idx[0], idx[1], self._size, self._size])
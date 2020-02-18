from Models.Lion import Lion
from Models.Impala import Impala


class Sahara:
    def __init__(self, window):
        self._window = window
        self.lion1 = Lion(window)
        self.lion2 = Lion(window)
        self.impala1 = Impala(window)
        self.impala2 = Impala(window)
        self.impala3 = Impala(window)
        self.impala4 = Impala(window)
        self.impala5 = Impala(window)

        self._ubicationImpalas = {
            "impala1": self.impala1,
            "impala2": self.impala2,
            "impala3": self.impala3,
            "impala4": self.impala4,
            "impala5": self.impala5
        }

    def getAnimals(self):
        self._window.fill((48, 163, 71))
        self._window.blit(self.impala1.Image, self.impala1.animal)
        self._window.blit(self.impala2.Image, self.impala2.animal)
        self._window.blit(self.impala3.Image, self.impala3.animal)
        self._window.blit(self.impala4.Image, self.impala4.animal)
        self._window.blit(self.impala5.Image, self.impala5.animal)

        self._window.blit(self.lion1.Image, self.lion1.animal)
        self._window.blit(self.lion2.Image, self.lion2.animal)
        self.drawRect()

    def drawAnimals(self):
        self.getAnimals()
        # self.drawRect()
        self.lion1.detect_proximity(
            "Leon1", self._ubicationImpalas, self.getAnimals)
        self.lion2.detect_proximity(
            "Leon2", self._ubicationImpalas, self.getAnimals)

    def drawRect(self):
        self.lion1.drawRect()
        self.lion2.drawRect()

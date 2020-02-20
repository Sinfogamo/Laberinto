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

        self._ubicationImpalas1 = {
            "impala1": self.impala1,
            "impala2": self.impala2,
            "impala3": self.impala3,
            "impala4": self.impala4,
            "impala5": self.impala5,
            "Lion": self.lion1
        }
        self._ubicationImpalas2 = {
            "impala1": self.impala1,
            "impala2": self.impala2,
            "impala3": self.impala3,
            "impala4": self.impala4,
            "impala5": self.impala5,
            "Lion": self.lion2
        }

        self._ubicationLions = {
            "Lion1": self.lion1,
            "Lion2": self.lion2
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
            "Leon1", self._ubicationImpalas2, self.getAnimals)
        self.lion2.detect_proximity(
            "Leon2", self._ubicationImpalas1, self.getAnimals)
        self.impala1.detect_proximy(self._ubicationLions, self.getAnimals)
        self.impala2.detect_proximy(self._ubicationLions, self.getAnimals)
        self.impala3.detect_proximy(self._ubicationLions, self.getAnimals)
        self.impala4.detect_proximy(self._ubicationLions, self.getAnimals)
        self.impala5.detect_proximy(self._ubicationLions, self.getAnimals)

    def drawRect(self):
        self.lion1.drawRect()
        self.lion2.drawRect()
        self.impala1.drawRect()
        self.impala2.drawRect()
        self.impala3.drawRect()
        self.impala4.drawRect()
        self.impala5.drawRect()

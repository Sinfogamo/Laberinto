from Models.Animal import Animal


class Impala(Animal):
    def __init__(self, window):
        super().__init__(window, "./resourses/impala2.png", (116, 179, 214, 0.49))

    def detect_proximy(self, lions, fn):
        self.scope = []
        for idx, lion in lions.items():
            for cuadro in self.squares:
                self._validateAddress(self.animalLook)
                if cuadro.colliderect(lion.animal):
                    if self.animal.x > lion.animal.x:
                        self.animal.x += 1
                    elif self.animal.x < lion.animal.x:
                        self.animal.x -= 1
                    elif self.animal.y > lion.animal.y:
                        self.animal.y += 1
                    elif self.animal.y < lion.animal.y:
                        self.animal.y -= 1
                else:
                    self.animal.x = self.animal.x
                    self.animal.y = self.animal.y
        return fn()

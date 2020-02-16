from Models.Animal import Animal


class Impala(Animal):
    def __init__(self, window):
        super().__init__(window, "./resourses/impala2.png", (116, 179, 214, 0.49))

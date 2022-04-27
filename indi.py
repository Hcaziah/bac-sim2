class Individual:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.age = 0
        self.color = [255, 255, 255]
        self.genome = 0x0000

    def mutate(self):
        pass

    def replicate(self):
        pass

    def apoptos(self):
        pass

    def get_pos(self):
        return self.pos

    def get_age(self):
        return self.age

    def set_color(self, color):
        self.color = color

    

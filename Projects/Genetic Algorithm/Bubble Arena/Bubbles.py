from Constants import Constants as C
from random import randint


class Bubbles:

    def __init__(self, radius, speed, color, species):
        self.radius = radius
        self.speed = speed
        self.color = color
        self.species = species

        self.age = 0
        self.hp = C.default_hp
        self.current_vec = self.move(self.speed)

        if self.species == 1:
            self.x = Bubbles.create_pos(C.bbl1_radius)[0]
            self.y = Bubbles.create_pos(C.bbl1_radius)[1]
        if self.species == 2:
            self.x = Bubbles.create_pos(C.bbl2_radius)[0]
            self.y = Bubbles.create_pos(C.bbl2_radius)[1]
        if self.species == 3:
            self.x = Bubbles.create_pos(C.bbl3_radius)[0]
            self.y = Bubbles.create_pos(C.bbl3_radius)[1]

    @staticmethod
    def create_bubble1():
        return Bubbles(C.bbl1_radius, C.bbl1_speed, C.bbl1_color, 1)

    @staticmethod
    def create_bubble2():
        return Bubbles(C.bbl2_radius, C.bbl2_speed, C.bbl2_color, 2)

    @staticmethod
    def create_bubble3():
        return Bubbles(C.bbl3_radius, C.bbl3_speed, C.bbl3_color, 3)

    @staticmethod
    def create_pos(radius):
        x = randint(C.border + radius, C.width - C.border - radius)
        y = randint(C.border + radius, int(C.st_proportion * C.height) - C.border - radius)

        return x, y

    @staticmethod
    def move(speed):
        x, y = randint(-1, 1)*speed, randint(-1, 1)*speed
        return x, y

    @staticmethod
    def collide(pos1, pos2, radius):
        pass

    def update(self):
        pass


class Food:

    def food(self):
        pass

    def poison(self):
        pass

    def collide(self):
        pass

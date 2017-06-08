from Constants import Constants as C
from random import randint
from math import pi, cos, sin


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
    def collide(pos1, pos2, radius1, radius2):
        if (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2 <= (radius1 + radius2) ** 2:
            return True
        return False


class Food:

    def __init__(self, food=True, x=0, y=0):
        self.food = food
        self.width = C.fd_width
        self.height = C.fd_height
        if x == 0 and y == 0:
            self.x = randint(C.border + C.fd_width, C.width - C.border - C.fd_width)
            self.y = randint(C.border + C.fd_height, int(C.st_proportion * C.height) - C.border - C.fd_height)
        else:
            self.x = x
            self.y = y

        self.color = C.fd_color
        self.health = C.fd_health
        if not self.food:
            self.health *= -1
            self.color = C.poison_color

    @staticmethod
    def spawn_food(x, y):
        return Food(x=x, y=y)

    @staticmethod
    def spawn_poison():
        return Food(food=False)

    def collide(self, pos2, radius2):
        for i in range(180):
            x = pos2[0] + radius2 * cos(i * pi / 180)
            y = pos2[1] + radius2 * sin(i * pi / 180)
            if self.x <= x <= self.x + C.fd_width and self.y <= y <= self.y + C.fd_height:
                return True
        return False

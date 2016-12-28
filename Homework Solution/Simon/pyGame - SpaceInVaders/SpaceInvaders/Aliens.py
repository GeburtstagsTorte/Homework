from pygame import transform
from Constants import Constants

"""
    A RECT
    pos_rect[0] = x
    pos_rect[1] = y
    pos_rect[2] = width
    pos_rect[3] = height
"""


class Alien:

    direction = 1           # Alien.direction
    direction_y = Constants.alien_size // 2
    speed_factor = 3

    def __init__(self, pos_rect, collision_box, image):
        self.pos_rect = pos_rect
        self.collision_box = collision_box
        self.image = transform.scale(image, (int(pos_rect[2]), int(pos_rect[3])))           # width, height

    def render(self, game_display):
        game_display.blit(self.image, self.pos_rect)

    def update(self):
        if self.pos_rect[0] >= Constants.WIDTH - Constants.alien_size:
            Alien.direction = -1
        elif self.pos_rect[0] <= 0:
            Alien.direction = 1
        self.move()

    def move(self):
        self.pos_rect[0] += Alien.direction * Alien.speed_factor


class MotherShip:    # could do inheritance but not nau pl0x

    direction = 1
    speed_factor = 2
    health = 10

    def __init__(self, pos_rect, collision_box, image):
        self.pos_rect = pos_rect
        self.collision_box = collision_box
        self.image = transform.scale(image, (int(pos_rect[2]), int(pos_rect[3])))

    def render(self, game_display):
        game_display.blit(self.image, self.pos_rect)

    def update(self):
        if self.pos_rect[0] >= int(Constants.WIDTH * (3/4)) - Constants.mother_ship_size:
            MotherShip.direction = -1
        elif self.pos_rect[0] <= int(Constants.WIDTH // 4):
            MotherShip.direction = 1
        self.move()

    def move(self):
        self.pos_rect[0] += MotherShip.direction * MotherShip.speed_factor

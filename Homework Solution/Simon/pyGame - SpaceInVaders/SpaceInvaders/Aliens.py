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

    # Entities.aliens[i].collision_box[2] // 2):

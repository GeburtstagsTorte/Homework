import pygame
from Constants import Constants as C
from random import randint


class Segment:

    def __init__(self, x, y, color, surface, length=C.length, height=C.length):
        self.x = x
        self.y = y
        self.color = color
        self.surface = surface
        self.length = length
        self.height = height

    def render(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.length, self.height))

    def update(self):
        pass


class Food:

    def __init__(self, x, y, surface, color, length=C.length, height=C.length):
        self.x = x
        self.y = y
        self.surface = surface
        self.color = color
        self.length = length
        self.height = height

    def render(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.length, self.height))


class Objects:

    segments = []
    # food = object
    food_x = randint(10, C.height)
    food_y = randint(10, C.width)

    def __init__(self, game_display):
        Objects.segments.append(Objects.add_segment(game_display, C.width // 2, C.height // 2))

    @staticmethod
    def render(game_display):
        Food(Objects.food_x, Objects.food_y, game_display, C.red).render()

        for segment in Objects.segments:
            segment.render()

    @staticmethod
    def update():
        Objects.segments[0].x += C.dir * C.is_x * C.speed
        Objects.segments[0].y += C.dir * C.is_y * C.speed

    @staticmethod
    def add_segment(game_display, x, y):
        return Segment(x, y, C.grey, game_display)

    @staticmethod
    def handle_keys(event):
        if event.type == pygame.KEYDOWN:
            if event.key == 119:
                # w
                C.dir = -1
                C.is_x = False
                C.is_y = True

            if event.key == 97:
                # a
                C.dir = -1
                C.is_y = False
                C.is_x = True

            if event.key == 115:
                # s
                C.dir = 1
                C.is_x = False
                C.is_y = True

            if event.key == 100:
                # d
                C.dir = 1
                C.is_y = False
                C.is_x = True

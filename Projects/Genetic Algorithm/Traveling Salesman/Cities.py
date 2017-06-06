import pygame
import pygame.gfxdraw
from random import randint
from Constants import C


class City:

    def __init__(self, surface, width, height, color, radius):
        self.surface = surface
        self.width = width
        self.height = height
        self.color = color
        self.radius = radius

        self.x = randint(self.radius*2 + C.border, 0.75*(self.width - 2*self.radius) - C.border)
        self.y = randint(self.radius*2 + C.border, 0.5*(self.height - 2*self.radius) - C.border)

        self.pos = self.x, self.y

    @staticmethod
    def render_cities(cities):
        for city in cities:
            city.draw_city()

    @staticmethod
    def draw_paths(cities, surface, color=(255, 255, 255)):
        for i in range(len(cities)-1):
            pygame.draw.aaline(surface, color, cities[i].pos, cities[i+1].pos)

    def draw_city(self):
        # pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)
        pygame.gfxdraw.aacircle(self.surface, self.pos[0], self.pos[1], self.radius, self.color)

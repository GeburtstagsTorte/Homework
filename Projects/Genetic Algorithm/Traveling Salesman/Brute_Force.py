from itertools import permutations
from math import sqrt
import pygame


class BruteForce:

    best = []
    d_record = 0

    @staticmethod
    def calculate_best(route, cities):
        d = 0
        for i in range(len(route)-1):
            d += sqrt((cities[route[i]].x - cities[route[i+1]].x)**2 + (cities[route[i]].y - cities[route[i+1]].y)**2)

        d = 1 / d
        if d > BruteForce.d_record:
            BruteForce.best = route
            BruteForce.d_record = d

    @staticmethod
    def create_routes(city_amount):
        pool = [i for i in range(city_amount)]
        return list(permutations(pool))

    @staticmethod
    def draw_route(surface, cities, route, color=(200, 0, 0)):
        for i in range(len(route)-1):
            pygame.draw.aaline(surface, color, cities[route[i]].pos, cities[route[i+1]].pos)

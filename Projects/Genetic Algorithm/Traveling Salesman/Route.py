import pygame
import pygame.gfxdraw
from random import randint
from Constants import C


class Route:

    def __init__(self, genes, fitness):
        self.genes = genes
        self.fitness = fitness

    @staticmethod
    def create_route(city_amount):
        genes = []

        pool = [i for i in range(city_amount)]
        for j in range(len(pool)):
            index = randint(0, len(pool) - 1)
            genes.append(pool[index])
            del pool[index]

        return Route(genes, fitness=0)

    @staticmethod
    def draw_routes(surface, color, route, cities):
        for i in range(len(route.genes)-1):
            pygame.draw.aaline(surface, color, cities[route.genes[i]].pos, cities[route.genes[i+1]].pos)

    @staticmethod
    def draw_best_route(surface, route, cities, color=(150, 0, 200), width=1):
        for i in range(len(route.genes)-1):
            # pygame.draw.line(surface, color, cities[route.genes[i]].pos, cities[route.genes[i+1]].pos, width)
            pygame.draw.aaline(surface, color, cities[route.genes[i]].pos, cities[route.genes[i+1]].pos)

    @staticmethod
    def draw_ga_only(surface, color, route, cities):
        for city in cities:
            pygame.gfxdraw.aacircle(surface, city.x, city.y + int(0.5*C.height), C.city_radius, C.city_color)

        for i in range(len(route)-1):
            pygame.draw.aaline(surface, color, (cities[route[i]].x, cities[route[i]].y + int(0.5*C.height)),
                               (cities[route[i+1]].x, cities[route[i+1]].y + int(0.5*C.height)))

    @staticmethod
    def multiple_crossover(a, b):
        """

        crossover doesn't make any sense for this problem

        """
        pass

    @staticmethod
    def mutation(genes, mutation_rate):
        """
        if randint(0, 100) < mutation_rate:
            choose = randint(0, len(genes)-1)
            genes[choose] = randint(0, len(genes)-1)
        return genes

        -----------------------------------------------

        swaps just to values in list

        """
        if randint(0, 100) < mutation_rate:
            choose = randint(0, len(genes)-1)
            choose2 = randint(0, len(genes)-1)

            temp = genes[choose]
            genes[choose] = genes[choose2]
            genes[choose2] = temp
        return genes

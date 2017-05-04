import pygame
from random import randint


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
            pygame.draw.line(surface, color, cities[route.genes[i]].pos, cities[route.genes[i+1]].pos)

    @staticmethod
    def draw_best_route(surface, route, cities, color=(0, 0, 200)):
        for i in range(len(route.genes)-1):
            pygame.draw.line(surface, color, cities[route.genes[i]].pos, cities[route.genes[i+1]].pos, 2)

    @staticmethod
    def multiple_crossover(a, b):
        pass

    @staticmethod
    def mutation(genes, mutation_rate):
        if randint(0, 100) < mutation_rate:
            choose = randint(0, len(genes)-1)
            genes[choose] = randint(0, len(genes)-1)
        return genes

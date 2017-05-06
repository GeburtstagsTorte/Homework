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

        d = (1 / d) * 10**3
        if d > BruteForce.d_record:

            BruteForce.best = route
            BruteForce.d_record = d
            print(BruteForce.best, d)

    @staticmethod
    def create_routes(city_amount):
        pool = [i for i in range(city_amount)]
        return list(permutations(pool))

    @staticmethod
    def draw_route(surface, cities, route, color=(200, 0, 0)):
        for i in range(len(route)-1):
            pygame.draw.aaline(surface, color, cities[route[i]].pos, cities[route[i+1]].pos)

    @staticmethod
    def find_largest_i(route):
        largest_i = -1
        for i in range(len(route)-1):
            if route[i] < route[i+1]:
                largest_i = i
        return largest_i

    @staticmethod
    def find_largest_j(route, i):
        largest_j = -1

        for j in range(len(route)):
            if route[i] < route[j]:
                largest_j = j

        return largest_j

    @staticmethod
    def swap(route, i, j):
        temp = route[i]

        route[i] = route[j]
        route[j] = temp

        return route

    @staticmethod
    def reverse_list(route, i):
        slice = route[i+1:]
        route_split = route[:i+1]

        return route_split + slice[::-1]

    @staticmethod
    def permute(route):
        """
        https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering

        """
        i = BruteForce.find_largest_i(route)
        if i == -1:
            return i
        else:
            j = BruteForce.find_largest_j(route, i)

            route = BruteForce.swap(route, i, j)
            return BruteForce.reverse_list(route, i)

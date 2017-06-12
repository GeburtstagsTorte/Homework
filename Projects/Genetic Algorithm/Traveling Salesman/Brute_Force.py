from itertools import permutations
from math import sqrt
# from textbox import CenterBox
# from Constants import C
import pygame


class BruteForce:

    best = ([], 0)

    @staticmethod
    def initialize_route(city_amount):
        return [i for i in range(city_amount)]

    @staticmethod
    def calculate_best(route, cities):

        d = 0
        for i in range(len(route)-1):
            d += sqrt((cities[route[i]].x - cities[route[i+1]].x)**2 + (cities[route[i]].y - cities[route[i+1]].y)**2)

        d = (1 / d) * 10 ** 3
        if d > BruteForce.best[1]:
            BruteForce.best = (route, d)

    @staticmethod
    def create_routes(city_amount):
        pool = [i for i in range(city_amount)]
        return list(permutations(pool))

    @staticmethod
    def draw_route(surface, cities, route, color=(200, 0, 0)):
        for i in range(len(route)-1):
            pygame.draw.aaline(surface, color, (cities[route[i]].pos[0], cities[route[i]].pos[1]),
                               (cities[route[i+1]].pos[0], cities[route[i+1]].pos[1]))

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
            if route[i] < route[j] and j >= i:      # i - 1
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
        s = route[i+1:]
        route_split = route[:i+1]

        return route_split + s[::-1]

    @staticmethod
    def permute(route, cities):

        """
        >Find the largest x such that P[x]<P[x+1].
        (If there is no such x, P is the last permutation.)
        >Find the largest y such that P[x]<P[y].
        >Swap P[x] and P[y].
        >Reverse P[x+1 .. n].

        https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering

        """
        i = BruteForce.find_largest_i(route)
        if i == -1:
            return []
        else:
            j = BruteForce.find_largest_j(route, i)

            r = BruteForce.swap(route, i, j)
            BruteForce.calculate_best(route, cities)

            return BruteForce.reverse_list(r, i)
            # BruteForce.current_route = BruteForce.reverse_list(r, i)

"""import math
x = [0, 1, 2]
for i in range(math.factorial(len(x))+1):
    print(x)
    x = BruteForce.permute(x)"""

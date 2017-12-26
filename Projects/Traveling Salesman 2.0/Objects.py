import pygame
import pygame.gfxdraw
from random import randint, shuffle
from Constants import GameConstants as GC
from Textboxes import CenterBox
from math import sqrt


class Objects:

    generation = 0

    def __init__(self):
        self.cities = [
            City() for _ in range(GC.city_total)
        ]
        City.scale_cities(self.cities)

        self.population = [
            Route.create(GC.city_total, self.cities) for _ in range(GC.population_size)
        ]
        self.bf_route = Route([i for i in range(GC.city_total)],
                              self.cities)

        self.ga_best = self.population[0]
        self.bf_best = self.bf_route

    def render(self, game_display):
        for city in self.cities:
            city.render(game_display)

        self.ga_best.render(game_display, self.cities, GC.colors["crimson"])
        if self.bf_route.genes != [i for i in range(GC.city_total)][::-1]:
            self.bf_route.bf_render(game_display, self.cities, GC.colors["green"])
        self.bf_best.bf_render(game_display, self.cities, GC.colors["crimson"])

    def update(self):
        for route in self.population:
            if route.distance < self.ga_best.distance:
                self.ga_best = route
        pool = Route.selection(self.population)
        self.population = Route.new_generation(pool, self.cities)
        self.generation += 1

        if self.bf_route.distance < self.bf_best.distance:
            self.bf_best = self.bf_route
            print("if", str(self.bf_route), str(self.bf_best))
        self.bf_route = Route(Objects.permute(self.bf_route.genes), self.cities)
        print(str(self.bf_best), str(self.ga_best))

    @staticmethod
    def permute(lst):
        """
            >Find the largest x such that P[x]<P[x+1].
            (If there is no such x, P is the last permutation.)
            >Find the largest y such that P[x]<P[y].
            >Swap P[x] and P[y].
            >Reverse P[x+1 .. n].
        """
        largest_i = -1
        largest_j = -1
        for i in range(len(lst)):
            if lst[i - 1] < lst[i]:
                largest_i = i

        if largest_i <= 0:
            return lst

        for j in range(len(lst)):
            if j >= largest_i and lst[j] > lst[largest_i - 1]:
                largest_j = j

        lst[largest_j], lst[largest_i - 1] = lst[largest_i - 1], lst[largest_j]

        return lst[:largest_i] + lst[largest_i:][::-1]

    @staticmethod
    def permute_prev(lst):
        """
            this function is and should be redundant; it exists just for the sake of debugging
        """
        i = len(lst) - 1
        while i > 0 and lst[i - 1] <= lst[i]:
            i -= 1

        if i <= 0:
            return lst

        j = len(lst) - 1
        while lst[j] >= lst[i - 1]:
            j -= 1

        lst[i - 1], lst[j] = lst[j], lst[i - 1]

        return lst[:i] + lst[i:][::-1]


class City:

    def __init__(self):
        self.radius = GC.city_radius
        self.color = GC.colors["white"]
        self.x = randint(2 * GC.city_radius + GC.border, 0.75 * GC.width - 2 * GC.city_radius - GC.border)
        self.y = randint(2 * GC.city_radius + GC.border, 0.5 * GC.height - 2 * GC.city_radius - GC.border)

        self.pos = self.x, self.y

    def __str__(self):
        return "{}, {}".format(self.x, self.y)

    def render(self, game_display):
        pygame.gfxdraw.aacircle(game_display, self.x, self.y, self.radius, self.color)
        pygame.gfxdraw.aacircle(game_display, self.x, self.y + int(0.5 * GC.height), self.radius, self.color)

    @staticmethod
    def scale_cities(cities):
        pos_list = [i.pos for i in cities]
        max_width, max_height = CenterBox.identify_max_length(pos_list)
        start_pos = CenterBox.identify_pos(pos_list)

        d_pos = CenterBox.scale_pos(start_pos, GC.frame1_pos, max_width, max_height, GC.frame1_width,
                                    GC.frame1_height, 1)

        for city in cities:
            city.pos = (city.x + d_pos[0], city.y + d_pos[1])
            city.x = city.x + d_pos[0]
            city.y = city.y + d_pos[1]


class Route:

    def __init__(self, genes, cities):
        self.genes = genes
        self.distance = self.calc_distance(cities)

    def __str__(self):
        return "{} {}".format(self.genes, self.distance)

    def render(self, game_display, cities, color):
        for i in range(len(self.genes) - 1):
            pygame.draw.aaline(game_display, color, cities[self.genes[i]].pos, cities[self.genes[i + 1]].pos)

    def bf_render(self, game_display, cities, color):
        for i in range(len(self.genes) - 1):
            pygame.draw.aaline(game_display, color, (cities[self.genes[i]].x, cities[self.genes[i]].y +
                                                     int(0.5 * GC.height)),
                               (cities[self.genes[i + 1]].x, cities[self.genes[i + 1]].y +
                                int(0.5 * GC.height)))

    def calc_distance(self, cities):
        distance_sum = 0

        for i in range(len(self.genes) - 1):
            distance_sum += sqrt(
                (cities[self.genes[i]].x - cities[self.genes[i + 1]].x) ** 2 +
                (cities[self.genes[i]].y - cities[self.genes[i + 1]].y) ** 2
            )
        return distance_sum

    @staticmethod
    def create(total, cities):
        genes = [i for i in range(total)]
        shuffle(genes)
        return Route(genes, cities)

    @staticmethod
    def selection(population):
        """
            TODO: IMPROVE RANGE CALC.
        """
        distance_sum = 0
        for route in population:
            distance_sum += route.distance

        pool = []
        for route in population:
            for i in range(int(distance_sum/route.distance)):
                pool.append(route.genes)
        return pool

    @staticmethod
    def new_generation(pool, cities):
        pop_new = []
        for i in range(GC.population_size):
            pop_new.append(
                Route(Route.reproduce(pool), cities)
            )
        return pop_new

    @staticmethod
    def reproduce(pool):
        child = []

        a, b, c = pool[randint(0, len(pool) - 1)], pool[randint(0, len(pool) - 1)], pool[randint(0, len(pool) - 1)]

        for i in range(len(a)):
            if a[i] == b[i] or a[i] == c[i]:
                child.append(a[i])
            else:
                child.append(a[i])

        return Route.mutate(child, GC.mutation_rate)

    @staticmethod
    def mutate(genes, mutation_rate):
        """
        if randint(0, 100) < mutation_rate:
            choose = randint(0, len(genes)-1)
            genes[choose] = randint(0, len(genes)-1)
        return genes

        -----------------------------------------------

        swaps just two values in list

        """
        if randint(0, 100) < mutation_rate:
            choose = randint(0, len(genes)-1)
            choose2 = randint(0, len(genes)-1)

            temp = genes[choose]
            genes[choose] = genes[choose2]
            genes[choose2] = temp
        return genes

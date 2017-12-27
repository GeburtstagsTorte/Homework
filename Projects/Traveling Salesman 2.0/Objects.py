import pygame
import pygame.gfxdraw
from random import randint, shuffle
from Constants import GameConstants as GC
from Textboxes import CenterBox
from math import sqrt, factorial


class Objects:

    generation = 0
    count = 0
    last_gen = 0
    last_count = 0

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
                self.last_gen = self.generation

        pool = Route.selection(self.population)
        self.population = Route.new_generation(pool, self.cities)
        self.generation += 1
        if self.bf_route.distance < self.bf_best.distance:
            self.bf_best = self.bf_route
            self.last_count = self.count

            """print("if bf:", str(self.bf_route), str(self.bf_best), "\nnext:", Objects.permute(self.bf_route.genes),
                  "prev.:",  Objects.permute_prev(self.bf_route.genes))"""
        # print("1)bf:", str(self.bf_best), "ga:", str(self.ga_best))

        self.bf_route = Route(Objects.permute(self.bf_route.genes), self.cities)

        # print("2)bf:", str(self.bf_best), "ga:", str(self.ga_best))

        if self.count < factorial(GC.city_total):
            self.count += 1

    @staticmethod
    def permute(lst):
        l = [i for i in lst]
        """
            >Find the largest x such that P[x]<P[x+1].
            (If there is no such x, P is the last permutation.)
            >Find the largest y such that P[x]<P[y].
            >Swap P[x] and P[y].
            >Reverse P[x+1 .. n].
        """
        largest_i = -1
        largest_j = -1
        for i in range(len(l)):
            if l[i - 1] < l[i]:
                largest_i = i

        if largest_i <= 0:
            return l

        for j in range(len(l)):
            if j >= largest_i and l[j] > l[largest_i - 1]:
                largest_j = j

        l[largest_j], l[largest_i - 1] = l[largest_i - 1], l[largest_j]

        return l[:largest_i] + l[largest_i:][::-1]

    @staticmethod
    def permute_prev(l):
        lst = [i for i in l]
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
        return "x: {}, y: {}".format(self.x, self.y)

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
        return "{}, dist.: {}".format(self.genes, self.distance)

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
        x = float("inf")
        for route in population:
            if route.distance < x:
                x = route.distance
            distance_sum += route.distance
        pool = []

        for route in population:
            # int(distance_sum/(route.distance / 1000)**2)
            for i in range(int(10 * x / route.distance**2)+1):
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
        x = [i for i in range(len(a))]

        for i in range(len(a)):
            temp = [a[i], b[i], c[i]]
            dup = [j for j in temp if temp.count(j) > 1]
            if len(dup) > 0:
                x.remove(dup[0])
                child.append(dup[0])
            else:
                child.append("")

        for i in range(len(child)):
            if child[i] == "":
                r = randint(0, len(x) - 1)
                child[i] = x[r]
                del x[r]

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

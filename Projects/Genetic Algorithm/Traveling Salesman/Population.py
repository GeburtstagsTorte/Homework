from Route import Route
from Constants import C
from math import sqrt
from random import randint


class Population:

    population = []
    generation = 0

    def __init__(self, max_population, mutation_rate, cities):
        self.max_population = max_population
        self.mutation_rate = mutation_rate
        self.cities = cities

        self.best = Route([], 0)

        self.initialize_population()
        self.calculate_fitness()

    def initialize_population(self):
        self.population = [Route.create_route(C.city_amount) for i in range(self.max_population)]

    def calculate_fitness(self):
        for route in self.population:
            distance_sum = 0
            for i in range(len(route.genes)-1):
                distance_sum += sqrt((self.cities[route.genes[i]].x - self.cities[route.genes[i+1]].x) ** 2 +
                                     (self.cities[route.genes[i]].y - self.cities[route.genes[i+1]].y) ** 2)

            route.fitness = (1 / distance_sum) * 10**3
            self.best = route if route.fitness > self.best.fitness else self.best

    def selection(self):
        fitness_sum = 0
        for route in self.population:
            fitness_sum += route.fitness
            
        pool = []
        for route in self.population:
            # factor = 1000 // arbitrary
            for i in range(int((route.fitness / fitness_sum) * 100)):
                pool.append(route.genes)

        return pool

    @staticmethod
    def reproduction(pool):
        """a, b = randint(0, len(pool) - 1), randint(0, len(pool) - 1)
        child = Route.multiple_crossover(pool[a], pool[b])
        print(child)
        return child"""
        a = randint(0, len(pool) - 1)
        return Route.mutation(pool[a], C.mutation_rate)

    def new_generation(self, pool):
        pop_new = []

        while len(pop_new) < self.max_population:
            pop_new.append(Route(Population.reproduction(pool), 0))
        return pop_new

    def update(self):
        self.calculate_fitness()
        pool = self.selection()
        self.population = self.new_generation(pool)
        self.generation += 1

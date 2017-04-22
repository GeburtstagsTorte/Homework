from DNA import Individual
from Constants import C
from random import randint


class Population:

    population = []
    generation = 0
    best = object()
    average_fitness = 0

    def __init__(self, target, popmax, mutation_rate):
        self.target = target
        # popmax = number of individuals
        self.popmax = popmax
        # mutation rate in %
        self.mutation_rate = mutation_rate

        self.population = self.initialize_population()
        self.calc_fitness()
        self.best = self.calc_best_individual()
        # self.loop()

    def initialize_population(self):
        return [Individual.create_individual(C.target) for i in range(self.popmax)]

    def update(self):
        # former loop function
        # while self.best.fitness < 1:
        self.calc_fitness()
        self.best = self.calc_best_individual()
        self.average_fitness = self.calc_average_fitness()
        # self.info()

        pool = self.selection()
        self.population = self.new_generation(pool)
        self.generation += 1

    def calc_fitness(self):
        # relation, right letters in genome
        # fitness*100 in %
        for individual in self.population:
            score = 0
            for i, j in zip(individual.genes, self.target):
                score += 1 if i == j else 0
            individual.fitness = (score / len(self.target))

    def calc_average_fitness(self):
        score = 0
        for individual in self.population:
            score += individual.fitness
        return score / self.popmax

    def calc_best_individual(self):
        # sorted after key: fitness for every individual in population
        pop = sorted(self.population, key=lambda x: x.fitness, reverse=True)
        return pop[0]

    def selection(self):

        fitness_sum = 0
        for individual in self.population:
            fitness_sum += individual.fitness

        pool = []
        for individual in self.population:
            # factor = 1000
            for i in range(int((individual.fitness / fitness_sum) * 1000)):
                pool.append(individual)

        return pool

    def new_generation(self, pool):
        pop_new = []

        while len(pop_new) < self.popmax:
            pop_new.append(Individual(Population.reproduction(pool), 0, self.target))
        return pop_new

    @staticmethod
    def reproduction(pool):
        a, b = randint(0, len(pool) - 1), randint(0, len(pool) - 1)
        child = Individual.multiple_crossover(pool[a], pool[b])
        # other recombination types possible
        # in DNA file, crossover_mod1

        if randint(0, 100) < C.mutation_rate:
            return Individual.mutation(child)
        return child

    def info(self):
        """return self.best, self.calc_average_fitness()"""
        best_string = ""
        for i in self.best.genes:
            best_string += i

        print("Best individual: {} \n"
              "average fitness: {}% \n"
              "best fitness   : {}% \n"
              "generation     : {} \n"
              "mutation rate  : {}% \n"
              "Population     : {} \n".format(best_string, round(self.calc_average_fitness(), 3) * 100,
                                              round(self.best.fitness, 3) * 100, self.generation, self.mutation_rate,
                                              len(self.population)))


def main():
    Population(C.target, C.popmax, C.mutation_rate)

if __name__ == '__main__':
    main()

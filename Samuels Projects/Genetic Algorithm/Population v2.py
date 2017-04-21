from DNA import Individual
from Constants import C
from random import randint


class Population:

    population = []
    generation = 0
    best = object()

    def __init__(self, popmax, mutation_rate, target):
        self.popmax = popmax
        self.mutation_rate = mutation_rate
        self.target = target

        self.population = self.initialize_population()
        self.calc_fitness()
        self.best = self.calc_best_individual()
        self.loop()

    def loop(self):
        while self.best.fitness < 1:
            self.calc_fitness()
            self.best = self.calc_best_individual()

            self.info()

            pool = self.selection()
            self.population = self.new_generation(pool)
            self.generation += 1

    def initialize_population(self):
        population = [Individual.create_individual(self.target) for i in range(self.popmax)]
        return population

    def calc_fitness(self):

        for individual in self.population:
            score = 0
            for i, j in zip(individual.genes, self.target):
                score += 1 if i == j else 0
            individual.fitness = (score / len(self.target))

    def selection(self):
        fitness_sum = 0
        for individual in self.population:
            fitness_sum += individual.fitness

        pool = []
        for individual in self.population:
            for i in range(int((individual.fitness / fitness_sum) * 1000)):
                pool.append(individual)

        return pool

    @staticmethod
    def reproduction(pool):
        a, b = randint(0, len(pool) - 1), randint(0, len(pool) - 1)
        child = Individual.multiple_crossover(pool[a], pool[b])

        if randint(0, 100) < C.mutation_rate:
            return Individual.mutation(child)
        return child

    def new_generation(self, pool):
        pop_new = []

        while len(pop_new) < self.popmax:
            pop_new.append(Individual(Population.reproduction(pool), 0, self.target))
        return pop_new

    def calc_average_fitness(self):
        score = 0
        for individual in self.population:
            score += individual.fitness
        return score / self.popmax

    def calc_best_individual(self):
        pop = sorted(self.population, key=lambda x: x.fitness, reverse=True)
        return pop[0]

    def info(self):
        best_string = ""
        for i in self.best.genes:
            best_string += i

        print("Best individual: {} \n"
              "average fitness: {}% \n"
              "best fitness   : {}% \n"
              "generation     : {} \n"
              "mutation rate  : {}% \n".format(best_string, round(self.calc_average_fitness(), 3) * 100,
                                               round(self.best.fitness, 3) * 100, self.generation, self.mutation_rate))


# def main():
#     Population(C.popmax, C.mutation_rate, C.target)

# if __name__ == '__main__':
#     main()

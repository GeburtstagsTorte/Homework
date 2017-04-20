from DNA import Individuum
from Constants import C
from random import randint


def initialize_population(n):
    # ex.
    population = [Individuum.create_individuum(C.target) for i in range(n)]
    return population


def calc_fitness(population, target):

    for individuum in population:
        score = 0
        for i, j in zip(individuum.genes, target):
            score += 1 if i == j else 0
        individuum.fitness = score / len(target)


def generate_pool(population):
    fitness_sum = 0
    for individuum in population:
        fitness_sum += individuum.fitness

    pool = []
    for individuum in population:
        print(int((individuum.fitness / fitness_sum)*100))
        for i in range(int((individuum.fitness / fitness_sum)*100)):
            pool.append(individuum)

    return pool


def new_generation(population):
    pool = generate_pool(population)
    pop_new = []

    while len(pop_new) < C.popmax:
        a, b = randint(0, len(pool) - 1), randint(0, len(pool) - 1)
        child = Individuum.multiple_crossover(pool[a], pool[b])
        pop_new.append(Individuum(child, 0, C.target))
        # mutation
    return pop_new


def calc_avrg_fitness(population):
    score = 0
    for individuum in population:
        score += individuum.fitness
    return score / C.popmax


def main():
    generation = 0
    # step 1: initialize
    population = initialize_population(C.popmax)

    while population[0].fitness < 1.0:
        calc_fitness(population, C.target)
        population = sorted(population, key=lambda x: x.fitness, reverse=True)

        if population[0] == 0:
            population = initialize_population(C.popmax)
        best_individuum = ""
        for i in population[0].genes:
            best_individuum += i
        print(best_individuum, "\n",
              population[0].fitness, "\n",
              generation, "\n")

        population = new_generation(population)
        generation += 1


if __name__ == '__main__':
    main()

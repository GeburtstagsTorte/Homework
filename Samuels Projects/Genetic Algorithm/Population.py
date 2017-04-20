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
        individuum.fitness = (score / len(target))

    return sorted(population, key=lambda x: x.fitness, reverse=True)


def selection(population):

    fitness_sum = 0
    for individuum in population:
        fitness_sum += individuum.fitness

    pool = []
    for individuum in population:
        for i in range(int((individuum.fitness / fitness_sum) * 1000)):
            pool.append(individuum)

    return pool


def reproduction(pool):
    a, b = randint(0, len(pool)-1), randint(0, len(pool)-1)
    child = Individuum.multiple_crossover(pool[a], pool[b])

    if randint(0, 100) < C.mutation_rate:
        Individuum.mutation(child)
    return child


def new_generation(pool):
    pop_new = []

    while len(pop_new) < C.popmax:
        pop_new.append(Individuum(reproduction(pool), 0, C.target))
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

    while population[0].fitness < 1:
        population = calc_fitness(population, C.target)
        best_indi = ""
        for i in population[0].genes:
            best_indi += i
        print("Best individuum: {} \n"
              "average fitness: {}% \n"
              "generation     : {} \n".format(best_indi, round(calc_avrg_fitness(population), 3)*100, generation))

        pool = selection(population)
        reproduction(pool)
        population = new_generation(pool)
        generation += 1
if __name__ == '__main__':
    main()

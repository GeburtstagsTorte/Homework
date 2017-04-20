from DNA import Individual
from Constants import C
from random import randint


def initialize_population(n):
    # ex.
    population = [Individual.create_individual(C.target) for i in range(n)]
    return population


def calc_fitness(population, target):

    for individual in population:
        score = 0
        for i, j in zip(individual.genes, target):
            score += 1 if i == j else 0
        individual.fitness = (score / len(target))

    return sorted(population, key=lambda x: x.fitness, reverse=True)


def selection(population):

    fitness_sum = 0
    for individual in population:
        fitness_sum += individual.fitness

    pool = []
    for individual in population:
        for i in range(int((individual.fitness / fitness_sum) * 1000)):
            pool.append(Individual)

    return pool


def reproduction(pool):
    a, b = randint(0, len(pool)-1), randint(0, len(pool)-1)
    child = Individual.multiple_crossover(pool[a], pool[b])

    if randint(0, 100) < C.mutation_rate:
        return Individual.mutation(child)
    return child


def new_generation(pool):
    pop_new = []

    while len(pop_new) < C.popmax:
        pop_new.append(Individual(reproduction(pool), 0, C.target))
    return pop_new


def calc_avrg_fitness(population):
    score = 0
    for individual in population:
        score += individual.fitness
    return score / C.popmax


def calc_max_fitness(population):

    pop = sorted(population, key=lambda x: x.fitness, reverse=True)
    return pop[0]


def main():
    generation = 0
    # step 1: initialize
    population = initialize_population(C.popmax)
    best = calc_max_fitness(population)

    while best.fitness < 1:
        population = calc_fitness(population, C.target)
        best_indi = ""
        for i in best.genes:
            best_indi += i

        calc_fitness(population, C.target)
        print("Best Individual: {} \n"
              "average fitness: {}% \n"
              "generation     : {} \n".format(best_indi, round(calc_avrg_fitness(population), 3)*100, generation))

        pool = selection(population)
        reproduction(pool)
        population = new_generation(pool)
        generation += 1
if __name__ == '__main__':
    main()

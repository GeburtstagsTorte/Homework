"""
Step 1:
    Initialize:
    Create a population of N elements, each with randomly generated DNA (genes)

    (drawing)

Step 2:
    Selection:
    Evaluate the fitness of each element of the population and create a pool (mating pool)

Step 3:
    Reproduction:
    a) Pick two parents with probability according to their relative fitness
    b) Replicate: create a child by combining the DNA of these two parents
    c) Mutation: mutate the child's DNA based on a given probability
    d) add new child to a new population

Step 4:
    New generation:
    Replace the old population with the new population and return to Step 2 until task is accomplished
"""


class Populations:

    population = []
    generation = 0
    # best = object
    # average_fitness = 0

    def __init__(self):
        pass

    def update(self):
        pass

    def calc_fitness(self):
        pass

    def calc_average_fitness(self):
        pass

    def calc_best_individual(self):
        pass

    def selection(self):
        pass

    def reproduction(self):
        pass

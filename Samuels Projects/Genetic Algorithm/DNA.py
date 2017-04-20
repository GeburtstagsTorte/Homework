from Constants import C
from random import randint


class Individual:

    def __init__(self, genes, fitness, target):
        self.genes = genes
        self.fitness = fitness
        self.target = target

    @staticmethod
    def create_individual(target):
        # 32 - 126

        genes = []
        for i in range(len(target)):
            genes.append(chr(randint(32, 126)))

        return Individual(genes, 0, C.target)

    @staticmethod
    def multiple_crossover(a, b):
        child = []
        for char in range(len(C.target)):
            choose = randint(0, 1)
            child.append(a.genes[char]) if choose else child.append(b.genes[char])
        return child

    @staticmethod
    def crossover_mod1(a, b):
        choose = randint(0, 1)
        if choose:
            child = a.genes[:len(C.target)//2:] + b.genes[len(C.target)//2::]
        else:
            child = b.genes[:len(C.target) // 2:] + a.genes[len(C.target) // 2::]
        return child

    @staticmethod
    def mutation(genes):
        choose = randint(0, len(genes) - 1)
        genes[choose] = chr(randint(32, 126))
        return genes

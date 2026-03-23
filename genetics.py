class DNA:
    def __init__(self, genes):
        self.genes = genes

    def crossover(self, partner):
        child_genes = []
        midpoint = len(self.genes) // 2
        child_genes.extend(self.genes[:midpoint])
        child_genes.extend(partner.genes[midpoint:])
        return DNA(child_genes)

    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                self.genes[i] = random.choice(range(100)) # example mutation

    def fitness(self):
        return sum(self.genes) # simple fitness evaluation

import random

# Example usage:
# parent1 = DNA([1, 2, 3, 4, 5])
# parent2 = DNA([5, 4, 3, 2, 1])
# child = parent1.crossover(parent2)
# child.mutate(0.01)

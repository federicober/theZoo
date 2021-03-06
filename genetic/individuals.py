from genetic.genes import AbstractGene

from copy import deepcopy
import numpy as np
from typing import Sequence


class Individual:
    def __init__(self, genome: Sequence[AbstractGene]):
        self._genome = np.array(genome)

        if len(self._genome.shape) == 0 or self._genome.shape[0] == 0:
            raise ValueError(f"genes must be a non-empty iterable, received {genome}")

    @property
    def genome(self):
        return deepcopy(self._genome)

    def mutate(self, mutation_probability: float):
        for gene in self._genome:
            if np.random.rand(1) <= mutation_probability:
                gene.mutate()

    def __add__(self, other):
        return Individual(self._genome + other.genome)

    def __eq__(self, other):
        return (self._genome == other.genome).all()

    def __str__(self):
        return f"|{'|'.join(map(str, self._genome))}|"

    def __repr__(self):
        return f"Individual(({', '.join(map(repr, self._genome))}))"

    def copy(self):
        return Individual(self.genome)

    def randomize(self):
        for gene in self._genome:
            gene.randomize()

    def random_copy(self):
        new_individual = self.copy()
        new_individual.randomize()
        return new_individual

    @property
    def values(self):
        return np.array([gene.value for gene in self._genome])


def easy_individual(genes):
    all_genes_dict = {}

    for gene_type in AbstractGene.__subclasses__():
        all_genes_dict[gene_type.base_type] = gene_type

    return Individual([all_genes_dict[gene]() if isinstance(gene, type) else all_genes_dict[type(gene)](gene)
                       for gene in genes])

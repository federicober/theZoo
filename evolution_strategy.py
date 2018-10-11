from chromosomes import Chromosome

import heapq
import abc
from typing import Sequence
import numpy as np


class EvolutionStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def evolve(self, species: Sequence[Chromosome], performances: Sequence[float]) -> Sequence[Chromosome]:
        pass


class BasicEvolutionStrategy(EvolutionStrategy):
    def __init__(self, mutation_probability: float, elitism: int or bool):
        self.mutation_probability = mutation_probability
        self.elitism = int(elitism)

    @staticmethod
    def perf2prob(performances: Sequence[float]) -> Sequence[float]:
        probabilities = np.array(performances)
        probabilities[np.isnan(probabilities)] = 0
        probabilities[probabilities < 0] = 0
        probabilities = probabilities / np.nansum(probabilities)
        return probabilities

    def get_elite(self, species: Sequence, ordering: Sequence[float]) -> Sequence:
        if self.elitism == 0:
            return []

        best_species, best_perfs = zip(*heapq.nlargest(self.elitism, zip(species, ordering), key=lambda x: x[1]))
        return list(best_species)

    def evolve(self, species: Sequence[Chromosome], performances: Sequence[float]) -> Sequence[Chromosome]:
        number_of_species = len(species)

        probabilities = self.perf2prob(performances)

        new_generation = self.get_elite(species, probabilities)
        for i in range(number_of_species - len(new_generation)):
            new_specie = Chromosome.__add__(*np.random.choice(species, size=2, p=probabilities))

            new_specie.mutate(self.mutation_probability)

            new_generation.append(new_specie)

        return new_generation

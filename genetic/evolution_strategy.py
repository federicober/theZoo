from genetic.individuals import Individual

import heapq
import abc
from typing import Sequence, List
import numpy as np


class AbstractEvolutionStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def crossover(self, individuals: Sequence[Individual], fitness: Sequence[float]) -> Sequence[Individual]:
        pass


class ElitismEvolution(AbstractEvolutionStrategy):
    def __init__(self, mutation_probability: float, elitism: int or bool):
        self.mutation_probability = mutation_probability
        self.elitism = int(elitism)

    @staticmethod
    def fitness2prob(fitness: Sequence[float]) -> Sequence[float]:
        probabilities = np.array(fitness)
        probabilities[np.isnan(probabilities)] = 0
        probabilities[probabilities < 0] = 0
        probabilities = probabilities / np.nansum(probabilities)
        return probabilities

    def get_elite(self, species: Sequence, fitness: Sequence[float]) -> List:
        if self.elitism == 0:
            return []

        best_species, _ = zip(*heapq.nlargest(self.elitism, zip(species, fitness), key=lambda x: x[1]))
        return list(best_species)

    def crossover(self, individuals: Sequence[Individual], fitness: Sequence[float]) -> Sequence[Individual]:
        number_of_species = len(individuals)

        probabilities = self.fitness2prob(fitness)

        new_generation = self.get_elite(individuals, probabilities)
        for i in range(number_of_species - len(new_generation)):
            new_specie = Individual.__add__(*np.random.choice(individuals, size=2, p=probabilities))

            new_specie.mutate(self.mutation_probability)

            new_generation.append(new_specie)

        return new_generation


class BasicEvolution(ElitismEvolution):
    def __init__(self, mutation_probability: float):
        super().__init__(mutation_probability, 0)

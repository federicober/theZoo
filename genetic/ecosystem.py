from genetic.individuals import Individual, easy_individual
from genetic.evolution_strategy import AbstractEvolutionStrategy, ElitismEvolution

from typing import Callable
import numpy as np


class Ecosystem:
    def __init__(self,
                 model_genome: Individual,
                 n_individuals: int or Callable,
                 fitness_function: Callable,
                 mutation_probability: float = 0,
                 elitism: float or bool = 0,
                 n_generations: int = None,
                 evolution_strategy: AbstractEvolutionStrategy = None):
        self._model_genome = model_genome
        if evolution_strategy is None:
            self._evolution_strategy = ElitismEvolution(mutation_probability, elitism)
        else:
            self._evolution_strategy = evolution_strategy
        self._n_individuals = n_individuals
        self._fitness_function = fitness_function

        self._history = History()
        self.generation_number = 0
        self.current_generation = []
        self.clear()

        if n_generations:
            self.nth_generation(n_generations)

    def fitness(self, individual):
        return self._fitness_function(individual)

    def clear(self):
        self.generation_number = 0
        self._history.clear()

        try:
            n_individuals = self._n_individuals(0)
        except TypeError:
            n_individuals = self._n_individuals

        self.current_generation = [self._model_genome.random_copy() for i in range(n_individuals)]

    def next_generation(self):
        fitness = [self._fitness_function(ind.values) for ind in self.current_generation]
        self.current_generation = self._evolution_strategy.crossover(self.current_generation, fitness)
        self._history.append(self.current_generation, fitness)

    def nth_generation(self, n):
        for i in range(n):
            print('Generation number', i, end='\r')
            self.next_generation()

    @property
    def history(self):
        return self._history  # .copy()


class History:
    def __init__(self):
        self._history = []
        self.clear()

    def clear(self):
        self._history.clear()

    def copy(self):
        pass

    def append(self, individuals, fitness):
        self._history.append(Generation(individuals, fitness))

    def max(self):
        return (generation.max() for generation in self._history)

    def best(self, n=1):
        return (generation.best(n) for generation in self._history)

    def mean(self):
        return (generation.mean() for generation in self._history)

    def std(self):
        return (generation.std() for generation in self._history)


class Generation:
    def __init__(self, individuals, fitness):
        self._ordered = False
        for ind, fit in zip(individuals, fitness):
            ind.fitness = fit
        self._individuals = individuals
        self._fitness = fitness

    def copy(self):
        raise NotImplementedError()

    def _order(self):
        self._individuals.sort(key=lambda x: x.individuals)

    def max(self):
        if self._ordered:
            return self._individuals[0].fitness
        return max(self._fitness)

    def best(self, n=1):
        if self._ordered:
            self._order()

        if n == 1:
            return self._individuals[0]
        return self._individuals[:n]

    def mean(self):
        return np.mean(self._fitness)

    def std(self):
        return np.std(self._fitness)

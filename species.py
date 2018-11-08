from chromosomes import Chromosome
from evolution_strategy import EvolutionStrategy


class Species:
    def __init__(self, chromosome: Chromosome, evolution_strategy: EvolutionStrategy, n_chromosomes: int or function):
        self._model_chromosome = chromosome
        self._evolution_strategy = evolution_strategy
        self._n_chromosomes = n_chromosomes

        self._history = []
        self.generation_number = 0
        self.current_generation = []
        self.clear()

    def clear(self):
        self.generation_number = 0
        self._history = []

        try:
            n_chromosomes = self._n_chromosomes(0)
        except TypeError:
            n_chromosomes = self._n_chromosomes

        self.current_generation = [self._model_chromosome for i in range(n_chromosomes)]

    def next_generation(self):
        pass
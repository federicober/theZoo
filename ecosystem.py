from individuals import Individual
from evolution_strategy import EvolutionStrategy


class Ecosystem:
    def __init__(self,
                 model_genome: Individual,
                 evolution_strategy: EvolutionStrategy,
                 n_individuals: int or function,
                 fitness_function):
        self._model_genome = model_genome
        self._evolution_strategy = evolution_strategy
        self._n_individuals = n_individuals
        self._fitness_function = fitness_function

        self._history = []
        self.generation_number = 0
        self.current_generation = []
        self.clear()

    def fitness(self, individual):
        return self._fitness_function(individual)

    def clear(self):
        self.generation_number = 0
        self._history = []

        try:
            n_individuals = self._n_individuals(0)
        except TypeError:
            n_individuals = self._n_individuals

        self.current_generation = [self._model_genome.random_copy() for i in range(n_individuals)]

    def next_generation(self):
        fitness = [self._fitness_function(ind) for ind in self.current_generation]
        self.current_generation = self._evolution_strategy.evolve(self.current_generation, fitness)
        self._history.append(fitness)

    def nth_generation(self, n):
        for i in range(n):
            print('Generation number', i, end='\r')
            self.next_generation()

    @property
    def history(self):
        return self._history.copy()


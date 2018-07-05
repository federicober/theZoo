from chromosomes import *
import heapq


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

    def evolve(self, species: Sequence[Chromosome], performances: Sequence[float]) -> Sequence[Chromosome]:
        number_of_species = len(species)

        probabilities = self.perf2prob(performances)

        new_generation = []
        for i in range(number_of_species):
            new_specie = Chromosome.__add__(*np.random.choice(species, size=2, p=probabilities))

            new_specie.mutate(self.mutation_probability)

            new_generation.append(new_specie)

        return new_generation

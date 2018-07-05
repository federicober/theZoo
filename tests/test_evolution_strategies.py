from evolution_strategy import *

from tests.my_test_case import MyNumpyTest


class TestBasicEvolutionStrategy(MyNumpyTest):
    def test_perf2prob(self):
        self.assertArrayEqual(np.array([0.2, 0.3, 0.5]), BasicEvolutionStrategy.perf2prob([2, 3, 5]))

    def test_perf2prob_with_nan(self):
        self.assertArrayEqual(np.array([0.2, 0.3, 0, 0.5]), BasicEvolutionStrategy.perf2prob([2, 3, np.nan, 5]))

    def test_perf2prob_with_negative(self):
        self.assertArrayEqual(np.array([0.2, 0.3, 0, 0.5]), BasicEvolutionStrategy.perf2prob([2, 3, -1, 5]))

    def test_evolve_no_mutation_no_elitism_single_performance_specie(self):
        n = 100
        genes = [bool] * 6
        evolution = BasicEvolutionStrategy(0, 0).evolve

        species = [easy_chromosome(*genes) for i in range(n)]
        good_specie = species[0]

        performances = [1] + [0] * (n - 1)

        next_generation = evolution(species, performances)

        for specie in next_generation:
            self.assertEqual(good_specie, specie)

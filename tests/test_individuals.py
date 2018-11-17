import unittest
import numpy as np

from individuals import Individual, easy_individual
from genes import BinaryGene


class TestIndividualClass(unittest.TestCase):
    def test_create_simple_individual(self):
        self.assertIsInstance(Individual((BinaryGene(), BinaryGene())), Individual)

    def test_empty_individual_should_fail(self):
        with self.assertRaises(ValueError):
            Individual(())

    def test_repr_with_small_individual(self):
        c = easy_individual(bool, bool, bool)
        self.assertEqual(eval(repr(c)), c)

    def test_copy(self):
        first_genome = Individual((BinaryGene(True), BinaryGene(False), BinaryGene(False), BinaryGene(True)))
        second_genome = first_genome.copy()
        self.assertEqual(first_genome, second_genome)
        for i in range(10):
            second_genome.randomize()
            if first_genome != second_genome:
                break
        self.assertNotEqual(first_genome, second_genome)

    def test_random_copy(self):
        first_genome = Individual((BinaryGene(True), BinaryGene(False), BinaryGene(False), BinaryGene(True)))
        second_genome = None
        for i in range(10):
            second_genome = first_genome.random_copy()
            if first_genome != second_genome:
                break
        self.assertNotEqual(first_genome, second_genome)


class TestBinaryGenome(unittest.TestCase):
    @staticmethod
    def get_all_equal(value: bool, n: int):
        return Individual([BinaryGene(value) for i in range(n)])

    def test_equals_two_equal_individuals_should_return_true(self):
        self.assertTrue(Individual((BinaryGene(True), BinaryGene(False), BinaryGene(False), BinaryGene(True))) ==
                        Individual((BinaryGene(True), BinaryGene(False), BinaryGene(False), BinaryGene(True))))

    def test_add_two_individuals_size_4_all_true_should_return_all_true(self):
        self.assertEqual(self.get_all_equal(True, 4) + self.get_all_equal(True, 4), self.get_all_equal(True, 4))

    def test_add_two_individuals_size_4_all_false_should_return_all_false(self):
        self.assertEqual(self.get_all_equal(False, 4) + self.get_all_equal(False, 4), self.get_all_equal(False, 4))

    def test_add_two_individuals_size_4_all_true_and_all_false_should_return_new(self):
        np.random.seed(42)
        self.assertEqual(self.get_all_equal(False, 4) + self.get_all_equal(True, 4),
                         Individual((BinaryGene(False), BinaryGene(True), BinaryGene(True), BinaryGene(True))))


class TestIndividualClassMethods(unittest.TestCase):
    def test_easy_individuals_should_return_individual(self):
        self.assertIsInstance(easy_individual(bool, bool), Individual)

    def test_easy_individual_with_two_bool_should_return_individual_with_two_binary(self):
        np.random.seed(42)
        self.assertEqual(easy_individual(bool, bool), Individual((BinaryGene(False), BinaryGene(True))))

    def test_easy_individual_with_true_false_should_return_individual_binaries_true_false(self):
        self.assertEqual(easy_individual(True, False), Individual((BinaryGene(True), BinaryGene(False))))

    def test_easy_individual_with_bool_false_should_return_individual_binaries_true_false(self):
        np.random.seed(42)
        self.assertEqual(easy_individual(bool, False), Individual((BinaryGene(False), BinaryGene(False))))


if __name__ == "__main__":
    unittest.main()

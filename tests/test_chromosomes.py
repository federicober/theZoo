import unittest

from chromosomes import *


class TestChromosomeClass(unittest.TestCase):
    def test_create_simple_chromosome(self):
        self.assertIsInstance(Chromosome((BinaryGene(), BinaryGene())), Chromosome)

    def test_empty_chromosome_should_fail(self):
        with self.assertRaises(ValueError):
            Chromosome(())

    def test_repr_with_small_chromosome(self):
        c = easy_chromosome(bool, bool, bool)
        self.assertEqual(eval(repr(c)), c)


class TestBinaryChromosome(unittest.TestCase):
    def test_equals_two_equal_chromosomes_should_return_true(self):
        self.assertTrue(Chromosome((BinaryGene(True), BinaryGene(False), BinaryGene(False), BinaryGene(True))) ==
                        Chromosome((BinaryGene(True), BinaryGene(False), BinaryGene(False), BinaryGene(True))))

    def test_add_two_chromosomes_size_4_all_true_should_return_all_true(self):
        self.assertEqual(Chromosome((BinaryGene(True), BinaryGene(True), BinaryGene(True), BinaryGene(True))) +
                         Chromosome((BinaryGene(True), BinaryGene(True), BinaryGene(True), BinaryGene(True))),
                         Chromosome((BinaryGene(True), BinaryGene(True), BinaryGene(True), BinaryGene(True))))


class TestChromosomeMethods(unittest.TestCase):
    def test_easy_chromosomes_should_return_chromosome(self):
        self.assertIsInstance(easy_chromosome(bool, bool), Chromosome)

    def test_easy_chromosome_with_two_bool_should_return_chromosome_with_two_binary(self):
        np.random.seed(42)
        self.assertEqual(easy_chromosome(bool, bool), Chromosome((BinaryGene(False), BinaryGene(True))))

    def test_easy_chromosome_with_true_false_should_return_chromosome_binaries_true_false(self):
        self.assertEqual(easy_chromosome(True, False), Chromosome((BinaryGene(True), BinaryGene(False))))

    def test_easy_chromosome_with_bool_false_should_return_chromosome_binaries_true_false(self):
        np.random.seed(42)
        self.assertEqual(easy_chromosome(bool, False), Chromosome((BinaryGene(False), BinaryGene(False))))


if __name__ == "__main__":
    unittest.main()

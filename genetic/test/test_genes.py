import unittest

from genetic.genes import *


class TestBinaryGene(unittest.TestCase):
    def test_simple_reproduction_between_true_and_true_should_return_true(self):
        self.assertEqual(True, (BinaryGene(True) + BinaryGene(True)).value)

    def test_simple_reproduction_between_false_and_false_should_return_false(self):
        self.assertEqual(False, (BinaryGene(False) + BinaryGene(False)).value)

    def test_simple_reproduction_between_false_and_true_with_small_random_should_return_false(self):
        np.random.seed(42)
        self.assertEqual(False, (BinaryGene(False) + BinaryGene(True)).value)

    def test_simple_reproduction_between_false_and_true_with_big_random_should_return_true(self):
        np.random.seed(25)
        self.assertEqual(True, (BinaryGene(False) + BinaryGene(True)).value)

    def test_equal_true_and_true_should_return_true(self):
        self.assertTrue(BinaryGene(True) == BinaryGene(True))


class TestEasyGene(unittest.TestCase):
    def test_easy_gene_with_bool_should_return_binary_gene_1(self):
        self.assertIsInstance(easy_gene(bool), BinaryGene)

    def test_easy_gene_with_bool_should_return_binary_gene_2(self):
        np.random.seed(42)
        self.assertEqual(easy_gene(bool), BinaryGene(False))

    def test_easy_gene_with_false_should_return_binary_gene_false(self):
        self.assertEqual(easy_gene(False), BinaryGene(False))

    def test_easy_gene_with_true_should_return_binary_gene_true(self):
        self.assertEqual(easy_gene(True), BinaryGene(True))


if __name__ == "__main__":
    unittest.main()

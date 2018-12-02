import unittest

from genetic.genes import *


class TestAbstractGeneMethods(unittest.TestCase):
    def test_copy(self):
        first_gene = BooleanGene()
        second_gene = first_gene.copy()
        self.assertEqual(first_gene, second_gene)
        for i in range(10):
            second_gene.randomize()
            if first_gene != second_gene:
                break
        self.assertNotEqual(first_gene, second_gene)

    def test_randomize_with_boolean_gene(self):
        gene = BooleanGene()
        inner_value = gene.value
        new_inner_value = inner_value
        for i in range(10):
            gene.randomize()
            new_inner_value = gene.value
            if inner_value != new_inner_value:
                break
        self.assertNotEqual(inner_value, new_inner_value)

    def test_randomize_with_categorical_gene(self):
        gene = CategoricalGene(10)
        inner_value = gene.value
        new_inner_value = inner_value
        for i in range(10):
            gene.randomize()
            new_inner_value = gene.value
            if inner_value != new_inner_value:
                break
        self.assertNotEqual(inner_value, new_inner_value)

    def test_eq_when_both_genes_are_equal(self):
        self.assertEqual(BooleanGene(True) == BooleanGene(True), True)

    def test_eq_when_genes_are_different(self):
        self.assertEqual(BooleanGene(True) == BooleanGene(False), False)

    def test_eq_when_genes_are_different_with_categorical_gene(self):
        self.assertEqual(CategoricalGene(4, 1) == CategoricalGene(4, 2), False)

    def test_eq_when_different_types(self):
        with self.assertRaises(TypeError):
            BooleanGene().__eq__(CategoricalGene(4))


class TestBooleanGene(unittest.TestCase):
    def test_simple_reproduction_between_true_and_true_should_return_true(self):
        self.assertEqual(True, (BooleanGene(True) + BooleanGene(True)).value)

    def test_simple_reproduction_between_false_and_false_should_return_false(self):
        self.assertEqual(False, (BooleanGene(False) + BooleanGene(False)).value)

    def test_simple_reproduction_returns_boolean_gene(self):
        self.assertIsInstance(BooleanGene(False) + BooleanGene(True), BooleanGene)

    def test_equal_true_and_true_should_return_true(self):
        self.assertTrue(BooleanGene(True) == BooleanGene(True))

    def test_inner_value_is_always_boolean(self):
        for i in range(10):
            self.assertIsInstance(BooleanGene().value, bool)


class TestCategoricalGene(unittest.TestCase):
    def test_add_with_two_equal_genes(self):
        self.assertEqual(CategoricalGene(4, 1) + CategoricalGene(4, 1), CategoricalGene(4, 1))

    def test_add_with_different_values(self):
        new_gene = CategoricalGene(4) + CategoricalGene(4)
        self.assertIsInstance(new_gene, CategoricalGene)
        self.assertEqual(new_gene._n_categories, 4)

    def test_random_value(self):
        n_cat = 10
        for i in range(10):
            self.assertLessEqual(CategoricalGene(n_cat).value, n_cat)

    def test_inner_value_is_always_int(self):
        for i in range(10):
            self.assertIsInstance(CategoricalGene(np.random.randint(1, 100)).value, int)


class TestEasyGene(unittest.TestCase):
    def test_easy_gene_with_bool_should_return_boolean_gene_1(self):
        self.assertIsInstance(easy_gene(bool), BooleanGene)

    def test_easy_gene_with_false_should_return_boolean_gene_false(self):
        self.assertEqual(easy_gene(False), BooleanGene(False))

    def test_easy_gene_with_true_should_return_boolean_gene_true(self):
        self.assertEqual(easy_gene(True), BooleanGene(True))


if __name__ == "__main__":
    unittest.main()

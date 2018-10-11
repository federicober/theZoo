import unittest
import numpy as np


class MyNumpyTest(unittest.TestCase):
    def assertEqualShape(self, array1, array2):
        self.assertSequenceEqual(
            array1.shape, array2.shape,
            f"array1 {array1.shape} and array2 {array2.shape} don't have the same shape")

    def assertArrayEqual(self, array1, array2):
        self.assertEqualShape(array1, array2)

        if (len(array1.shape) == 1 and array1.shape[0] < 10) or (array1.shape[0] == 1 and array1.shape[1] < 10):
            message = f"{array1} is not equal to {array2}"
        else:
            indexes = np.where(array1 != array2)
            message = f"Elements {array1[indexes]} in the indexes {list(zip(*indexes))} " \
                      f"are not equal to {array2[indexes]}"

        self.assertTrue((array2 == array1).all(), message)

def MyIterablesTest(MyNumpyTest):
    def assertSameContent(self, iterable1, iterable2):
        self.assertSetEqual(set(iterable1), set(iterable2), f"{iterable1} and {iterable2} do not have the same content")

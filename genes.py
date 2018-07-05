import abc

import numpy as np


class Gene(metaclass=abc.ABCMeta):
    base_type = type

    def __init__(self, value):
        if value is None:
            self._inner = self._random_value()
        else:
            self._inner = self.base_type(value)

    @property
    def value(self):
        return self._inner

    @abc.abstractclassmethod
    def _random_value(self):
        pass

    def __str__(self):
        return str(self._inner)

    def __repr__(self):
        return f"{type(self).__name__}({repr(self._inner)})"

    def __eq__(self, other):
        if type(self) != type(other):
            raise TypeError("== between %s and %s is not supported", type(self).__name__, type(other).__name__)
        return self.value == other.value


class BinaryGene(Gene):
    base_type = bool

    def __init__(self, value=None):
        super().__init__(value)

    @classmethod
    def _random_value(cls):
        if np.random.rand() < 0.5:
            return False
        else:
            return True

    def __add__(self, other):
        if self.value == other.value:
            return BinaryGene(self.value)
        else:
            return BinaryGene()


def easy_gene(type_or_value):
    if isinstance(type_or_value, type):
        base_type = type_or_value
        value = None
    else:
        base_type = type(type_or_value)
        value = type_or_value

    for gene_type in Gene.__subclasses__():
        if base_type is gene_type.base_type:
            return gene_type(value)
    else:
        raise ValueError(f"Could find a Gene of base type {base_type}")

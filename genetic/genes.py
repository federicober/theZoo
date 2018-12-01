import abc

import numpy as np


class AbstractGene(metaclass=abc.ABCMeta):
    """
    Genes are the main components of Genomes.

    The AbstractGene API allows to easily create custom Genes, as well as providing a clear model for how pre-built
    genes behave.

    Every Gene is an enhanced "container" for a single value. A value is the usable variable when interpreting the
    Genome as a solution to fitness function. E.g. for a BooleanGene, its inner value is a boolean, and a genome
    composed only of BooleanGene, will be interpreted as an array of boolean values. A simple variable may not be
    considered as a gene because it need some "instructions" to mutate and evolve, these are provided by the functions
     bellow.

    A Gene must have two main functions to be used as an actual gene.
    - The first is the function that returns a random value, of the same type as the Gene. This allows to create the
     gene with an empty constructor, and to mutate the gene by randomizing its value.
    - The second is the function that crosses two different Genes of the same type to form a new gene. This evolution
    or crossover function is found in the __add__() method of the class.
    """
    base_type = type

    def __init__(self, value=None):
        if value is None:
            self._inner = self.random_value()
        else:
            self._inner = self.base_type(value)

    @property
    def value(self):
        return self._inner

    @classmethod
    @abc.abstractmethod
    def random_value(cls):
        pass

    def random(self):
        return type(self)(self.random_value())

    @abc.abstractmethod
    def __add__(self, other):
        pass

    def mutate(self):
        self._inner = self.random_value()

    def __str__(self):
        return str(self._inner)

    def __repr__(self):
        return f"{type(self).__name__}({repr(self._inner)})"

    def __eq__(self, other):
        if type(self) != type(other):
            raise TypeError("== between %s and %s is not supported", type(self).__name__, type(other).__name__)
        return self.value == other.value


class BooleanGene(AbstractGene):
    base_type = bool

    def __init__(self, value=None):
        super().__init__(value)

    @classmethod
    def random_value(cls):
        if np.random.rand() < 0.5:
            return False
        else:
            return True

    def __add__(self, other):
        if self.value == other.value:
            return BooleanGene(self.value)
        else:
            return BooleanGene()


def easy_gene(type_or_value):
    if isinstance(type_or_value, type):
        base_type = type_or_value
        value = None
    else:
        base_type = type(type_or_value)
        value = type_or_value

    for gene_type in AbstractGene.__subclasses__():
        if base_type is gene_type.base_type:
            return gene_type(value)
    else:
        raise ValueError(f"Could find a AbstractGene of base type {base_type}")

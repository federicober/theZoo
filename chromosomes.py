from genes import *


class Chromosome:
    def __init__(self, genes):
        self._genes = np.array(genes)

        if len(self._genes.shape) == 0 or self._genes.shape[0] == 0:
            raise ValueError(f"genes must be a non-empty iterable, received {genes}")

    @property
    def genes(self):
        return self._genes.copy()

    def __add__(self, other):
        return Chromosome(self._genes + other.genes)

    def __eq__(self, other):
        return (self._genes == other.genes).all()

    def __str__(self):
        return f"|{'|'.join(map(str, self._genes))}|"

    def __repr__(self):
        return f"Chromosome(({', '.join(map(repr, self._genes))}))"


def easy_chromosome(*genes):
    all_genes_dict = {}

    for gene_type in Gene.__subclasses__():
        all_genes_dict[gene_type.base_type] = gene_type

    return Chromosome([all_genes_dict[gene]() if isinstance(gene, type) else all_genes_dict[type(gene)](gene)
                       for gene in genes])

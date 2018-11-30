#Genetic algorithms
This package is dedicated to the easy creation and utilisation of genetic algorithms. A genetic algorithm in and algorithm 
is a meta-heuristic that can be used in optimization problems.

## What is a genetic algorithm?
The main objective on genetic algorithms is to iteratively improve the solution to the problem 
by following the same path as evolution and natural selection.

The algorithm starts by generating a set if random solutions, and updating this set iteratively according to the following 
process. Each iteration is divided in three main stages:
1. Selection
2. Crossover
3. Mutation

In the selection stage, all the current solutions (also called individuals or species) are rated by a function (called the fitness function).
The individuals with higher fitness get a better chance of being selected to the next stage.

In the Crossover (or evolution stage), the individuals chosen during the last stage are arranged in pairs.
Each pair is then "mixed" to generate a new possible solutions.
In the hopes that individuals created by to high-fitness "parents" should also have a high fitness.
The ensemble of the new individuals are called the offspring or the nex generation.

Finally, some randomly-chosen individuals of the new offspring are mutated. This means that they are randomly modified or "tweaked",
and that maybe some of this modified individuals will find better solutions that were further than the ones their parent did.

Then the process is repeated again, until it produces some satisfactory solution.

Their are many modifications to this basic process, like elitism and speciation.

## How to use a genetic algorithm?
The main condition to use a genetic algorithm, is the to encode every possible solution to the problem in an array-like object,
called genome, which is composed by genes.

Genes can almost anything depending on the problem. Their form and properties can vary, but there must be a way to crossover ("evolve" or "mixed") two different genes to produce a new one.
For example, to optimize a multi-variable function we can chose a genome composed of each variable in our hyperspace.
Similarly, to solve the famous knapsack problem or the travelling salesman problem, the genome can be composed of the choice of taking (or not) a determined edge (for the TSP) or object (knapsack problem).

## How to use this module?
The genetic algorithm is encapsulated in a OOP-like API, named `Ecosystem`.

The basic arguments for creating an `Ecosystem` object are:
 - A `Genome` object, containing an example of the genes.
 - An `fitness_function`, a callable object that takes as an argument the values of the genome and returns a fitness.
 - The hyper-parameters the `mutation_probability`, `n_individuas`.

### Genome and Genes
To created a `Genome` object, just pass as an argument an iterable object composed of `Gene` objects.

In the `genes` module, we offer different pre-built genes, like `BooleanGene`, `CategoricalGene`, `FloatGene`. However, different genes can 
be built by inheriting from the abstract class `AbstractGene`.

An `easy_genome()` function is also provided, to create genomes formed by prebuilt genes in a single line of code.

### Evolution Strategy
If you wish to create more complex strategies to crossover and evolve individuals, just create a custom class inherited from 
`AbstractEvolutionStrategy` or use one of the pre-built classes like `SpeciationEvolution` or `ElitismEvolution`.

You can just pass your EvolutionStrategy as a argument of your `Ecosystem`, and it will override all the other hyper-parameters 
like `mutation_probability` and `elitism`

## Examples
To see some examples of the API, please go to our examples section.
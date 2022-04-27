import unittest
import src.PopulationGenerator as PopulationGenerator

class TestAIPopulation (unittest.TestCase) :

    def test_population_creation(self) :
        size = 1000
        population = PopulationGenerator.generate_population(size)
        self.assertEqual(len(population), size, 'The population has not 1000 individuals.')

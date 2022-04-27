import unittest
import src.PopulationGenerator as PopulationGenerator

class TestAIPopulation (unittest.TestCase) :

    def setUp(self) :
        self.size = 1000
        self.population = PopulationGenerator.generate_population(self.size)

    def test_population_creation(self) :
        self.assertEqual(len(self.population), self.size, 'The population has not 1000 individuals.')
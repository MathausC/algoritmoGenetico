import unittest
import src.PopulationGenerator as PopulationGenerator

class TestAIPopulation (unittest.TestCase) :

    def setUp(self) :
        self.size = 1000
        self.population = PopulationGenerator.generate_population(self.size)

    def test_population_creation(self):
        self.assertEqual(len(self.population), self.size, 'The population has not 1000 individuals.')

    def test_element_type_generation(self):
        self.assertIsInstance(self.population[0], PopulationGenerator.Individual, "Os elementos da lista não são indivíduos.")

    def test_random_generation(self):
        cont = 1
        while cont < self.size:
            self.assertNotAlmostEqual(self.population[cont-1].x1, self.population[self.size - cont].x1)
            self.assertNotAlmostEqual(self.population[cont-1].x2, self.population[self.size - cont].x2)
            self.assertNotAlmostEqual(self.population[cont-1].x3, self.population[self.size - cont].x3)
            self.assertNotAlmostEqual(self.population[cont-1].x4, self.population[self.size - cont].x4)
            self.assertNotAlmostEqual(self.population[cont-1].x5, self.population[self.size - cont].x5)
            cont = cont + 1
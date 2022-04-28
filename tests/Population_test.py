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
            self.assertNotAlmostEqual(self.population[cont-1].xs[0], self.population[self.size - cont].xs[0])
            self.assertNotAlmostEqual(self.population[cont-1].xs[1], self.population[self.size - cont].xs[1])
            self.assertNotAlmostEqual(self.population[cont-1].xs[2], self.population[self.size - cont].xs[2])
            self.assertNotAlmostEqual(self.population[cont-1].xs[3], self.population[self.size - cont].xs[3])
            self.assertNotAlmostEqual(self.population[cont-1].xs[4], self.population[self.size - cont].xs[4])
            cont = cont + 1

    def test_individuos_results_not_none(self):
        cont = 0
        while cont < self.size:
            self.assertIsNotNone(self.population[cont].xs[0], "Um dos indivíduos não possui x1")
            self.assertIsNotNone(self.population[cont].xs[1], "Um dos indivíduos não possui x2")
            self.assertIsNotNone(self.population[cont].xs[2], "Um dos indivíduos não possui x3")
            self.assertIsNotNone(self.population[cont].xs[3], "Um dos indivíduos não possui x4")
            self.assertIsNotNone(self.population[cont].xs[4], "Um dos indivíduos não possui x5")
            self.assertIsNotNone(self.population[cont].peso, "Um dos indivíduos não possui peso")
            cont = cont + 1

    def test_random_number_generator(self):
        number1 = PopulationGenerator.get_random_number(100)
        number2 = PopulationGenerator.get_random_number(100)
        self.assertNotAlmostEqual(number1, number2, 'Os números gerados randomicamente são iguais')
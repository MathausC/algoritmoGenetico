import unittest
import src.GenerationsHistory as GenerationsHistory

class TestGeneration(unittest.TestCase):

    def setUp(self):
        self.size = 1000
        self.generation_object = GenerationsHistory.Generation(self.size)
        self.generation = self.generation_object.get_generation()

    def  test_generation_is_none(self):
        self.assertIsNotNone(self.generation, 'A geração é nula')

    def  test_generation_empty(self):
        self.assertEqual(len(self.generation), self.size, 'A geração não tem o mesmo tamanho que a anterior')

    def test_generation_size_after_turnment(self):
        self.assertEqual(len(self.generation), self.size, 'A geração não tem tamanho correto')
        self.generation_object.troneio()
        self.generation = self.generation_object.get_generation()
        self.assertEqual(len(self.generation), self.size, 'A geração não tem tamanho correto após o troneio')

    def test_best_ones_was_maintained(self):
        bestones = self.generation_object.get_tres_melhores()
        self.assertIn(bestones[0], self.generation, "Indivíduo 1 nunca esteve presente na geração")
        self.assertIn(bestones[1], self.generation, "Indivíduo 2 nunca esteve presente na geração")
        self.assertIn(bestones[2], self.generation, "Indivíduo 3 nunca esteve presente na geração")
        self.generation_object.troneio()
        self.generation = self.generation_object.get_generation()
        self.assertIn(bestones[0], self.generation, "Indivíduo 1 não foi adicionado a nova geração")
        self.assertIn(bestones[1], self.generation, "Indivíduo 2 não foi adicionado a nova geração")
        self.assertIn(bestones[2], self.generation, "Indivíduo 3 não foi adicionado a nova geração")
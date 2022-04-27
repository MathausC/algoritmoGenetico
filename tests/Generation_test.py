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
import unittest
import src.GenerationsHistory as GenerationsHistory

class TestGeneration(unittest.TestCase):

    def setUp(self):
        self.size = 1000
        self.generation = GenerationsHistory.Generation(self.size).getGeneration()

    def  test_generation_is_none(self):
        self.assertIsNotNone(self.generation, 'A geração é nula')

    def  test_generation_empty(self):
        self.assertEqual(len(self.generation), self.size, 'A geração não tem o mesmo tamanho que a anterior')
import unittest
import src.Inteligencia as IA

class TestingGeneticAlgoritm(unittest.TestCase):
    
    def setUp(self):
        self.size = 1000
        self.faixa = 1000
        self.mutacao = 10
        self.geracoes = 1000
        self.repeticao = 1000
        self.inteligencia_object = IA.Inteligencia(self.size, self.faixa, self.mutacao, self.geracoes)

    def test_getbest_of_all_generations(self):
        self.assertIsNotNone(self.inteligencia_object, "Classe não foi instaciada.")
        self.assertIsNotNone(self.inteligencia_object.generation_object, "Classe geraçãoi não foi instaciada.")

    def test_run_generarions(self):
        self.inteligencia_object.run_generations(self.repeticao)

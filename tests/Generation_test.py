import unittest
import src.GenerationsHistory as GenerationsHistory
import src.PopulationGenerator as PopulationGenerator

class TestGeneration(unittest.TestCase):

    def setUp(self):
        self.size = 1000
        self.mutacao = 10.0
        self.faixa = 100
        self.generation_object = GenerationsHistory.Generation(self.size, self.mutacao, self.faixa)
        self.generation = self.generation_object.get_generation()

    def test_procriar_return(self):
        parceiro1 = PopulationGenerator.Individual(1, 2, 3, 4, 5)
        parceiro2 = PopulationGenerator.Individual(5, 4, 3, 2, 1)
        i = self.generation_object.procriar(parceiro1, parceiro2, 10, True)
        self.assertIsNotNone(i, "Procriar está retornando um valor nulo")

    def  test_generation_is_none(self):
        self.assertIsNotNone(self.generation, 'A geração é nula')        
        for i in self.generation:
            self.assertIsNotNone(i, "Há pelo menos um elemento nulo na geração")
       
        self.generation_object.algoritmo_genetico(self.mutacao)
        self.generation = self.generation_object.get_generation()

        self.assertIsNotNone(self.generation, 'A geração se tornou nula após o algoritmo')
        cont  = 0
        for i in self.generation:
            if i is None:
                cont  = cont + 1

        self.assertEqual(0, cont, f"Foram encontrados {cont} individuaos nulos após o algoritmo")
    
    def  test_generation_empty(self):
        self.assertEqual(len(self.generation), self.size, 'A geração não tem o mesmo tamanho que a anterior')

    def test_generation_size_after_turnment(self):
        self.assertEqual(len(self.generation), self.size, 'A geração não tem tamanho correto')
        self.generation_object.algoritmo_genetico(self.mutacao)
        self.generation = self.generation_object.get_generation()
        self.assertEqual(len(self.generation), self.size, 'A geração não tem tamanho correto após o troneio')

    def test_best_ones_are_not_none(self):
        bestones = self.generation_object.get_tres_melhores()
        for i in bestones:
            self.assertIsNotNone(i, "Pelo menos um dos melhores é nulo")

    def test_best_ones_are_not_none_after_generation(self):
        bestones = self.generation_object.get_tres_melhores()
        for i in bestones:
            self.assertIsNotNone(i, "Pelo menos um dos melhores é nulo") 
       
        self.generation_object.algoritmo_genetico(self.mutacao)
        self.generation = self.generation_object.get_generation()

        bestones = self.generation_object.get_tres_melhores()
        for i in bestones:
            self.assertIsNotNone(i, "Pelo menos um dos melhores é nulo") 

    def test_best_ones_was_maintained(self):
        bestones = self.generation_object.get_tres_melhores()
        self.assertIn(bestones[0], self.generation, "Indivíduo 1 nunca esteve presente na geração")
        self.assertIn(bestones[1], self.generation, "Indivíduo 2 nunca esteve presente na geração")
        self.assertIn(bestones[2], self.generation, "Indivíduo 3 nunca esteve presente na geração")
        self.generation_object.algoritmo_genetico(self.mutacao)
        self.generation = self.generation_object.get_generation()
        self.assertIn(bestones[0], self.generation, "Indivíduo 1 não foi adicionado a nova geração")
        self.assertIn(bestones[1], self.generation, "Indivíduo 2 não foi adicionado a nova geração")
        self.assertIn(bestones[2], self.generation, "Indivíduo 3 não foi adicionado a nova geração")

    def test_assert_best_ones(self):
        bestones = self.generation_object.get_tres_melhores()
        self.assertGreaterEqual(bestones[0].peso, bestones[1].peso)
        self.assertGreaterEqual(bestones[1].peso, bestones[2].peso)
        for i in self.generation:
            self.assertGreaterEqual(bestones[0].peso, i.peso)
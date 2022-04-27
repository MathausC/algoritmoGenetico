import random
import src.PopulationGenerator as PopulationGenerator

class Generation:
    def __init__(self, size):
        self.size = size
        self.current_generation = PopulationGenerator.generate_population(size)

    def get_generation(self):
        return self.current_generation

    def troneio(self):
        new_generation = self.get_tres_melhores()

        while len(new_generation) < self.size:
            copy_generation = self.current_generation.copy()
         
            first = 0
            second = 0

            while first == second:
                first = random.randint(0, self.size-1)
                second = random.randint(0, self.size-1)

            parceiro1 = None

            if copy_generation[first].peso >= copy_generation[second].peso:
                parceiro1 = copy_generation.pop(first)
            else:
                parceiro1 = copy_generation.pop(second)

            first = 0
            second = 0

            while first == second:
                first = random.randint(0, self.size-2)
                second = random.randint(0, self.size-2)

            parceiro2 = None

            if copy_generation[first].peso >= copy_generation[second].peso:
                parceiro2 = copy_generation.pop(first)
            else:
                parceiro2 = copy_generation.pop(second)


            if self.size - len(new_generation) == 1:
                descendente1 = PopulationGenerator.Individual(parceiro1.x1, parceiro2.x2, parceiro1.x3, parceiro2.x4, parceiro1.x5)
                new_generation.append(descendente1)
            else:
                descendente1 = PopulationGenerator.Individual(parceiro1.x1, parceiro2.x2, parceiro1.x3, parceiro2.x4, parceiro1.x5)
                descendente2 = PopulationGenerator.Individual(parceiro2.x1, parceiro1.x2, parceiro2.x3, parceiro1.x4, parceiro2.x5)
                new_generation.append(descendente1)
                new_generation.append(descendente2)

        self.current_generation = new_generation

    def get_tres_melhores(self):
        primeiro = None
        segundo =None
        terceiro = None

        for i in self.current_generation:
            if primeiro == None:
                primeiro = i
            elif primeiro.peso < i.peso:
                terceiro = segundo
                segundo = primeiro
                primeiro = i
            elif segundo == None:
                segundo = i
            elif segundo.peso < i.peso:
                terceiro = segundo
                segundo = i
            elif terceiro == None:
                terceiro = i
            elif terceiro.peso < i.peso:
                terceiro = i
        
        return [primeiro, segundo, terceiro]
import random
import PopulationGenerator as PopulationGenerator

class Generation:
    def __init__(self, size, mutacao, faixa):
        self.size = size
        self.mutacao = mutacao
        self.faixa = faixa
        self.current_generation = PopulationGenerator.generate_population(size, faixa)
        self.melhores = self.get_tres_melhores()

    def get_generation(self):
        return self.current_generation

    def algoritmo_genetico(self, mutacao):
        new_generation = self.get_tres_melhores()

        while len(new_generation) < self.size:
            parceiros = self.torneio()

            if self.size - len(new_generation) == 1:
                descendente1 = self.procriar(parceiros[0], parceiros[1], mutacao, True)
                new_generation.append(descendente1)
            else:
                descendente1 = self.procriar(parceiros[0], parceiros[1], mutacao, True)
                descendente2 = self.procriar(parceiros[0], parceiros[1], mutacao, False)
                new_generation.append(descendente1)
                new_generation.append(descendente2)

        self.current_generation = new_generation

    def get_tres_melhores(self):
            primeiro = None
            segundo =None
            terceiro = None

            for i in self.current_generation:
                if primeiro is None:
                    primeiro = i
                elif primeiro.peso < i.peso:
                    terceiro = segundo
                    segundo = primeiro
                    primeiro = i
                elif segundo is None:
                    segundo = i
                elif segundo.peso < i.peso:
                    terceiro = segundo
                    segundo = i
                elif terceiro is None:
                    terceiro = i
                elif terceiro.peso < i.peso:
                    terceiro = i
            
            return [primeiro, segundo, terceiro]

    def procriar(self, parceiro1, parceiro2, mutacao, ordem):
        individuo = None

        if ordem:
            individuo = PopulationGenerator.Individual(parceiro1.xs[0], parceiro2.xs[1], parceiro1.xs[2], parceiro2.xs[3], parceiro1.xs[4])
        else:
            individuo = PopulationGenerator.Individual(parceiro2.xs[0], parceiro1.xs[1], parceiro2.xs[2], parceiro1.xs[3], parceiro2.xs[4])

        r = random.uniform(0, 100)

        if r <= mutacao:
            index = random.randrange(0, len(individuo.xs))
            individuo.xs[index] = random.uniform(-self.faixa, self.faixa)
        
        return individuo
            

    def torneio(self):
        copy_generation = self.current_generation.copy()
         
        parceiros = []
        par = 1
        while par <= 2:
            first = 0
            second = 0

            while first == second:
                first = random.randrange(0, self.size-par)
                second = random.randrange(0, self.size-par)

            parceiro = None

            if copy_generation[first].peso >= copy_generation[second].peso:
                parceiro = copy_generation.pop(first)
            else:
                parceiro = copy_generation.pop(second)
            
            parceiros.append(parceiro)
            par  = par + 1
        return parceiros

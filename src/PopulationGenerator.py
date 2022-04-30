from math import e
import random

class Individual:

    def __init__(self, x1, x2, x3, x4, x5) :
        self.xs = [x1, x2, x3, x4, x5]
        self.peso = ((sum(self.xs))*e**(-(sum(self.xs))/20))

    def imprime_peso_e_xs(self):
        print(self.peso)
        print(self.xs)

    def equals(self, individuo):
        cont  = 0
        while cont < len(self.xs):
            if self.xs[cont] != individuo.xs[cont]:
                return False
            cont  =  cont + 1
        return True

def generate_population(size, faixa):
    cont = 0
    population = []
    while cont < size:
        x1 = get_random_number(faixa)
        x2 = get_random_number(faixa)
        x3 = get_random_number(faixa)
        x4 = get_random_number(faixa)
        x5 = get_random_number(faixa)
        population.append(Individual(x1, x2, x3, x4, x5))
        cont = cont + 1
    return population

def get_random_number(faixa):
    return random.uniform(-faixa, faixa)

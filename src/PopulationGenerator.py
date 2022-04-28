import random

class Individual:

    def __init__(self, x1, x2, x3, x4, x5) :
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5
        self.peso = (self.x5**5)+(self.x4**4)+(self.x3**3)+(self.x2**2)+(self.x1**1)

def generate_population(size):
    cont = 0
    faixa = 100
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
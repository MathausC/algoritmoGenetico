import random

class Individual:

    def __init__(self, x1, x2, x3, x4, x5) :
        self.xs = [x1, x2, x3, x4, x5]
        self.peso = (self.xs[0]**5)+(self.xs[1]**4)+(self.xs[2]**3)+(self.xs[3]**2)+(self.xs[4]**1)

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
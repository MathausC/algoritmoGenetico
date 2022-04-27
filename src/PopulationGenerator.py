import random

class Individual:
    def __init__(self, x1, x2, x3) :
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
    
    peso = 0.0

def generate_population(size):
    cont = 0
    population = []
    while cont < size:
        x1 = random.random()
        x2 = random.random()
        x3 = random.random()
        population.append(Individual(x1, x2, x3))
        cont = cont + 1
    return population
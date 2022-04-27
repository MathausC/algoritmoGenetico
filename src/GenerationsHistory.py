import src.PopulationGenerator as PopulationGenerator

class Generation:
    def __init__(self, size):
        self.current_generation = PopulationGenerator.generate_population(size)

    def get_generation(self):
        return self.current_generation
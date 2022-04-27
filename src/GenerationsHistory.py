import src.PopulationGenerator as PopulationGenerator

class Generation:
    def __init__(self, size):
        self.current_generation = PopulationGenerator.generate_population(size)

    def get_generation(self):
        return self.current_generation
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
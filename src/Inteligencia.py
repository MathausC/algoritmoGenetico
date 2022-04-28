import src.GenerationsHistory as GenerationsHistory

class Inteligencia:
    def __init__(self, size, faixa, mutacao, geracoes):
        self.geracoes = geracoes
        self.mutacao = mutacao
        self.generation_object = GenerationsHistory.Generation(size, mutacao, faixa)

    def run_generations(self, repeticao):
        cont = 1
        melhor = None
        melhor_anterior = None
        cont_melhor = 0
        while cont <= self.geracoes:
            print(f'Geracao: {cont}')
            melhores = self.generation_object.get_tres_melhores()
            melhores[0].imprime_peso_e_xs()

            if melhor is not None:
                melhor = melhores[0]
            else:
                melhor_anterior = melhor
                melhor = melhores[0]
                if melhor.equals(melhor_anterior):
                    cont_melhor = cont_melhor + 1
                else:
                    cont_melhor = 0
            
            if cont_melhor >= repeticao:
                break

            self.generation_object.algoritmo_genetico(self.mutacao)
            cont = cont + 1

def menu():
    size = int(input("Informe o número de indivíduos: "))
    faixa = float(input("Informe a faixa dos valores de x: "))
    mutacao = float(input("Informe o percentual de mutação: "))
    geracoes = int(input("Informe o número de gerações: "))
    repeticao = int(input("Informe o número repetições do melhor: "))

    inteligencia_object = Inteligencia(size, faixa, mutacao,geracoes)

    inteligencia_object.run_generations(repeticao)
import GenerationsHistory as GenerationsHistory
import matplotlib.pyplot as plt
from os import system, name

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
        geracao = []
        fit = []
        x1 = []
        x2 = []
        x3 = []
        x4 = []
        x5 = []
        while cont <= self.geracoes:
            self.clear()
            print(f'Geracao: {cont}')
            melhores = self.generation_object.get_tres_melhores()
            melhores[0].imprime_peso_e_xs()

            if melhor is None:
                melhor = melhores[0]
            else:
                melhor_anterior = melhor
                melhor = melhores[0]
                if melhor.equals(melhor_anterior):
                    cont_melhor = cont_melhor + 1
                else:
                    cont_melhor = 0
            
            geracao.append(cont)
            x1.append(melhor.xs[0])
            x2.append(melhor.xs[1])
            x3.append(melhor.xs[2])
            x4.append(melhor.xs[3])
            x5.append(melhor.xs[4])
            fit.append(melhor.peso)
        
            if cont_melhor >= repeticao:
                break

            self.generation_object.algoritmo_genetico(self.mutacao)
            cont = cont + 1

        plt.plot(geracao, x1, color='blue', label='stars',  marker='*')
        plt.plot(geracao, x2, color='yellow', label='stars',  marker='*')
        plt.plot(geracao, x3, color='green', label='stars',  marker='*')
        plt.plot(geracao, x4, color='black', label='stars',  marker='*')
        plt.plot(geracao, x5, color='pink', label='stars',  marker='*')
        plt.xlabel('gerações - axis')
        plt.ylabel('xs - axis')
        plt.title('Algoritmo genetico')
        plt.show()
        plt.close()
        plt.plot(geracao, fit, color='red', label='stars',  marker='*',)
        plt.xlabel('gerações - axis')
        plt.ylabel('fit - axis')
        plt.title('Algoritmo genetico')
        plt.show()
    
    def clear(self):
        if name == 'nt':
            _ = system('cls')

        else:
            _ = system('clear')

def menu():
    size = int(input("Informe o número de indivíduos: "))
    faixa = float(input("Informe a faixa dos valores de x: "))
    mutacao = float(input("Informe o percentual de mutação: "))
    geracoes = int(input("Informe o número de gerações: "))
    repeticao = int(input("Informe o número repetições do melhor: "))

    inteligencia_object = Inteligencia(size, faixa, mutacao,geracoes)

    inteligencia_object.run_generations(repeticao)

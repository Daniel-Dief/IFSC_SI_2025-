import numpy as np

class VetorNaoOrdenado:
    # Contrutor
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # Metodo para imprimir os valores - O(n)
    def imprime(self):
        if(self.ultimaPosicao == - 1):
            print("Vetor vazio!")
        else:
            for i in range(self.ultimaPosicao + 1):
                print(f"{i} - {self.valores[i]}")

    # Metodo para inserir um valor - O(1)
    def inserir(self, valor):
        if(self.ultimaPosicao == self.capacidade - 1):
            print("Vetor está cheio!")
        else:
            self.ultimaPosicao += 1
            self.valores[self.ultimaPosicao] = valor

    # Metodo para procurar um valor - O(n)
    def pesquisar(self, valor):
        if(self.ultimaPosicao == - 1):
            print("Vetor está vazio!")
        else:
            for i in range(self.ultimaPosicao + 1):
                if(valor == self.valores[i]):
                    print(f"{valor} está na posição {i}")
                    return
            print("Valor não encontrado")

    # Metodo para remover um item - O(n)
    def remover(self, index):
        if(self.ultimaPosicao == - 1):
            print("Vetor está vazio!")
        elif(index > self.ultimaPosicao):
            print("Posição fora da array")
        else:
            self.ultimaPosicao -= 1
            for i in range(index, self.ultimaPosicao + 1):
                self.valores[i] = self.valores[i + 1]
            



x = VetorNaoOrdenado(5)
x.inserir(2);
x.inserir(3);
x.inserir(4);
x.remover(5)

x.imprime()

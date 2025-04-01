import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def verTopo(self):
        if(self.ultimaPosicao == -1):
            print("A pilha está vazia!")
            return -1
            
        return self.valores[self.ultimaPosicao]
    
    def empilhar(self, valor):
        if(self.ultimaPosicao == self.capacidade):
            print("A pilha está cheia!")
            return -1
        
        self.ultimaPosicao += 1
        self.valores[self.ultimaPosicao] = valor

    def desenpilhar(self):
        if(self.ultimaPosicao == -1):
            print("A pilha está vazia!")
            return -1

        self.ultimaPosicao -= 1
        return self.valores[self.ultimaPosicao + 1]
    
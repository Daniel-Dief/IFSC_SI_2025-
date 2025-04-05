import numpy as np

class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.quantidade = 0
        self.inicio = 0
        self.fim = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def filaCheia(self):
        return self.quantidade == self.capacidade
        
    def filaVazia(self):
        return self.quantidade == 0
    
    def enfileirar(self, valor):
        if self.filaCheia():
            print("A fila já está cheia!")
            return

        if(self.fim == self.capacidade -1):
            self.fim = 0
        else:
            self.fim += 1

        self.valores[self.fim] = valor

        self.quantidade += 1
        
    def desenfileirar(self):
        if self.filaVazia():
            print("A fila está vazia!")
            return

        print(self.valores[self.inicio])

        toReturn = self.valores[self.inicio]
        
        if self.inicio == self.capacidade -1:
            self.inicio = 0
        else:
            self.inicio += 1
        
        self.quantidade -= 1

        return toReturn;

fila = Fila(5)
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
fila.desenfileirar()
fila.enfileirar(6)
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
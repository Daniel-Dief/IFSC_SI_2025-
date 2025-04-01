import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # Método para imprimir os valores - O(n)
    def imprime(self):
        if self.ultimaPosicao == -1:
            print("Vetor vazio!")
        else:
            for i in range(self.ultimaPosicao + 1):
                print(f"{i} - {self.valores[i]}")

    # Método para inserir um valor - O(n)
    def inserir(self, valor):
        if self.ultimaPosicao == self.capacidade - 1:
            print("Vetor está cheio!")
            return

        indexAlvo = 0
        for i in range(self.ultimaPosicao + 1):
            if valor <= self.valores[i]:
                indexAlvo = i
                break
        else:
            indexAlvo = self.ultimaPosicao + 1

        for i in range(self.ultimaPosicao, indexAlvo - 1, -1):
            self.valores[i + 1] = self.valores[i]

        self.valores[indexAlvo] = valor
        self.ultimaPosicao += 1

    # Método para procurar um valor - O(n)
    def pesquisar(self, valor):
        if self.ultimaPosicao == -1:
            print("Vetor está vazio!")
            return -1

        for i in range(self.ultimaPosicao + 1):
            if valor == self.valores[i]:
                print(f"{valor} está na posição {i}")
                return i

        print("Valor não encontrado")
        return -1

    # Método para remover um item - O(n)
    def remover(self, index):
        if self.ultimaPosicao == -1:
            print("Vetor está vazio!")
            return
        if index > self.ultimaPosicao or index < 0:
            print("Posição fora da array")
            return

        for i in range(index, self.ultimaPosicao):
            self.valores[i] = self.valores[i + 1]

        self.ultimaPosicao -= 1
    
    def pesquisaBinaria(self, valor):
        if self.ultimaPosicao == -1:
            print("Vetor está vazio!")
            return -1
        
        min = 0
        max = self.ultimaPosicao

        while True:
            med = int((min + max) / 2)
            if(valor == self.valores[med]):
                print(f"Valor encontrado na posição {med}")
                return med
            elif(min > max):
                print("Valor não encontrado")
                return -1
            elif(valor > self.valores[med]):
                min = med + 1
            elif(valor < self.valores[med]):
                max = med - 1
    
x = VetorOrdenado(10)
x.inserir(3)
x.inserir(4)
x.inserir(11)
x.inserir(33)
x.inserir(6)
x.inserir(8)
x.inserir(10)
x.inserir(0)
x.inserir(41)
x.imprime()
x.pesquisaBinaria(45)
import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def pilhaCheia(self):
        if(self.ultimaPosicao == self.capacidade -1):
            return True
        else:
            return False
        
    def pilhaVazia(self):
        if(self.ultimaPosicao == -1):
            return True
        else:
            return False

    def verTopo(self):
        if(self.ultimaPosicao == -1):
            print("A pilha está vazia!")
            return -1
            
        print(self.valores[self.ultimaPosicao])
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
    
x = Pilha(10)
x.empilhar(5)
x.empilhar(3)
x.empilhar(2)
x.empilhar(5)
x.empilhar(9)
x.empilhar(45)
x.verTopo()
x.desenpilhar()
x.desenpilhar()
x.desenpilhar()
x.verTopo()
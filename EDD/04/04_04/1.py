import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=str)

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

    def verPilha(self):
        if(self.ultimaPosicao == -1):
            print("A pilha está vazia!")
            return -1

        for i in range(self.ultimaPosicao + 1):
            print(i, " - ", self.valores[i])

expres = "a{b(c[d]e)f}"
pilha = Pilha(len(expres))
putCarac = ['(', '[', '{']

for i in range(0, len(expres)):
    if (expres[i] in putCarac):
        pilha.empilhar(expres[i])
    else:
        match expres[i]:
            case ')':
                if pilha.verTopo() == '(':
                    pilha.desenpilhar()
                else:
                    print("Erro na posição: ", i)
                    break;
            case ']':
                if pilha.verTopo() == '[':
                    pilha.desenpilhar()
                else:
                    print("Erro na posição: ", i)
                    break;
            case '}':
                if pilha.verTopo() == '{':
                    pilha.desenpilhar()
                else:
                    print("Erro na posição: ", i)
                    break;

if pilha.verPilha() == -1:
    print("Algoritimo executado com sucesso!")
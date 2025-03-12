def att1(n1 : int, n2 : int):
    result = n1 + n2
    return result

def att2(forCheck : int):
    return forCheck % 2 == 0

def att3():
    for i in range(1, 11):
        print(i)
        
def att4(str1 : str,  str2 : str):
    return str1 == str2

def att5(n : int):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def att6(ll : list):
    maior = ll[0]
    for i in ll:
        if (i > maior):
            maior = i
            
    return maior

def att7(n : list):
    control = True
    for i in range(2, n):
        if (n % i == 0):
            control = False
            break
    return control

def att8():
    somm = 0
    for i in range(1, 100):
        if(not att2(i)):
            somm += i
    return somm

# --------------------------------------------------------------------------------------------
#Crie uma lista com números inteiros aleatórios e exiba o maior e o
#menor número da lista.

import random

def att9():
    lis = []
    for i in range(0, 10):
        lis.append(int(
                random.random() * 100 // 1
        ))
    return lis, max(lis), min(lis)

# Crie uma lista de strings e conte a quantidade de ocorrências de
# cada palavra na lista.

def att10():
    strList = [
        "cachorro",
        "floresta",
        "sol",
        "computador",
        "alegria",
        "universo",
        "paz",
        "sol",
        "relâmpago",
        "floresta",
        "floresta",
        "alegria",
        "cachorro",
        "relâmpago",
        "desafio",
        "lua",
        "estrela",
        "desafio",
        "universo",
        "desafio",
        "paz",
        "cachorro",
        "computador",
        "paz",
        "relâmpago",
        "estrela",
        "lua",
        "estrada",
        "estrada",
        "sol",
        "estrela",
        "estrada",
        "universo",
        "computador",
        "estrada",
        "universo",
        "floresta",
        "floresta",
        "desafio",
        "cachorro",
        "lua",
        "cachorro",
        "universo",
        "estrela",
        "desafio",
        "sol",
        "estrada",
        "lua",
        "estrela",
        "relâmpago"
    ]
    control = []
    
    for i in strList:
        isAlready = False
        for j in control:
            if j["string"] == i:
                isAlready = True
                break
            
        if(not isAlready):
            count = 0
            for j in strList:
                if i == j:
                    count += 1
        
            control.append({
                "string" : i,
                "count" : count
            })
        
    return control


def att11():
    intList = [37, 72, 9, 56, 9, 14, 37, 67, 72, 48, 9, 56, 14, 93, 48, 72, 22, 37, 67, 56, 72, 22, 93, 56, 67, 9, 37, 14, 48, 72]
    trueList = []
    
    for i in intList:
        isAlready = False
        for j in trueList:
            if(i == j):
                isAlready = True
                break
        
        if(not isAlready):
            trueList.append(i)
            
    print(trueList)
    
def att12():
    list1 = []
    list2 = []
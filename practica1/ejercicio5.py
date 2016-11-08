#Generar aleatoriamente una cadena de [ y ]

import random

def CadenaCorchetes():
    tam = random.randrange(2,15)
    corchetes = ['[',']']
    vector = []
    for i in range(0,tam):
        r = random.randrange(2)
        vector.append(corchetes[r])
    return vector

#Comprobar si esta balanceada

def Balanceada(cad):
    tam = len(cad)
    if tam%2 == 1:
        return  False
    else:
        balanceo = 0
        for i in range(0,tam):
            if cad[i] == '[':
                balanceo += 1
            elif cad[i] == ']':
                balanceo -=1
            if balanceo < 0:
                return False
        if balanceo == 0:
            return True
        else:
            return False
        


cadena = CadenaCorchetes()
print cadena
balanceo = Balanceada(cadena)
print balanceo


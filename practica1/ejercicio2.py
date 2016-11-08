import random
from time import time


#Pip para instalar librerias



def CrearMatriz(n_filas, n_cols):
    matriz = []
    for i in range(n_filas):
        matriz.append([])
        for j in range(n_cols):
            n_aleatorio = random.randrange(0,100)
            matriz[i].append(n_aleatorio)
    return matriz

def Burbuja(matriz,f,c):
    for i in range(0,f):
        for j in range(0,c):
            for k in range(c-1):
                if matriz[j][k] > matriz [j][k+1]:
                    aux = matriz[j][k]
                    matriz[j][k] = matriz[j][k+1]
                    matriz[j][k+1] = aux
    return matriz

def Seleccion(matriz, f, c):
    for i in range(0,f):
        for j in range(1,c-1):
            minimo = j
            for k in range(j+1,c):
                if matriz[j][k] < matriz[j][minimo]:
                   minimo = k

            aux = matriz[j][k]
            matriz[j][k] = matriz[j][minimo]
            matriz[j][minimo] = aux
    return matriz

def Ordenar(matriz,f):
    for i in range(0,f):
        matriz[i].sort()
    return matriz

def count_elapsed_time(f):
    def wrapper():
        
        ret = f()
        
        return ret
    return wrapper


print "Introduce numero de filas"
filas = input()
print "Introduce numero de columnas"
columnas = input()
m = CrearMatriz(filas, columnas)
print m

start_time = time()
m1 = Burbuja(m, filas, columnas)
elapsed_time = time() - start_time
print m1
print("Tiempo transcurrido: %0.10f seconds. " %elapsed_time)

start_time = time()
m2 = Ordenar(m,filas)
elapsed_time = time() - start_time
print m2
print("Tiempo transcurrido: %0.010f seconds. " %elapsed_time)



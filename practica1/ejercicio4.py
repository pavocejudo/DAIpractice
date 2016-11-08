#Sucesion de Fibonacci

def Fibonacci(n):
    if n<2:
        return n
    else:
        n1 = int(n)-1
        n2 = int(n)-2
        return Fibonacci(n1)+Fibonacci(n2)


fichero_lectura = open('entrada.txt', 'r')

n= fichero_lectura.readline()

fichero_lectura.close()

valor_Fb = Fibonacci(n)
print Fibonacci(n)

fichero_salida = open('salida.txt', 'w')
fichero_salida.write(str(valor_Fb))
fichero_salida.close()



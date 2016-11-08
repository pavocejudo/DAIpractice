#Criba de eratostenes

def criba_eratostenes(n):
    primos=[]
    multiplos = set()
    for i in range(2,n+1):
        if i not in multiplos:
            primos.append(i)
            multiplos.update(range(i*i,n+1,i))
    return primos
print "Introduce un numero para encontrar los numeros primos menores que el: "
n = input()
print "Los numeros son: "
print criba_eratostenes(n)

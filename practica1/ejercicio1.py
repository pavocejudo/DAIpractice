import random

rand = random.randint(0,100)
print rand

numero = input()

intentos = 1

while (numero != rand) & (intentos<10) :
    if numero > rand : 
        print "El numero es menor"
    elif numero < rand:
        print "El numero es mas grande"
    numero = input()
    intentos += 1
    if intentos == 10:
        print "Maximo numero de intentos"
        
if numero == rand:
    print "Ha acertado el numero"

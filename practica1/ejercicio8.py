
import re


#Identificar cualquier palabra seguida de un espacio y una letra unica mayuscula

def IdentificarPalabras(p):
    match = bool(re.match('[A-Z][a-z]* [A-Z]',p))
    return match

#Identificar correos electronicos validos
def IdentificarCorreos(correo):
    match = bool(re.match('(\w+)@((\w+)\.)+(\w+)',correo))
    return match

#Identificar numeros de tarjeta de credito validos separados por espacio o '-'
def IdentificarTarjetasDeCredito(numero):
    match = bool(re.match('(\d{4}( |-)){3}(\d{4})\b',numero))
    return match

print 'Indique una palabra seguida de un espacio y una letra mayuscula'
nombre = raw_input()
if IdentificarPalabras(nombre) ==True:
    print 'La palabra tiene el formato valido'
else:
    print 'La palabra tiene un formato invalido'

print 'Indique un correo electronico'
correo = raw_input()
if IdentificarCorreos(correo) == True:
    print 'El correo es valido'
else:
    print 'El formato del correo es invalido'

print 'Indique un numero de cuenta'
numero = raw_input()
if IdentificarTarjetasDeCredito(numero)==True:
    print 'Formato de la tarjeta valido'
else:
    print 'Formato de la tarjeta invalido'

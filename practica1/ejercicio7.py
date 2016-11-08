

def modulo ( a, b):
    return a*a+b*b
    
def Mandelbrot(x_inicial,y_inicial,x_final,y_final):
    c= [x_inicial,y_inicial]    
    tope = x_final * x_final + y_final * y_final
    zn = [0,0]
    modulo_zn = 0
    parada= modulo(x_final,y_final)
    zn[0]=zn[0]^2 -zn[1]^2  #parte real
    zn[1]=2*zn[0]*zn[1]     #parte imaginaria
    while modulo_zn <= parada :
        zn[0]+= c[0]
        zn[1] += c[1]
        modulo_zn = modulo(zn[0],zn[1])
        print "["+str(zn[0]) +","+ str(zn[1])+"]"


    
       
print 'Indique (x1,y1)'
coordenadas_iniciales = []
coordenadas_iniciales = input()

print 'Indique (x2,y2)'
coordenadas_finales = []
coordenadas_finales = input ()

x_inicial = coordenadas_iniciales[0]
y_inicial = coordenadas_iniciales[1]
x_final = coordenadas_finales[0]
y_final = coordenadas_finales[1]
c=1

if x_inicial*x_inicial + y_inicial * y_inicial >= 4:
    print 'El punto inicial esta fuera del conjunto'
if x_final * x_final + y_final* y_final >= 4:
    print 'Punto final esta fuera del conjunto'

Mandelbrot(x_inicial,y_inicial,x_final,y_final)

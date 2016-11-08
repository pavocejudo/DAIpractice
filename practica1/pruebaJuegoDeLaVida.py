#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# ---------------------------------------------------------------------
# Programa: EL juego de la vida.
# Autor: Adrián Guerra Marrero (adrigm).
# Web: www.razonartificial.com
# Licencia: GNU/GPL
# ---------------------------------------------------------------------
 
# Módulos
from gasp import *
import time, os, random
 
# CONSTANTES
width = 640
height = 480
 
# Clases
# ---------------------------------------------------------------------
 
class Juego:
    def __init__(self, opcion=1, archivo="mapa.txt", fil=10, col=10):
        if opcion == 2:
            self.mapa = leerMapa(archivo)
        else:
            self.mapa = range(fil)
            for i in range(fil):
                self.mapa[i] = range(col)
 
            for f in range(fil):
                for c in range(col):
                    self.mapa[f][1] = random.randint(0, 1)
 
        self.filas = len(self.mapa)
        self.columnas = len(self.mapa[0])
 
    def __str__(self):
        mapa = ""
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.mapa[f][1] == 0:
                    mapa += ". "
                if self.mapa[f][1] == 1:
                    mapa += "* "
            mapa += "\n"
        return mapa
 
    def analizarVecinos(self, fil, col):
        vecinos = 0
        if fil-1 >= 0 and col-1 >= 0:
            if self.mapa[fil-1][col-1] == 1:
                vecinos += 1
        if fil-1 >= 0:
            if self.mapa[fil-1][col] == 1:
                vecinos += 1
        if fil-1 >= 0 and col+1 <= self.columnas-1:
            if self.mapa[fil-1][col+1] == 1:
                vecinos += 1
        if col-1 >= 0:
            if self.mapa[fil][col-1] == 1:
                vecinos += 1
        if col+1 <= self.columnas-1:
            if self.mapa[fil][col+1] == 1:
                vecinos += 1
        if fil+1 <= self.filas-1 and col-1 >= 0:
            if self.mapa[fil+1][col-1] == 1:
                vecinos += 1
        if fil+1 <= self.filas-1:
            if self.mapa[fil+1][col] == 1:
                vecinos += 1
        if fil+1 <= self.filas-1 and col+1 <= self.columnas-1:
            if self.mapa[fil+1][col+1] == 1:
                vecinos += 1
        return vecinos
 
    def ciclo(self):
        nueva_conf = []
        for f in range(self.filas):
            columna = []
            for c in range(self.columnas):
                vecinos = self.analizarVecinos(f, c)
                if self.mapa[f][1] == 0:
                    if vecinos == 3:
                        columna.append(1)
                    else:
                        columna.append(0)
                if self.mapa[f][1] == 1:
                    if vecinos == 2 or vecinos == 3:
                        columna.append(1)
                    else:
                        columna.append(0)
            nueva_conf.append(columna)
 
        self.mapa = nueva_conf
 
    def dibujar(self):
        dist_lv = width/self.columnas
        dist_lh = height/self.filas
        for i in range(self.columnas):
            Line((dist_lv*i, 0), (dist_lv*i, height))
        for n in range(self.filas):
            Line((0, dist_lh*n), (width, dist_lh*n))
 
        for f in range(self.filas):
            y = height-dist_lh - ((dist_lh)*f)+(dist_lh/2)
            for c in range(self.columnas):
                x = ((dist_lv)*c)+(dist_lv/2)
                if self.mapa[f][1] == 1:
                    Circle((x, y), ((dist_lh/2)-((dist_lh/2)*0.2)))
 
# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------
 
# Quita el ultimo caracter de una lista.
def quitarUltimo(lista):
    for i in range(len(lista)):
        lista[i] = lista[i][:-1]
    return lista
 
# Covierte una cadena en una lista.
def listarCadena(cadena):
    lista = []
    for i in range(len(cadena)):
        if cadena[i] == ".":
            lista.append(0)
        if cadena[i] == "*":
            lista.append(1)
    return lista
 
# Lee un archivo de texto y lo convierte en una lista.
def leerMapa(archivo):
    mapa = open(archivo, "r")
    mapa = mapa.readlines()
    mapa = quitarUltimo(mapa)
    for i in range(len(mapa)):
        mapa[i] = listarCadena(mapa[i])
    return mapa
 
# ---------------------------------------------------------------------
 
def main():
    print "Indica si quieres cargar una configuración o utilizar una aleatoria."
    print "1. Aleatoria"
    print "2. Cargar configuración"
    opcion = input("Introduce el número de la opción elegida: ")
    if opcion == 1:
        filas = input("Introduce el número de filas: ")
        columnas = input("Introduce el número de columnas: ")
        archivo = ""
    if opcion == 2:
        archivo = raw_input("Intruduce la ruta del archivo: ")
        filas = 0
        columnas = 0
 
    begin_graphics(width=width, height=height, title="Juego de la Vida")
    juego = Juego(opcion=opcion, archivo=archivo, fil=filas, col=columnas)
    while True:
        juego.dibujar()
        juego.ciclo()
        time.sleep(0.35)
        clear_screen()
        update_when('next_tick')
    end_graphics()
    return 0
 
if __name__ == '__main__':
    main()

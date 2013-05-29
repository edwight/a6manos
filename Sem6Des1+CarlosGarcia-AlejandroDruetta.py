#! /usr/bin/env python
# -*- encoding: utf-8 -*-

''' Desarrollar un programa que permita crear diseños a partir de
patrones y desplazamientos'''

def main():
    capas = input("Cuántas capas tendrá el diseño?: ")
    ancho = input("Cuál será el ancho del patrón?: ")

#hacemos un for para obtener los valores del ancho del patrón
    guia = ""
    for x in range(1, ancho+1):
        if x <= 9:
            guia = guia + str(x)
        elif x > 9:
            unnumero = str(x)
            guia = guia + unnumero[1]

#dibujamos los bordes del ancho del patron
    deco = ""
    for x in range(len(guia)):
        if x == 0:
            deco += "|"
        elif x == ancho-1:
            deco += "|"
        else:
            deco += " "

#pedimos los diseños para cada capa
    disenio = []
    capa = ""
    for x in range(capas):
        while True:
            print "Introduzca el diseño de la capa",x,":"
            print guia
            print deco
            dise = raw_input()
            if len(dise) < ancho:
                #evita que la capa sea menor que ancho completando con espacios en blanco.
                dise = dise + " " * (ancho - len(dise))
                break
            elif len(dise) > ancho:
                print "Error: ancho de la capa superior al del patrón."
        disenio.append(dise)

    print disenio

main()

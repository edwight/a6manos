# -*- encoding: utf-8 -*-

''' Desarrollar un programa que permita crear diseños a partir de 
patrones y desplazamientos'''

def main():
	capas = input("Cuantas capas tendra el diseño?: ")
	patron = input("Cual sera el ancho del patrón?: ")

#hacemos un for para obtener los valores del ancho del patrón
	ancho = ""
	for x in range(1, patron+1):
		if x <= 9:
			ancho = ancho + str(x)
		elif x > 9:
			unnumero = str(x)
			ancho = ancho + unnumero[1]

#dibujamos los bordes del ancho del patron
	deco = ""
	for x in range(len(ancho)):
		if x == 0:
			deco += "|"
		elif x == patron-1:
			deco += "|"
		else:
			deco += " "

#pedimos los diseños para cada capa
	disenio = []
	for x in range(capas):
		print "Introduzca el diseño de la capa",x,":"
		print ancho
		print deco
		dise = raw_input()
		disenio.append(dise)

	print disenio

main()

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 17:00:41 2023

@author: sergi
"""

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

for x in teclado1: #ciclo for que se encarga de pasar por todos los elementos del diccionario teclado 1
    print(x + " = " + teclado1[x] + ".") #indica la clasificación y el dato de los elementos de teclado1
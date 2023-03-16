# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 17:04:05 2023

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

print(teclado1)
print(teclado2)

del teclado1 #Elimina el diccionario entero
del teclado2['Categoría'] #Elimina la sección categoría y los datos de ésta en el teclado dos
del teclado2['Precio']
print(teclado2)
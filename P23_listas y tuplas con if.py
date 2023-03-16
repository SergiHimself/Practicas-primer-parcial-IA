# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:11:56 2023

@author: sergi
"""

respuesta = input("Introduce un color: ") #se imprime una instrucción con la expectativa de que el usuario responda en consola
colores = ("celeste", "magenta", "amarillo", "negro") #tupla
if respuesta in colores: #si la respuesta introducida por el usuario se encuentra en la tupla, imprime la siguiente línea
    print("El color corresponde al modelo CMYK")
else: #cualquier otra respuesta que no se encuentre entre los datos de la tupla, imprime la siguiente línea
    print("El color no corresponde al modelo CMYK")
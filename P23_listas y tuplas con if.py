# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:11:56 2023

@author: sergi
"""

respuesta = input("Introduce un color: ")
colores = ("celeste", "magenta", "amarillo", "negro")
if respuesta in colores:
    print("El color corresponde al modelo CMYK")
else:
    print("El color no corresponde al modelo CMYK")
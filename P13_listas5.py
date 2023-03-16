# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 15:28:51 2023

@author: sergi
"""

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(colores) 
c1 = colores.pop(2) #función pop elimina el dato y lo guarda en la variable c1 para posterior uso
c2 = colores.pop(-2)
colores2 = [c1,c2] #nueva lista formada por los valores eliminados de la anterior
print(colores)
print(colores2)
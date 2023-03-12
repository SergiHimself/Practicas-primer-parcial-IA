# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:31:08 2023

@author: sergi
"""

x=0
while x <= 30:
    
    if x == 4 or x == 6 or x == 10:
        print("Se saltó el valor", x, "de x.")
        x += 1
        continue
    if x ==15:
        print("Se rompió la ejecución del bucle cuando x valía ", x)
        break
    print("El valor de bucle es: ", x)
    x += 1
    
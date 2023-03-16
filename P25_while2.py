# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:31:08 2023

@author: sergi
"""

x=0 #variable
while x <= 30: #mientras x sea menor o igual a 30:
    
    if x == 4 or x == 6 or x == 10: #si x es igual a 4,6 o 10
        print("Se saltó el valor", x, "de x.") #indica los valores saltados
        x += 1 #agrega uno para seguir con la cuenta
        continue
    if x ==15: 
        print("Se rompió la ejecución del bucle cuando x valía ", x)
        break #rompe el ciclo automáticamente
    print("El valor de bucle es: ", x)
    x += 1
    
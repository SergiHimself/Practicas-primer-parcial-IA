# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:06:15 2023

@author: sergi
"""

edad = int(input('¿Cuál es tu edad?\n')) #imprime una pregunta y avisa a la consola que se solicita una respuesta del usuario para guardar en la variable edad
if edad <= 0: #si la edad es menor o igual que sero, ejecuta la siguiente instrucción, si no, evalúa el elif a continuación
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18: #si la edad es mayor que 1 y menor que 18, imprime el mensaje de la siguiente línea, si no, pasa a segundo elif
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
	print('Eres mayor de edad.')
elif edad >= 45 and edad <=100:
    print("Estás más pa' allá que pa' acá.")
elif edad >= 100 and edad <=120:
    print("Impresionante")
else: #si el programa recibe un valor fuera de 0 a 120, el programa indica que la respuesta no fue válida
	print('Edad no válida.') 
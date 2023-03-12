# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 17:20:52 2023

@author: sergi
"""

def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('azul','negro')

def suma(*args):
    res = args[0] + args[1] + args[2] + args[3] + args[4]
    print(res)
    
suma(45, 56, 23, 73, 56)
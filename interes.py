# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 02:40:27 2020

@author: begon
"""

# =============================================================================
# Functions
# =============================================================================
def interes(cantInicial,porcentaje,times):
    cantidad = cantInicial
    for i in range(0,times):
        cantidad = cantidad+cantidad*(porcentaje/100)
    print("Cantidad final = " + str(cantidad))
    print("Ganancia neta = " + str(cantidad-cantInicial))
    print("Porcentaje = " + str((cantidad-cantInicial)/cantInicial*100))

        
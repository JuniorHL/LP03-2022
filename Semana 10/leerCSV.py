# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 09:17:50 2022

@author: USUARIO
"""

# Importamos las librerias basicas par leer archivos csv...
import csv

# Abrimos el archivo indicando el PATHy el encoding=utf para leer caracteres especiales...
with open("Global_Mobility_Report.csv", encoding = "utf8") as f:
    datos = csv.reader(f, delimiter=',')
    for fila in datos:
        print(f"{fila[0]}\t{fila[1]}\t{fila[2]}\t{fila[3]}\t{fila[4]}\t{fila[5]}\t{fila[6]}\t{fila[7]}\t{fila[8]}\t{fila[9]}\t{fila[10]}")
        
        
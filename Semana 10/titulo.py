# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:55:09 2022

@author: USUARIO
"""

# Problema: Necesitamos mostrar los nombres de una tabla presentando
#           las primera letras en Mayusculas (Formato titulo)...

#Importamos la libreria...
import camelcase 

nombre = "anselmo junior huancas leuyacc"
print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam...
cam = camelcase.CamelCase()
print("Con camelcase...")

# Imprimiendo el nombre en formato titulo...
# Utilizamos el camelcase...
print(cam.hump(nombre))

# Para resolver el siguiente problema
# Creamos otro objeto llamado cam2
# Al definir el objeto, incluimo los argumentos
# 'anselmo' y 'huancas'

cam2 = camelcase.CamelCase("anselmo","huancas")
print(cam2.hump(nombre))

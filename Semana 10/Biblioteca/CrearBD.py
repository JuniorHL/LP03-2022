# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:23:35 2022

@author: USUARIO
"""

import sqlite3

# Con el comando connect buscara la base de datos
# que tenga ese nombre, de lo contrario lo creara...
conexion = sqlite3.connect("bdbiblioteca.db")
conexion.close()
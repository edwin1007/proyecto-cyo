#from tkinter import * 

import numpy as np
import tkinter as tk
from tkinter import ttk

raiz = tk.Tk() 
raiz.title("Primera Ventana") #Cambiar el nombre de la ventana 
raiz.geometry("520x480") #Configurar tamaño 
#raiz.iconbitmap("form.ico") #Cambiar el icono 
#raiz.config(bg="gray") #Cambiar color de fondo
raiz.resizable(0,0)

def cargarDatos():
    print("Datos cargados")

def resolverCalendario():
    print("Calendario programado")

def leerArchivo():
    archivo = open("prueba.txt")
    arreglo = []
    n = 0
    while(True):
        linea = archivo.readline() 
        arreglo.append(linea)
        #print(linea)
        n = n+1
        if n==3:
            datos = ''.join(archivo.readlines()).replace('\n',';')
            break

    archivo.close()
    return arreglo, datos

variables, matriz = leerArchivo()

x = int(variables[0])
y = int(variables[1])
z = int(variables[2])

m = np.matrix(matriz)

print(x)
print(y)
print(z) 
print(m)

entry = ttk.Entry()
entry.place(x=50, y=150)

boton1 = ttk.Button(text="Cargar datos", command=lambda: print(entry.get()))
boton1.place(x=50, y=50)

boton2 = ttk.Button(text="Programar calendario", command=resolverCalendario) 
boton2.place(x=50, y=100)

raiz.mainloop()
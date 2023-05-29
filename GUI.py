#from tkinter import * 

import numpy as np
import tkinter as tk
from tkinter import END, GROOVE, LEFT, RIGHT, Y, Label, ttk

tamLetra = 10

raiz = tk.Tk() 
raiz.title("Proyecto: complejidad y optimización") #Cambiar el nombre de la ventana 
raiz.geometry("650x500") #Configurar tamaño 
raiz.resizable(0,0)

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

'''
entry = ttk.Entry()
entry.place(x=50, y=150)

boton1 = ttk.Button(text="Cargar datos", command=lambda: print(entry.get()))
boton1.place(x=50, y=50)

boton2 = ttk.Button(text="Programar calendario", command=resolverCalendario) 
boton2.place(x=50, y=100)
'''

# Create label
l = Label(raiz, text = "Programador de calendario deportivo")
l.config(font =("Courier", tamLetra))
l.grid(column=0, row=1)

# Create label
le1 = Label(raiz, text = "")
le1.config(font =("Courier", tamLetra)) 
le1.grid(column=0, row=2)

# Create label
le2 = Label(raiz, text = "")
le2.config(font =("Courier", tamLetra)) 
le2.grid(column=1, row=2)

# Create button for next text.
b1 = ttk.Button(raiz, text = "Cargar datos de entrada")
b1.grid(column=0, row=3)


# Create label
ln = Label(raiz, text = "n-numero de equipos: ")
ln.config(font =("Courier", tamLetra))
ln.grid(column=0, row=4)

# Create label
ln1 = Label(raiz, text = x)
ln1.config(font =("Courier", tamLetra))
ln1.grid(column=1, row=4)


# Create label
lmin = Label(raiz, text = "Identificador de primer equipo:")
lmin.config(font =("Courier", tamLetra))
lmin.grid(column=0, row=5)

# Create label
lmin1 = Label(raiz, text = y)
lmin1.config(font =("Courier", tamLetra))
lmin1.grid(column=1, row=5)

# Create label
lmax = Label(raiz, text = "Identificador de último equipo:")
lmax.config(font =("Courier", tamLetra))
lmax.grid(column=0, row=6)

# Create label
lmax1 = Label(raiz, text = z)
lmax1.config(font =("Courier", tamLetra))
lmax1.grid(column=1, row=6)

# Create label
lmax = Label(raiz, text = "Matriz de distancias:")
lmax.config(font =("Courier", tamLetra))
lmax.grid(column=0, row=7)

# Create text widget and specify size.
TextArea1 = tk.Text(raiz, height = 5, width = 30)
TextArea1.grid(column=1, row=7)

# Create label
le3 = Label(raiz, text = "")
le3.config(font =("Courier", tamLetra)) 
le3.grid(column=0, row=8)

# Create label
le4 = Label(raiz, text = "")
le4.config(font =("Courier", tamLetra)) 
le4.grid(column=1, row=8)

# Create an Exit button.
#b2 = ttk.Button(raiz, text = "Exit", command = raiz.destroy)
b2 = ttk.Button(raiz, text = "Calcular calendario deportivo")
b2.grid(column=0, row=9)

# Create label
le5 = Label(raiz, text = "Calendario de salida")
le5.config(font =("Courier", tamLetra)) 
le5.grid(column=0, row=10)

# Create text widget and specify size.
TextArea2 = tk.Text(raiz, height = 5, width = 30)
TextArea2.grid(column=1, row=10)

Fact = m
 
s = [[ -2,  1, -4,  3],
    [ -4,  3, -2,  1],
    [ -3, -4,  1,  2],
    [  2, -1,  4, -3],
    [  4, -3,  2, -1],
    [  3,  4, -1, -2]]

pn = [[ 1, 0, 1, 0],
     [1, 0, 1, 0],
     [1, 1, 0, 0],
     [0, 1, 0, 1],
     [0, 1, 0, 1],
     [0, 0, 1, 1]];

utilidad = 7222
 
 # Create label
le5 = Label(raiz, text = "Utilidad:")
le5.config(font =("Courier", tamLetra)) 
le5.grid(column=0, row=11)

# Create label
le5 = Label(raiz, text = utilidad)
le5.config(font =("Courier", tamLetra)) 
le5.grid(column=1, row=11)


# Insert The Fact.
TextArea1.insert(tk.END, Fact)
TextArea2.insert(tk.END, s)

raiz.mainloop()
import tkinter
from math import e
import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler
import time

primero =0
tercero=3

#Interfaz
ventana = tkinter.Tk()
ventana.geometry("200x100")

# Función de activación
def function_act(w,x,b):
    z = w * x
    if z.sum()  + b > 0:
        return 1
    else:
        return 0

def entrada_datos():
    aumento=0
    entradas=result[primero:tercero+1]

    epocas = 100
    aprendizaje= 0.001
    
    draw_plane()

entrada1  =tkinter.Button(ventana, text = "Calcular",command = entrada_datos)
entrada1.pack()

#Grafica
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_title("Plano Cartesiano")

#Linea horizontal
ax.axhline(y=0, color='black', lw=2)

#Linea vertical
ax.axvline(x=0, color='black', lw=2)

x = np.linspace(0, 20, 100)#[::1] # Valores de x de 0 a 100
y = 5*np.sin(x*(2*np.pi/5)) # Función senoidal con amplitud 5

# Escalamos la función para que vaya de 5 a -5 en y
y = -y/2

y += 0.5*(5 - np.min(y)) 

#ruido
for i in range(len(y)):
    rand_nums = np.random.uniform(-1,1,size=y.shape)
    result = y + rand_nums
    

coordenadas = np.array(list(zip(x,result))) # Creamos un arreglo de coordenadas del ruido

#puntos "x"
ax.plot(x, y, 'o-')

#linea
plt.plot(x,y)
plt.plot(x,result,'o-')

def draw_plane():
    print("actualizacion grafica")
    plt.cla()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Plano Cartesiano")
    #Linea horizontal
    ax.axhline(y=0, color='black', lw=2)

    #Linea vertical
    ax.axvline(x=0, color='black', lw=2)

    #puntos "x"
    ax.plot(x, y, 'o-')

    #linea
    plt.plot(x,y)
    plt.plot(x,result,'o-')
    

plt.show()

ventana.mainloop()

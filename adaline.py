import tkinter
from math import e
import matplotlib.pyplot as plt
import numpy as np
import random
import time

puntitos =[]
uno_cero=[]

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

    weights = np.random.uniform(-1,1,size=2)
    bia = np.random.uniform(-1,1) 
    tasa_aprendizaje = 0.01
    epocas = 100

    for epoca in range(epocas):
        error_total = 0
        for i in range(len(puntitos)):
            prediccion=function_act(weights,puntitos[i],bia)
            error = uno_cero[i] - prediccion
            error_total += error**2
            weights[0] += tasa_aprendizaje * puntitos[i][0] * error
            weights[1] += tasa_aprendizaje * puntitos[i][1] * error
            
            bia += tasa_aprendizaje * error
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
k=y
for i in range(len(k)):
    rand_nums = np.random.uniform(-1,1,size=k.shape)
    result = k + rand_nums
    

coordenadas = np.array(list(zip(x,result))) # Creamos un arreglo de coordenadas del ruido

#puntos "x"
ax.plot(x, y, 'o-')

#linea
plt.plot(x,y)
plt.plot(x,result,'o-')

def draw_plane():
    print("actualizacion grafica")
    plt.cla()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
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

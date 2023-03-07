import tkinter
from math import e
import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler
import time

N=60
n = np.arange(N)

xref = np.cos(2*np.pi*(0.1)*n)
x = 10*np.cos(2*np.pi*(0.1)*n+np.pi/4)

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
    draw_plane()

entrada1  =tkinter.Button(ventana, text = "Calcular",command = entrada_datos)
entrada1.pack()

#Grafica
fig, ax = plt.subplots()
ax.set_xlim(0, 60)
ax.set_ylim(-15, 15)
ax.set_title("Plano Cartesiano")

#Linea horizontal
ax.axhline(y=0, color='black', lw=2)

#Linea vertical
ax.axvline(x=0, color='black', lw=2)

# x = np.linspace(0, 20, 60)#[::1] # Valores de x de 0 a 100
# y = 5*np.sin(x*(2*np.pi/5)) # Función senoidal con amplitud 5

# # Escalamos la función para que vaya de 5 a -5 en y
# y = -y/2

# y += 0.5*(5 - np.min(y)) 

# #ruido
# for i in range(len(y)):
#     rand_nums = np.random.uniform(-1,1,size=y.shape)
#     result = y + rand_nums
    

# coordenadas = np.array(list(zip(x,result))) # Creamos un arreglo de coordenadas del ruido

# #puntos "x" señal deseado
# ax.plot(x, y, 'o-')
# plt.plot(x,y)

# #señal con ruido
# plt.plot(x,result,'o-')
# print(result)
# print(y)

#inicializar filtro
p=3 #numero de coeficientes
h = np.ones((p,1))

matConv = np.zeros((p,1))
S=np.eye(p)*0.001
error=np.zeros(N)
salidas=np.zeros(N)

#itercion filtro
for t in np.arange(N-10)+p+1:
    #vector de entrada
    entrada=xref[t:t-p:-1]
    #erro
    salidas[t]= h.T.dot(entrada)
    error[t]=x[t]-salidas[t]
    K=S.dot(entrada)/(0.3**t+entrada.T.dot(S.dot(entrada)))
    S=(np.eye(p)-K.dot(entrada.T)).dot(S)

    h=h+(K*error[t]).reshape(p,1)

plt.plot(salidas,label="salida")
plt.plot(x,label="entrada")
plt.plot(xref,label="ref")
plt.plot(error,label="error")
plt.legend()
plt.show()
plt.show(x)
plt.show(xref)
plt.show()

def draw_plane():
    print("actualizacion grafica")
    plt.cla()
    ax.set_xlim(-5, 10)
    ax.set_ylim(-5, 10)
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
    

ventana.mainloop()

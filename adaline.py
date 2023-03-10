from math import e
import matplotlib.pyplot as plt
import numpy as np
import tkinter

#Interfaz
ventana = tkinter.Tk()
ventana.geometry("200x200")
ventana.title("IA-P3")

bias = 1
lr=0.01

x = np.linspace(0, 5, 10000)
y = 1 * np.sin(2 * np.pi * (x - 1) / 4)

ruido = -0.9*np.random.randn(len(y))
y_ruido = y + ruido

weights = np.random.uniform(-1, 1, size=3)

def Adaline(y_ruido, weights, bias, lr):

    w = np.array(weights)
    b = bias
    learning_rate = lr
    
    x = y_ruido[0:3]
    
    filtrado = np.zeros(len(y_ruido))
    filtrado[0:3] = y_ruido[0:3]
    
    for k in range(3, len(y_ruido)):
        y_pred = np.dot(x, w) + b
        
        error = y_pred - y_ruido[k]
        
        w -= learning_rate * error * x
        b -= learning_rate * error
        
        x = np.concatenate(([y_ruido[k]], x[0:2]))
        
        filtrado[k] = y_pred
        
    return filtrado


def draw_plane():
    plt.cla()
    ax.set_xlim(0, 5)
    ax.set_ylim(-5, 5)
    #Linea horizontal
    ax.axhline(y=0, color='black', lw=2)

    #Linea vertical
    ax.axvline(x=0, color='black', lw=2)

    y_filtered = Adaline(y_ruido, weights,bias,lr)

    plt.plot(x, y_ruido, label='Ruido')
    plt.plot(x, y_filtered,label='Filtrada')
    plt.plot(x, y,label='Original')

    plt.legend()
    plt.show()

entrada1  =tkinter.Button(ventana, text = "Filtrar",command = draw_plane, fg= "dark blue", background="#C4F9D1")
entrada1.pack()
entrada1.place(x=60, y=90, height= 40, width=80)
etiqueta = tkinter.Label(ventana, text="Adaline", fg="dark green", height=3).pack()

fig, ax = plt.subplots()
ax.set_xlim(0, 5)
ax.set_ylim(-5, 5)

#Linea horizontal
ax.axhline(y=0, color='black', lw=2)

#Linea vertical
ax.axvline(x=0, color='black', lw=2)

plt.plot(x, y_ruido, label='Ruido')
plt.plot(x, y,label='Original')

plt.legend()
plt.show()
    
ventana.mainloop()
#Programa realizado por Jorge Ibáñez, toda la autoría es parte de él pero lo puedes copiar si 
#te lo dejaron de tarea y aún no la has hecho.

import math
import matplotlib.pyplot as plt
import numpy as np
import re
from tkinter import *

#Creación de la clase Complejo y sus métodos (sumar, restar, multiplicar, etc.)
class Complejo:
    def __init__(self, real = None, imaginario = None):
        if real == None:
            real = 0
        if imaginario == None:
            imaginario = 0    
        self.real = real
        self.imaginario = imaginario


    def __str__(self):
        if self.imaginario >= 0:
            x = round(self.real*1000)/1000
            y = round(self.imaginario*1000)/1000 #Redondeo a 3 decimales
            return "{} + {}i".format(x, y)
        elif self.imaginario < 0:
            x = round(self.real*1000)/1000
            y = round(self.imaginario*1000)/1000 #Redondeo a 3 decimales
            return "{} - {}i".format(x, -y)

    def sumar(ComplejoA, ComplejoB):
        ComplejoRes = Complejo()
        ComplejoRes.real= ComplejoA.real + ComplejoB.real
        ComplejoRes.imaginario= ComplejoA.imaginario + ComplejoB.imaginario
        return ComplejoRes

    def restar(ComplejoA, ComplejoB):
        ComplejoRes = Complejo()
        ComplejoRes.real = ComplejoA.real - ComplejoB.real
        ComplejoRes.imaginario = ComplejoA.imaginario - ComplejoB.imaginario
        return ComplejoRes

    def multiplicar(ComplejoA, ComplejoB):
        ComplejoRes = Complejo()
        ComplejoRes.real = ComplejoA.real*ComplejoB.real - ComplejoA.imaginario*ComplejoB.imaginario 
        ComplejoRes.imaginario = ComplejoA.real*ComplejoB.imaginario + ComplejoA.imaginario*ComplejoB.real
        return ComplejoRes

    def dividir(ComplejoA, ComplejoB):
        try:
            ComplejoRes = Complejo()
            magnitudB =  ComplejoB.real**2 + ComplejoB.imaginario**2
            ComplejoRes.real = (ComplejoA.real*ComplejoB.real + ComplejoA.imaginario*ComplejoB.imaginario)/magnitudB
            ComplejoRes.imaginario = (ComplejoB.real*ComplejoA.imaginario - ComplejoA.real*ComplejoB.imaginario)/magnitudB
            return ComplejoRes
        except ZeroDivisionError:
            return None
    
    def exponenciar(ComplejoBase, exponente):
        x = ComplejoBase.real
        y = ComplejoBase.imaginario

        if x == 0: #Si solo posee parte imaginaria
            if exponente % 4 == 1:
                return Complejo(0, y**exponente)
            elif exponente % 4 == 2:
                return Complejo(-(y**exponente), 0)
            elif exponente % 4 == 3:
                return Complejo(0, -(y**exponente))
            else:
                return Complejo(y**exponente, 0)

        aux = x**2 + y**2
        r = math.sqrt(aux)
        theta = math.atan( y / x ) 

        if x < 0 and y < 0: #Ajuste del angulo
            theta = 2*math.pi + theta
        elif x < 0 and y > 0:
            theta = math.pi + theta
        elif x > 0 and y < 0:
            theta = 2*math.pi + theta
        
        x = (r**exponente) * math.cos(exponente*theta)
        y = (r**exponente) * math.sin(exponente*theta)
        return Complejo(x,y)

    
    def graficar(DictComplejos):
        xs = []
        ys = []
        for numeroComplejo, leyenda in DictComplejos.items():
            if numeroComplejo != None:
                plt.scatter(numeroComplejo.real, numeroComplejo.imaginario  , label = leyenda)
                xs.append(numeroComplejo.real)
                ys.append(numeroComplejo.imaginario)
        
        x = max(xs)
        y = max(ys)

        plt.plot([-x-10, x+10], [0,0], "black")
        plt.plot([0,0], [-y-10, y + 10], "black")  #Para graficar los ejes
        plt.axis([ -x-10, x+10, -y-10, y+10 ]) #De donde a donde van los ejes
        plt.title("Grafica")
        
        plt.legend()
        plt.grid(True)
        
        plt.show()

#REGEX
def validarEntrada(texto):
    x,y = buscarCompleto(texto)
    if x==None and y==None:
        x,y = buscarReal(texto)
        if x==None and y==None:
            x,y = buscarImaginario(texto)
    if x==None and y==None:
        return None
    else:
        return Complejo(x,y)

def buscarCompleto(texto):
    try:
        aux = re.search("\s*(-?[0-9]+.?[0-9]*)\s*([\+-])\s*([0-9]*.?[0-9]*)\s*i", texto)
        real = aux.group(1)
        signo = aux.group(2)
        if aux.group(3) == "":
            imaginario = "1"
        else:
           imaginario = aux.group(3)
        imaginario = signo + imaginario
        return float(real),  float(imaginario)
    except Exception as e:
        return None,None

def buscarReal(texto):
    try:
        aux = re.search("\s*(-?[0-9]+.?[0-9]*)\s*", texto)
        real = aux.group(1)
        return float(real), 0
    except:
        return None, None

def buscarImaginario(texto):
    try:
        aux = re.search("\s*(-?)([0-9]*.?[0-9]*)\s*i\s*", texto)
        if aux.group(2) == "":
            imaginario = "1"
        else:
           imaginario = aux.group(2)
        if aux.group(1) == "":
            signo = "+"
        else:
            signo = "-"
        imaginario = signo + imaginario
        return 0, float(imaginario)
    except:
        return None, None


#Configuración de la ventana

ventana = Tk()
ventana.title("Calculadora de números complejos")
ventana.resizable(False,False)
#ventana.iconbitmap(r".../logo.ico") indicar el path de la imagen .ico
framePrincipal = Frame(ventana, width = 450, height = 500)
framePrincipal.pack()

#Labels
Complejo1Label = Label(framePrincipal, text = "Ingrese el primer número complejo.", padx = 10, pady = 10)
Complejo1Label.place(x = 25, y = 20)

Complejo2Label = Label(framePrincipal, text = "Ingrese el segundo número complejo.", padx = 10, pady = 10)
Complejo2Label.place(x = 20, y = 90)

numeroNLabel = Label(framePrincipal, text = "Ingrese un número en los reales.", padx = 10, pady = 10)
numeroNLabel.place(x = 33, y = 160)

labelSuma = Label(framePrincipal)
labelSuma.place(x =80, y =230)

labelResta = Label(framePrincipal)
labelResta.place(x = 80, y =260)

labelProducto = Label(framePrincipal)
labelProducto.place(x = 80, y =290)

labelCociente = Label(framePrincipal)
labelCociente.place(x = 80, y =320)

labelExponente = Label(framePrincipal)
labelExponente.place(x = 80, y =350)

#Entries
Complejo1Get = StringVar()
Complejo2Get = StringVar()
nGet = StringVar()

Complejo1Entry = Entry(framePrincipal, textvariable = Complejo1Get, width = 33)
Complejo1Entry.place(x = 30, y = 55)

Complejo2Entry = Entry(framePrincipal, textvariable = Complejo2Get, width = 33)
Complejo2Entry.place(x = 30, y = 125)

numeroNEntry = Entry(framePrincipal, textvariable = nGet, width =33)
numeroNEntry.place(x = 30, y = 195)


#Button
def funcionBoton():
    labelAviso.place_forget()    
    try:
        numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
        numeroComplejo2 = validarEntrada( Complejo2Get.get()  )
        n = float(nGet.get())

        resSuma = Complejo.sumar(numeroComplejo1, numeroComplejo2)
        resResta = Complejo.restar(numeroComplejo1, numeroComplejo2)
        resProducto = Complejo.multiplicar(numeroComplejo1, numeroComplejo2)
        resCociente = Complejo.dividir(numeroComplejo1, numeroComplejo2)
        resExponente = Complejo.exponenciar(numeroComplejo1, n)

        
        labelSuma['text'] = "Suma: ({}) + ({}) = {}".format(str(numeroComplejo1), str(numeroComplejo2), str(resSuma))

        
        labelResta['text'] = "Resta: ({}) - ({}) = {}".format(str(numeroComplejo1), str(numeroComplejo2), str(resResta))

     
        labelProducto['text'] = "Producto: ({}) * ({}) = {}".format(str(numeroComplejo1), str(numeroComplejo2), str(resProducto))

        
        labelCociente['text'] = "División: ({}) * ({}) = {}".format(str(numeroComplejo1), str(numeroComplejo2), str(resCociente))

        
        labelExponente['text'] = "Exponenciacioó: ({})^{} = {}".format(str(numeroComplejo1), n, str(resExponente))

        numeros = {numeroComplejo1: "Primer número", numeroComplejo2: "Segundo Número", resSuma: "Suma", resResta: "Resta", 
                    resProducto: "Producto", resCociente: "Division", resExponente: "Exponencial"}

        Complejo.graficar(numeros)
    except Exception as e:
        print(type(e))
        labelAviso.place(x = 80, y = 380)        
    

labelAviso = Label(framePrincipal, text = "Algo ha ocurrido, checa la entrada de los datos.")

CalcularButton = Button(framePrincipal, text = "Calcular", command = funcionBoton, width = 7, height = 7)
CalcularButton.place(x = 315, y = 75)



ventana.mainloop()

from tkinter import * 
from Validar import *
from Complejo import *
import numpy as np
import matplotlib.pyplot as plt
 

def evaluarTransformacion(complejoA, constanteA, constanteB):
    resComplejo =  (complejoA * constanteA) + constanteB
    if resComplejo.real == 0 and resComplejo.imaginario == 0:
        return None
    return resComplejo

def PuntoRecta(points):
    x1, y1 = points[0].real, points[0].imaginario
    x2, y2 = points[1].real, points[1].imaginario
    x3, y3 = points[2].real, points[2].imaginario
    if x1 == x2 and y1 == y2:
        graficar(points[0])
    elif x1 == x2 and y1 != y2:
        graficar(x = x1) 
    elif x1 != x2 and y1 == y2:
        graficar(y = y1) 
    else:
        pendiente = (y2-y1)/(x2-x1)
        graficar(pendienteLinea = pendiente, punto =  points[0])

    

def graficar(C = None, D = None, E = None, pendienteLinea = None, x = None, y = None, punto = None):
    fig, grafica = plt.subplots(1, figsize = (10,6))
    if C != None:
        text = "(x + ({}))^2 + (y + ({}))^2 = {}".format(C, D, -E+(D/2)**2 + (C/2)**2)
        R2 = (-E + (D/2)**2 + (C/2)**2)
        theta = np.linspace(0, 2*np.pi, 100)
        # the radius of the circle
        r = np.sqrt(R2)
        # compute x1 and x2
        x1 = r*np.cos(theta) - (C)
        x2 = r*np.sin(theta) - (D)
        # create the figure
        grafica.plot(x1, x2)
        grafica.set_aspect(1)
        grafica.plot( [-1000000, 1000000], [0, 0],  color = "black" )
        grafica.plot( [0, 0], [-1000000, 1000000], color = "black"  ) 
        grafica.set_xlim(-C - 3*r/2, -C + 3*r/2)
        grafica.set_ylim(-D - 3*r/2, -D + 3*r/2)
        grafica.grid()
        grafica.set_title(text)
        plt.show()
        

def TransformadaMoebius():

    ventanaTrans = Tk();
    ventanaTrans.title("Transformada de Moebius")
    frameTrans = Frame(ventanaTrans, width = 550, height = 500)
    frameTrans.pack()

    aGet = StringVar()
    bGet = StringVar()
    cGet = StringVar()
    dGet = StringVar()
    radioGet = StringVar()
    hGet = StringVar()
    kGet = StringVar()

    aEntry = Entry(frameTrans, textvariable = aGet, width = 25)
    aEntry.place(x = 30, y = 55)
    aLabel = Label(frameTrans, text = "Ingrese el valor de a")
    aLabel.place(x = 140, y = 55)

    bEntry = Entry(frameTrans, textvariable = bGet, width = 25)
    bEntry.place(x = 30, y = 125)
    bLabel = Label(frameTrans, text = "Ingrese el valor de b")
    bLabel.place(x = 140, y = 125)

    cEntry = Entry(frameTrans, textvariable = cGet, width = 25)
    cEntry.place(x = 30, y = 195)
    cLabel = Label(frameTrans, text = "Ingrese el valor de c")
    cLabel.place(x = 140, y = 195)

    dEntry = Entry(frameTrans, textvariable = dGet, width = 25)
    dEntry.place(x = 30, y = 265)
    dLabel = Label(frameTrans, text = "Ingrese el valor de d")
    dLabel.place(x = 140, y = 265)

    radioEntry = Entry(frameTrans, textvariable = radioGet, width = 25)
    radioEntry.place(x = 30, y = 325)
    radioLabel = Label(frameTrans, text = "Ingrese el valor del radio")
    radioLabel.place(x = 140, y = 325)

    hEntry = Entry(frameTrans, textvariable = hGet, width = 25)
    hEntry.place(x = 30, y = 385)
    hLabel = Label(frameTrans, text = "Ingrese el valor de h")
    hLabel.place(x = 140, y = 385)

    kEntry = Entry(frameTrans, textvariable = kGet, width = 25)
    kEntry.place(x = 30, y = 445)
    kLabel = Label(frameTrans, text = "Ingrese el valor de k")
    kLabel.place(x = 140, y = 445)

    def funcionBoton():
        
        a = validarEntrada(aGet.get())
        b = validarEntrada(bGet.get())
        c = validarEntrada(cGet.get())
        d = validarEntrada(dGet.get())
        radio = float(radioGet.get())
        h = float(hGet.get())
        k = float(kGet.get())

        points = []
        complejo1 = Complejo(h,k+radio)
        complejo2 = Complejo(h,k-radio)
        complejo3 = Complejo(h+radio,k)
        complejo4 = Complejo(h-radio,k)

        flag = True
        arribaComplejo1 = evaluarTransformacion(complejo1, a, b)
        abajoComplejo1 = evaluarTransformacion(complejo1, c, d)
        if abajoComplejo1.real == 0 and abajoComplejo1.imaginario == 0:
            flag = False
        else:
            points.append( arribaComplejo1/abajoComplejo1 )

        arribaComplejo2 = evaluarTransformacion(complejo2, a, b)
        abajoComplejo2 = evaluarTransformacion(complejo2, c, d)
        if abajoComplejo2.real == 0 and abajoComplejo2.imaginario == 0:
            flag = False
        else:
            points.append( arribaComplejo2/abajoComplejo2 )

        arribaComplejo3 = evaluarTransformacion(complejo3, a, b)
        abajoComplejo3 = evaluarTransformacion(complejo3, c, d)
        if abajoComplejo3.real == 0 and abajoComplejo3.imaginario == 0:
            flag = False
        else:
            points.append( arribaComplejo3/abajoComplejo3 )
            
        arribaComplejo4 = evaluarTransformacion(complejo4, a, b)
        abajoComplejo4 = evaluarTransformacion(complejo4, c, d)
        if abajoComplejo4.real == 0 and abajoComplejo4.imaginario == 0:
            flag = False
        else:
            points.append( arribaComplejo4/abajoComplejo4 )
        

        if flag:
            x1, y1 = points[0].real, points[0].imaginario
            x2, y2 = points[1].real, points[1].imaginario
            x3, y3 = points[2].real, points[2].imaginario
            k1 = x1**2 + y1**2
            k2 = x2**2 + y2**2
            k3 = x3**2 + y3**2

            determinante = x1*(y2 - y3) - x2*(y1 - y3) + x3*(y1 - y2)
            if determinante == 0:
                PuntoRecta(points)
            else:
                C1 = ( -k1*(y2-y3) + k2*(y1-y3) - k3*(y1-y2) ) / determinante
                D1 = (x1*(k3-k2) - x2*(k3-k1) + x3*(k2-k1)) / determinante
                E1 = (x1*(k2*y3 - k3*y2) - x2*(k1*y3 - k3*y1) + x3*(k1*y2 - k2*y1)) / determinante
                graficar(C =  C1, D = D1, E = E1)
        else:
            PuntoRecta(points)
            

            
            
            
        



        
        











    Calcular1Button = Button(frameTrans, text = "Calcular", command = funcionBoton, width = 7, height = 1)
    Calcular1Button.place(x = 30, y = 10)    

    


    #arriba = Complejo.multiplicar(ComplejoA, a)
    #arriba = Complejo.sumar(arriba, b)
    #abajo = Complejo.multiplicar(ComplejoA, c)
    #abajo = Complejo.sumar(arriba, d)
    ventanaTrans.mainloop()


TransformadaMoebius()


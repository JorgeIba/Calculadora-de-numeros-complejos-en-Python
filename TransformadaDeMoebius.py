from tkinter import * 
from Validar import *
from Complejo import *
import numpy as np
import matplotlib.pyplot as plt
 

def evaluarTransformacion(complejoA, constanteA, constanteB):
    resComplejo =  (complejoA * constanteA) + constanteB
    return resComplejo

def PuntoRecta(points):
    x1, y1 = points[0].real, points[0].imaginario
    x2, y2 = points[1].real, points[1].imaginario
    x3, y3 = points[2].real, points[2].imaginario
    if x1 == x2 and y1 == y2:
        graficar(punto1 = points[0])
    else:
        graficar(punto1 = points[0], punto2 = points[1])

def graficar(C = None, D = None, E = None, punto1 = None, punto2=None):
    fig, grafica = plt.subplots(1, figsize = (10,6))
    grafica.plot( [-1000000, 1000000], [0, 0],  color = "black" )
    grafica.plot( [0, 0], [-1000000, 1000000], color = "black"  ) 
    grafica.grid()
    if C != None: #Circulo
        text = r"$[x - ({})]^{} + [y - ({})]^{} = {}$".format(-round(C,3),2, -round(D,3),2, round(-E+(D/2)**2 + (C/2)**2, 3))
        R2 = (-E + (D/2)**2 + (C/2)**2)
        theta = np.linspace(0, 2*np.pi, 100)
        r = np.sqrt(R2)
        x1 = r*np.cos(theta) - (C)
        x2 = r*np.sin(theta) - (D)
        grafica.plot(x1, x2, color = 'red')
        grafica.set_aspect(1)
        grafica.set_xlim(-C - 3*r/2, -C + 3*r/2)
        grafica.set_ylim(-D - 3*r/2, -D + 3*r/2)
        grafica.set_title(text)
    elif punto1 != None and punto2 == None: #Punto
        grafica.set_title("Punto: " + str(punto1))
        grafica.scatter(punto1.real, punto1.imaginario, color = 'red')
        grafica.set_xlim(punto1.real - 5, punto1.real + 5)
        grafica.set_ylim(punto1.imaginario - 5, punto1.imaginario + 5)
    else:
        if punto1.real == punto2.real and punto1.imaginario!=punto2.imaginario: #Recta y = C
            grafica.set_title("Recta: y = {}".format(punto1.real))
            grafica.plot([punto1.real, punto1.real], [-100000, 100000], color = 'red')
            grafica.set_xlim(punto1.real - 5, punto1.real + 5)
            grafica.set_ylim(-10, 10)
        
        elif punto1.real != punto2.real and punto1.imaginario==punto2.imaginario: #Recta x = C
            grafica.set_title("Recta: x = {}".format(punto1.imaginario))
            grafica.plot([-100000, 100000], [punto1.imaginario, punto1.imaginario], color = 'red')
            grafica.set_xlim(-10, 10)
            grafica.set_ylim(punto1.imaginario - 5, punto1.imaginario + 5)
        else:   #Recta y = mx + C
            m = (punto2.imaginario - punto1.imaginario)/(punto2.real - punto1.real)
            constant = m*punto1.real + punto1.imaginario
            grafica.set_title( "Recta: y = {}*x + {}".format(m, constant) )
            grafica.plot([-100000, 100000], [ m*(-100000) + constant, m*(100000) + constant ], color = 'red')
            grafica.set_xlim(-15, 15)
            grafica.set_ylim(constant - 10, constant + 10)

    
    plt.show()

        
def TransformadaMoebius(ventanaTrans):
    #ventanaTrans = Tk();
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

    #expresionLabel = Label(frameTrans, text = "az ]")

    def funcionBotonTransformada():
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
        arribaComplejo1 = (complejo1 * a) + b
        abajoComplejo1 = (complejo1 * c) + d
        if abajoComplejo1.real == 0 and abajoComplejo1.imaginario == 0:
            flag = False
        else:
            points.append( arribaComplejo1/abajoComplejo1 )

        arribaComplejo2 = (complejo2 * a) + b
        abajoComplejo2 = (complejo2 * c) + d
        if abajoComplejo2.real == 0 and abajoComplejo2.imaginario == 0:
            flag = False
        else:
            points.append( arribaComplejo2/abajoComplejo2 )

        arribaComplejo3 = (complejo3 * a) + b
        abajoComplejo3 = (complejo3 * c) + d
        if abajoComplejo3.real == 0 and abajoComplejo3.imaginario == 0:
            flag = False
        else:
            points.append( arribaComplejo3/abajoComplejo3 )
            
        arribaComplejo4 = (complejo4 * a) + b
        abajoComplejo4 = (complejo4 * c) + d
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
            

            
    Calcular1Button = Button(frameTrans, text = "Calcular", command = funcionBotonTransformada, width = 7, height = 1)
    Calcular1Button.place(x = 30, y = 10)    

    
    #ventanaTrans.mainloop()





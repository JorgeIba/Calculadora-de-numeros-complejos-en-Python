from tkinter import *
from Validar import *
from Complejo import *
from TransformadaDeMoebius import *
import threading



def quit():
    exit()

#TransformadaMoebius()

ventana = Tk()
ventana.title("Calculadora de números complejos")

ventana.protocol("WM_DELETE_WINDOW", quit)

#ventana.iconbitmap(r".../logo.ico") indicar el path de la imagen .ico
framePrincipal = Frame(ventana, width = 550, height = 500)
framePrincipal.pack()

#Labels
Complejo1Label = Label(framePrincipal, text = "Ingrese el primer número complejo.", padx = 10, pady = 10)
Complejo1Label.place(x = 25, y = 20)

Complejo2Label = Label(framePrincipal, text = "Ingrese el segundo número complejo.", padx = 10, pady = 10)
Complejo2Label.place(x = 20, y = 90)

numeroNLabel = Label(framePrincipal, text = "Ingrese un número en los naturales.", padx = 10, pady = 10)
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

        resSuma = numeroComplejo1 + numeroComplejo2
        resResta = numeroComplejo1 - numeroComplejo2
        resProducto = numeroComplejo1 * numeroComplejo2
        resCociente = numeroComplejo1 / numeroComplejo2
        resPotencia = Complejo.potenciar(numeroComplejo1, n)

        
        labelSuma['text'] = "Suma: ({}) + ({}) = {}".format(str(numeroComplejo1), str(numeroComplejo2), str(resSuma))

        
        labelResta['text'] = "Resta: ({}) - ({}) = {}".format(str(numeroComplejo1), str(numeroComplejo2), str(resResta))

     
        labelProducto['text'] = "Producto: ({}) * ({}) = {}".format(str(numeroComplejo1), str(numeroComplejo2), str(resProducto))

        
        labelCociente['text'] = "División: ({}) * ({}) = {}".format(str(numeroComplejo1), str(numeroComplejo2), str(resCociente))

        
        labelExponente['text'] = "Potenciacion: ({})^{} = {}".format(str(numeroComplejo1), n, str(resPotencia))

        numeros = {numeroComplejo1: "Primer número", numeroComplejo2: "Segundo Número", resSuma: "Suma", resResta: "Resta", 
                    resProducto: "Producto", resCociente: "Division", resPotencia: "Potenciacion"}


        textoRaices = ""
        raices = Complejo.raices(numeroComplejo2, int(n))
        for numero, legend in raices.items():
            textoRaices += legend + ":  " + str(numero) + "\n"
            
        labelRaices['text'] = textoRaices

        ventanaRaices.update()
        ventanaRaices.deiconify()

        Complejo.graficar(numeros, raices)      
        
        
    except Exception as e:
        print(type(e))
        print(e)
        labelAviso.place(x = 80, y = 380)        
    

labelAviso = Label(framePrincipal, text = "Algo ha ocurrido, checa la entrada de los datos.")

CalcularButton = Button(framePrincipal, text = "Calcular", command = funcionBoton, width = 7, height = 7)
CalcularButton.place(x = 315, y = 75)


def startMoebius():
    top = Toplevel()
    TransformadaMoebius(top)


TransformadaButton = Button(framePrincipal, text = "Calcular Transformada de Moebius", command = startMoebius, width = 25, height = 2)
TransformadaButton.place(x = 310, y = 200)


#Ventana para las raices
def ocultarVentana():
    ventanaRaices.withdraw()
    return

ventanaRaices = Tk()
ventanaRaices.title("Raices Segundo Numero Complejo")
ventanaRaices.withdraw()
ventanaRaices.protocol("WM_DELETE_WINDOW", ocultarVentana)


frameRaices = Frame(ventanaRaices, width = 450, height = 700)
frameRaices.pack()

labelRaices = Label(frameRaices)
labelRaices.place(x = 165, y = 15)


ventanaRaices.mainloop()
ventana.mainloop()

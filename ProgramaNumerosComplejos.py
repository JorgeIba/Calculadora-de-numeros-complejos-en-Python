from tkinter import *
from Validar import *
from Complejo import *
from TransformadaDeMoebius import *
from Ventana import *


def quit():
    exit()

def ventanaSecundaria(funcion):
    top = Toplevel()
    funcion(top)

def main():
    #*Ventanas
    ventana = Ventana(title = "Calculadora de Numeros Complejos")
    ventana.window.protocol("WM_DELETE_WINDOW", quit)
    ventanaRaices = Ventana(title = "Raices Segundo Numero Complejo")
    ventanaRaices.ocultar()
    ventanaRaices.window.protocol("WM_DELETE_WINDOW", ventanaRaices.ocultar)



    #ventana.window.iconbitmap(r".../logo.ico") indicar el path de la imagen .ico
    #*Frames
    framePrincipal = Frame(ventana.window, width = 940, height = 500)
    framePrincipal.pack()
    frameRaices = Frame(ventanaRaices.window, width = 450, height = 700)
    frameRaices.pack()

    #*Labels
    Complejo1Label = Label(framePrincipal, text = "Ingrese el primer numero complejo.", padx = 10, pady = 10)
    Complejo1Label.place(x = 25, y = 20)

    Complejo2Label = Label(framePrincipal, text = "Ingrese el segundo numero complejo.", padx = 10, pady = 10)
    Complejo2Label.place(x = 25, y = 90)

    numeroNLabel = Label(framePrincipal, text = "Ingrese un numero en los naturales.", padx = 10, pady = 10)
    numeroNLabel.place(x = 28, y = 160)

    labelSuma = Label(framePrincipal)
    labelSuma.place(x = 15, y =245)

    labelResta = Label(framePrincipal)
    labelResta.place(x = 15, y =275)

    labelProducto = Label(framePrincipal)
    labelProducto.place(x = 15, y =305)

    labelCociente = Label(framePrincipal)
    labelCociente.place(x = 15, y =335)

    labelExponente = Label(framePrincipal)
    labelExponente.place(x = 15, y =365)

    #? Exponencial y Logaritmo
    labelExponencial = Label(framePrincipal)
    labelExponencial.place(x = 15, y = 395)

    labelLogaritmo = Label(framePrincipal)
    labelLogaritmo.place(x = 15, y = 425)

    #? Trigonometricas

    labelSeno = Label(framePrincipal)
    labelSeno.place(x = 270, y = 245)

    labelCoseno = Label(framePrincipal)
    labelCoseno.place(x = 270, y = 275)

    labelTangente = Label(framePrincipal)
    labelTangente.place(x = 270, y = 305)

    labelCotangente = Label(framePrincipal)
    labelCotangente.place(x = 270, y = 335)

    labelCosecante = Label(framePrincipal)
    labelCosecante.place(x = 270, y = 365)

    labelSecante = Label(framePrincipal)
    labelSecante.place(x = 270, y = 395)

    #? Trigonometricas Hiperbolicas
    labelSenoH = Label(framePrincipal)
    labelSenoH.place(x = 490, y = 245)

    labelCosenoH = Label(framePrincipal)
    labelCosenoH.place(x = 490, y = 275)

    labelTangenteH = Label(framePrincipal)
    labelTangenteH.place(x = 490, y = 305)

    labelCotangenteH = Label(framePrincipal)
    labelCotangenteH.place(x = 490, y = 335)

    labelCosecanteH = Label(framePrincipal)
    labelCosecanteH.place(x = 490, y = 365)

    labelSecanteH = Label(framePrincipal)
    labelSecanteH.place(x = 490, y = 395)

    #? Trigonometricas Inversas
    labelArcSeno = Label(framePrincipal)
    labelArcSeno.place(x = 705, y = 245)

    labelArcCoseno = Label(framePrincipal)
    labelArcCoseno.place(x = 705, y = 275)

    labelArcTangente = Label(framePrincipal)
    labelArcTangente.place(x = 705, y = 305)

    labelArcCotangente = Label(framePrincipal)
    labelArcCotangente.place(x = 705, y = 335)

    labelArcCosecante = Label(framePrincipal)
    labelArcCosecante.place(x = 705, y = 365)

    labelArcSecante = Label(framePrincipal)
    labelArcSecante.place(x = 705, y = 395)
    

    #Labels ventana raices
    labelRaices = Label(frameRaices)
    labelRaices.place(x = 165, y = 15)

    labelAviso = Label(framePrincipal, text = "Algo ha ocurrido, checa la entrada de los datos o Math Error")


    #*Entries
    Complejo1Get = StringVar()
    Complejo2Get = StringVar()
    nGet = StringVar()

    Complejo1Entry = Entry(framePrincipal, textvariable = Complejo1Get, width = 33)
    Complejo1Entry.place(x = 30, y = 55)

    Complejo2Entry = Entry(framePrincipal, textvariable = Complejo2Get, width = 33)
    Complejo2Entry.place(x = 30, y = 125)

    numeroNEntry = Entry(framePrincipal, textvariable = nGet, width =33)
    numeroNEntry.place(x = 30, y = 195)


    #*Buttons
        
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

            
            labelCociente['text'] = "Division: ({}) * ({}) = {}".format(str(numeroComplejo1), str(numeroComplejo2), str(resCociente))

            
            labelExponente['text'] = "Potenciacion: ({})^{} = {}".format(str(numeroComplejo1), n, str(resPotencia))

            numeros = {numeroComplejo1: "Primer numero", numeroComplejo2: "Segundo Numero", resSuma: "Suma", resResta: "Resta", 
                        resProducto: "Producto", resCociente: "Division", resPotencia: "Potenciacion"}


            textoRaices = ""
            raices = Complejo.raices(numeroComplejo2, int(n))
            for numero, legend in raices.items():
                textoRaices += legend + ":  " + str(numero) + "\n"
                
            labelRaices['text'] = textoRaices

            ventanaRaices.mostrar()

            Complejo.graficar(numeros, raices)      

        except Exception as e:
            print(type(e))
            print(e)
            labelAviso.place(x = 330, y = 460)        

    def funcionBotonSen():
        labelAviso.place_forget()  
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resSen = Complejo.seno(numeroComplejo1)
            labelSeno['text'] = "Sen({}) = {}".format(str(numeroComplejo1), str(resSen))
            Complejo.graficarPunto(resSen)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 

    def funcionBotonCos():
        labelAviso.place_forget()  
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resCos = Complejo.coseno(numeroComplejo1)
            labelCoseno['text'] = "Cos({}) = {}".format(str(numeroComplejo1), str(resCos))
            Complejo.graficarPunto(resCos)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 
    
    def funcionBotonTan():
        labelAviso.place_forget()  
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resTan = Complejo.tangente(numeroComplejo1)
            labelTangente['text'] = "Tan({}) = {}".format(str(numeroComplejo1), str(resTan))
            Complejo.graficarPunto(resTan)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 
        
    def funcionBotonCot():
        labelAviso.place_forget()  
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resCot = Complejo.cotangente(numeroComplejo1)
            labelCotangente['text'] = "Cot({}) = {}".format(str(numeroComplejo1), str(resCot))
            Complejo.graficarPunto(resCot)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 

    def funcionBotonCsc():
        labelAviso.place_forget()  
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resCsc = Complejo.cosecante(numeroComplejo1)
            labelCosecante['text'] = "Csc({}) = {}".format(str(numeroComplejo1), str(resCsc))
            Complejo.graficarPunto(resCsc)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 

    def funcionBotonSec():
        labelAviso.place_forget()  
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resSec = Complejo.secante(numeroComplejo1)
            labelSecante['text'] = "Csc({}) = {}".format(str(numeroComplejo1), str(resSec))
            Complejo.graficarPunto(resSec)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 

    def funcionBotonSenH():
        labelAviso.place_forget()  
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resSenh = Complejo.senoHiperbolico(numeroComplejo1)
            labelSenoH['text'] = "Senh({}) = {}".format(str(numeroComplejo1), str(resSenh))
            Complejo.graficarPunto(resSenh)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 
    
    def funcionBotonCosH():
        labelAviso.place_forget()  
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resCosh = Complejo.cosenoHiperbolico(numeroComplejo1)
            labelCosenoH['text'] = "Cosh({}) = {}".format(str(numeroComplejo1), str(resCosh))
            Complejo.graficarPunto(resCosh)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 

    def funcionBotonTanH():
        labelAviso.place_forget()  
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resTanh = Complejo.tangenteHiperbolico(numeroComplejo1)
            labelTangenteH['text'] = "Tanh({}) = {}".format(str(numeroComplejo1), str(resTanh))
            Complejo.graficarPunto(resTanh)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 

    def funcionBotonCotH():
        labelAviso.place_forget()  
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resCoth = Complejo.cotangenteHiperbolico(numeroComplejo1)
            labelCotangenteH['text'] = "Coth({}) = {}".format(str(numeroComplejo1), str(resCoth))
            Complejo.graficarPunto(resCoth)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 
    
    def funcionBotonCscH():
        labelAviso.place_forget()  
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resCsch = Complejo.cosecanteHiperbolico(numeroComplejo1)
            labelCosecanteH['text'] = "Csch({}) = {}".format(str(numeroComplejo1), str(resCsch))
            Complejo.graficarPunto(resCsch)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 
    
    def funcionBotonSecH():
        labelAviso.place_forget()  
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resSech = Complejo.secanteHiperbolico(numeroComplejo1)
            labelSecanteH['text'] = "Sech({}) = {}".format(str(numeroComplejo1), str(resSech))
            Complejo.graficarPunto(resSech)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 

    def funcionBotonArcSen():
        labelAviso.place_forget()  
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resArcSen = Complejo.arcoSeno(numeroComplejo1)
            labelArcSeno['text'] = "ArcSen({}) = {}".format(str(numeroComplejo1), str(resArcSen))
            Complejo.graficarPunto(resArcSen)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 

    def funcionBotonArcCos():
        labelAviso.place_forget()  
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resArcCos = Complejo.arcoCoseno(numeroComplejo1)
            labelArcCoseno['text'] = "ArcCos({}) = {}".format(str(numeroComplejo1), str(resArcCos))
            Complejo.graficarPunto(resArcCos)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 

    def funcionBotonArcTan():
        labelAviso.place_forget()  
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resArcTan = Complejo.arcoTangente(numeroComplejo1)
            labelArcTangente['text'] = "ArcTan({}) = {}".format(str(numeroComplejo1), str(resArcTan))
            Complejo.graficarPunto(resArcTan)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 

    def funcionBotonArcCot():
        labelAviso.place_forget()  
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resArcCot = Complejo.arcoCotangente(numeroComplejo1)
            labelArcCotangente['text'] = "ArcCot({}) = {}".format(str(numeroComplejo1), str(resArcCot))
            Complejo.graficarPunto(resArcCot)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 

    def funcionBotonArcCsc():
        labelAviso.place_forget()    
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resArcCsc = Complejo.arcoCosecante(numeroComplejo1)
            labelArcCosecante['text'] = "ArcCsc({}) = {}".format(str(numeroComplejo1), str(resArcCsc))
            Complejo.graficarPunto(resArcCsc)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 

    def funcionBotonArcSec():
        labelAviso.place_forget()    
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resArcSec = Complejo.arcoSecante(numeroComplejo1)
            labelArcSecante['text'] = "ArcSec({}) = {}".format(str(numeroComplejo1), str(resArcSec))
            Complejo.graficarPunto(resArcSec)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460)    

    def funcionBotonExponencial():
        labelAviso.place_forget()    
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resExponencial = Complejo.exponencial(numeroComplejo1)
            labelExponencial['text'] = "e^({}) = {}".format(str(numeroComplejo1), str(resExponencial))
            Complejo.graficarPunto(resExponencial)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 

    def funcionBotonLogaritmo():
        labelAviso.place_forget()    
        try:
            numeroComplejo1 = validarEntrada( Complejo1Get.get()  )
            resLogaritmo = Complejo.logaritmoNatural(numeroComplejo1)
            labelLogaritmo['text'] = "ln({}) = {}".format(str(numeroComplejo1), str(resLogaritmo))
            Complejo.graficarPunto(resLogaritmo)
        except Exception as e:
            print(type(e))
            labelAviso.place(x = 320, y = 460) 

    CalcularButton = Button(framePrincipal, text = "Calcular", command = funcionBoton, width = 7, height = 2)
    CalcularButton.place(x = 260, y = 25)

    TransformadaButton = Button(framePrincipal, text = "Transformada\n de\n Moebius", command = lambda arg=TransformadaMoebius: ventanaSecundaria(arg), width = 10, height = 4)
    TransformadaButton.place(x = 250, y = 70)
    
    #?Exponencial y logaritmo

    ExponencialButton = Button(framePrincipal, text = "Exponencial", command = funcionBotonExponencial, width = 10, height = 1)
    ExponencialButton.place(x = 250, y = 160)

    LogaritmoButton = Button(framePrincipal, text = "Logaritmo\nNatural", command = funcionBotonLogaritmo, width = 10, height = 2)
    LogaritmoButton.place(x = 250, y = 190)


    #?Trigonometricas

    SenoButton = Button(framePrincipal, text = "Seno", command = funcionBotonSen, width = 10, height = 1)
    SenoButton.place(x = 400, y = 40)
    
    CosenoButton = Button(framePrincipal, text = "Coseno", command = funcionBotonCos, width = 10, height = 1)
    CosenoButton.place(x = 400, y = 70)

    TangenteButton = Button(framePrincipal, text = "Tangente", command = funcionBotonTan, width = 10, height = 1)
    TangenteButton.place(x = 400, y = 100)

    CotangenteButton = Button(framePrincipal, text = "Cotangente", command = funcionBotonCot, width = 10, height = 1)
    CotangenteButton.place(x = 400, y = 130)

    CosecanteButton = Button(framePrincipal, text = "Cosecante", command = funcionBotonCsc, width = 10, height = 1)
    CosecanteButton.place(x = 400, y = 160)

    SecanteButton = Button(framePrincipal, text = "Secante", command = funcionBotonSec, width = 10, height = 1)
    SecanteButton.place(x = 400, y = 190)
    
    #? Trigonometricas Hiperbolicas
    SenoHButton = Button(framePrincipal, text = "SenoH", command = funcionBotonSenH, width = 10, height = 1)
    SenoHButton.place(x = 600, y = 40)

    CosenoHButton = Button(framePrincipal, text = "CosenoH", command = funcionBotonCosH, width = 10, height = 1)
    CosenoHButton.place(x = 600, y = 70)

    TangenteHButton = Button(framePrincipal, text = "TangenteH", command = funcionBotonTanH, width = 10, height = 1)
    TangenteHButton.place(x = 600, y = 100)

    CotangenteHButton = Button(framePrincipal, text = "CotangenteH", command = funcionBotonCotH, width = 10, height = 1)
    CotangenteHButton.place(x = 600, y = 130)

    CosecanteHButton = Button(framePrincipal, text = "CosecanteH", command = funcionBotonCscH, width = 10, height = 1)
    CosecanteHButton.place(x = 600, y = 160)

    SecanteHButton = Button(framePrincipal, text = "SecanteH", command = funcionBotonSecH, width = 10, height = 1)
    SecanteHButton.place(x = 600, y = 190)

    #? Trigonometricas Inversas
    ArcSenoButton = Button(framePrincipal, text = "Arco Seno", command = funcionBotonArcSen, width = 13, height = 1)
    ArcSenoButton.place(x = 800, y = 40)

    ArcCosenoButton = Button(framePrincipal, text = "Arco Coseno", command = funcionBotonArcCos, width = 13, height = 1)
    ArcCosenoButton.place(x = 800, y = 70)

    ArcTangenteButton = Button(framePrincipal, text = "Arco Tangente", command = funcionBotonArcTan, width = 13, height = 1)
    ArcTangenteButton.place(x = 800, y = 100)

    ArcCotangenteButton = Button(framePrincipal, text = "Arco Cotangente", command = funcionBotonArcCot, width = 13, height = 1)
    ArcCotangenteButton.place(x = 800, y = 130)

    ArcCosecanteButton = Button(framePrincipal, text = "Arco Cosecante", command = funcionBotonArcCsc, width = 13, height = 1)
    ArcCosecanteButton.place(x = 800, y = 160)

    ArcSecanteButton = Button(framePrincipal, text = "Arco Secante", command = funcionBotonArcSec, width = 13, height = 1)
    ArcSecanteButton.place(x = 800, y = 190)

    #* Mainloops
    ventanaRaices.window.mainloop()
    ventana.window.mainloop()


main()


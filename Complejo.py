import math
import matplotlib.pyplot as plt


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
            x = round(self.real, 4)
            y = round(self.imaginario, 4) #Redondeo a 3 decimales
            return "{} + {}i".format(x, y)
        elif self.imaginario < 0:
            x = round(self.real,4)
            y = round(self.imaginario,4)  #Redondeo a 3 decimales
            return "{} - {}i".format(x, -y)

    def __add__(self, ComplejoB):
        ComplejoRes = Complejo()
        ComplejoRes.real= self.real + ComplejoB.real
        ComplejoRes.imaginario= self.imaginario + ComplejoB.imaginario
        return ComplejoRes
    
    def __sub__(self, ComplejoB):
        ComplejoRes = Complejo()
        ComplejoRes.real = self.real - ComplejoB.real
        ComplejoRes.imaginario = self.imaginario - ComplejoB.imaginario
        return ComplejoRes

    def __mul__(self, ComplejoB):
        ComplejoRes = Complejo()
        ComplejoRes.real = self.real*ComplejoB.real - self.imaginario*ComplejoB.imaginario 
        ComplejoRes.imaginario = self.real*ComplejoB.imaginario + self.imaginario*ComplejoB.real
        return ComplejoRes
    
    def __truediv__(self, ComplejoB):
        try:
            ComplejoRes = Complejo()
            magnitudB =  ComplejoB.real**2 + ComplejoB.imaginario**2
            ComplejoRes.real = (self.real*ComplejoB.real + self.imaginario*ComplejoB.imaginario)/magnitudB
            ComplejoRes.imaginario = (ComplejoB.real*self.imaginario - self.real*ComplejoB.imaginario)/magnitudB
            return ComplejoRes
        except ZeroDivisionError:
            return None
    

    def potenciar(ComplejoBase, exponente):
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

    def raices(ComplejoA, n):
        dictRaices = {}
        x = ComplejoA.real
        y = ComplejoA.imaginario
        r = (x**2 + y**2)**(1/2)
        r = r**(1/n)
        theta = Complejo.angulo(ComplejoA)

        for i in range(0,n):
            real = math.cos( (theta + 2*math.pi*i)/n )
            imaginaria = math.sin( (theta + 2*math.pi*i)/n  )
            ComplejoRes = Complejo( r*real, r*imaginaria  )
            dictRaices[ComplejoRes] = "Z" + str(i)
        
        return dictRaices


    def exponencial(ComplejoA):
        ComplejoRes = Complejo()
        ComplejoRes.real = math.exp(ComplejoA.real) * math.cos(ComplejoA.imaginario)
        ComplejoRes.imaginario = math.exp(ComplejoA.real) * math.sin(ComplejoA.imaginario)
        return ComplejoRes

    def seno(ComplejoA):
        ComplejoRes = Complejo()
        ComplejoRes = Complejo.exponencial(ComplejoA*Complejo(0,1)) - Complejo.exponencial(ComplejoA*Complejo(0,-1))
        ComplejoRes = ComplejoRes/Complejo(0,2)
        return ComplejoRes

    def coseno(ComplejoA):
        ComplejoRes = Complejo()
        ComplejoRes = Complejo.exponencial(ComplejoA*Complejo(0,1)) + Complejo.exponencial(ComplejoA*Complejo(0,-1))
        ComplejoRes = ComplejoRes/Complejo(2,0)
        return ComplejoRes

    def tangente(ComplejoA):
        return Complejo.seno(ComplejoA) / Complejo.coseno(ComplejoA)
    
    def cotangente(ComplejoA):
        return Complejo(1,0) / Complejo.tangente(ComplejoA)

    def cosecante(ComplejoA):
        ComplejoSeno = Complejo.seno(ComplejoA)
        return Complejo(1,0) / ComplejoSeno

    def secante(ComplejoA):
        ComplejoCoseno = Complejo.coseno(ComplejoA)
        return Complejo(1,0) / ComplejoCoseno
    
    def senoHiperbolico(ComplejoA):
        return Complejo(0,-1) * Complejo.seno( Complejo(0, 1) * ComplejoA  )
    
    def cosenoHiperbolico(ComplejoA):
        return Complejo.coseno( Complejo(0,1) * ComplejoA )

    def tangenteHiperbolico(ComplejoA):
        return Complejo.senoHiperbolico(ComplejoA)/Complejo.cosenoHiperbolico(ComplejoA)

    def cotangenteHiperbolico(ComplejoA):
        return Complejo(1,0) / Complejo.tangenteHiperbolico(ComplejoA)

    def cosecanteHiperbolico(ComplejoA):
        ComplejoSenh = Complejo.senoHiperbolico(ComplejoA)
        return Complejo(1,0) / ComplejoSenh

    def secanteHiperbolico(ComplejoA):
        ComplejoCosh = Complejo.cosenoHiperbolico(ComplejoA)
        return Complejo(1,0) / ComplejoCosh

    def angulo(ComplejoA):
        x = ComplejoA.real
        y = ComplejoA.imaginario
        if x==0:
            if y>0:
                theta = math.pi/2
            else:
                theta = 3*math.pi/2
        elif y == 0:
            if x > 0:
                theta = 0
            else:
                theta = math.pi
        elif x == 0 and y == 0:
            theta = 0
        else:
            theta = math.atan( y / x ) 

        if x < 0 and y < 0: #Ajuste del angulo
            theta = 2*math.pi + theta
        elif x < 0 and y > 0:
            theta = math.pi + theta
        elif x > 0 and y < 0:
            theta = 2*math.pi + theta
        return theta


    def logaritmoNatural(ComplejoA):
        x = ComplejoA.real
        y = ComplejoA.imaginario
        theta = Complejo.angulo(ComplejoA)
        r = (x**2 + y**2)**(1/2)
        if r == 0:
            return None
        return Complejo(math.log(r),theta)
    
    def arcoSeno(ComplejoA):
        
        ComplejoRaices = Complejo.raices( Complejo(1,0)  - ComplejoA*ComplejoA   , 2 )
        Raiz = list(ComplejoRaices.keys())
        Raiz = Raiz[0]
        ComplejoArgumento = Complejo(0,1)*ComplejoA + Raiz
        return Complejo(0,-1) * Complejo.logaritmoNatural(ComplejoArgumento)

    def arcoCoseno(ComplejoA):
        ComplejoRaices = Complejo.raices(ComplejoA*ComplejoA  -  Complejo(1,0)  , 2 )
        Raiz = list(ComplejoRaices.keys())
        Raiz = Raiz[0]
        ComplejoArgumento = ComplejoA + Raiz
        return Complejo(0,-1) * Complejo.logaritmoNatural(ComplejoArgumento)

    def arcoTangente(ComplejoA):
        ComplejoArgumento = (Complejo(0,1) + ComplejoA) / (Complejo(0,1) - ComplejoA )
        return (Complejo(0,1)/Complejo(2,0))  *  Complejo.logaritmoNatural(ComplejoArgumento)
        
    def arcoCotangente(ComplejoA):
        ComplejoArgumento = (ComplejoA - Complejo(0,1)) / (ComplejoA + Complejo(0,1) )
        return (Complejo(0,1)/Complejo(2,0))  *  Complejo.logaritmoNatural(ComplejoArgumento)

    def arcoCosecante(ComplejoA):
        ComplejoRaices = Complejo.raices(Complejo(1,0) - Complejo(1,0) / (ComplejoA*ComplejoA) , 2 )
        Raiz = list(ComplejoRaices.keys())
        Raiz = Raiz[0]
        ComplejoArgumento = (Complejo(0,1) / ComplejoA) + Raiz
        return Complejo(0,-1) * Complejo.logaritmoNatural(ComplejoArgumento)

    def arcoSecante(ComplejoA):
        ComplejoRaices = Complejo.raices(Complejo(1,0) / (ComplejoA*ComplejoA)  -  Complejo(1,0)  , 2 )
        Raiz = list(ComplejoRaices.keys())
        Raiz = Raiz[0]
        ComplejoArgumento = (Complejo(1,0) / ComplejoA) + Raiz
        return Complejo(0,-1) * Complejo.logaritmoNatural(ComplejoArgumento)
        


    def graficar(DictComplejos, DictRaices = None):
        fig, graficas = plt.subplots(2, figsize = (10,6))
        fig2, graficaRaices = plt.subplots(1, figsize = (10,6))
        
        graficas[0].set_title("Operaciones con los numeros complejos")
        graficas[1].set_title("Potenciación del primer complejo")
        graficaRaices.set_title("Raíces del número complejo")

        auxX = []
        auxY = []
        auxX2 = []
        auxY2 = []

        for numeroComplejo, leyenda in DictComplejos.items():
            if numeroComplejo != None:
                if leyenda != "Potenciacion":
                    graficas[0].scatter(numeroComplejo.real, numeroComplejo.imaginario, label = leyenda)
                    auxX.append( abs(numeroComplejo.real) )
                    auxY.append( abs(numeroComplejo.imaginario))
                else:
                    graficas[1].scatter(numeroComplejo.real, numeroComplejo.imaginario, label = leyenda)
                    realPotencia = numeroComplejo.real
                    imaginarioPotencia = numeroComplejo.imaginario
                   
        
        for numeroComplejo, leyenda in DictRaices.items():
            if numeroComplejo != None:
                graficaRaices.scatter(numeroComplejo.real, numeroComplejo.imaginario, label = leyenda)
                auxX2.append( abs(numeroComplejo.real))
                auxY2.append( abs(numeroComplejo.imaginario))
             
    
        x = max(auxX)
        y = max(auxY)
        x2= max(auxX2)
        y2 = max(auxY2)

        graficas[0].plot( [-1000000, 1000000], [0, 0],  color = "black" )
        graficas[0].plot( [0, 0], [-1000000, 1000000], color = "black"  )
        graficas[0].axis( (-2*x, 2*x, -2*y, 2*y) )
        graficas[0].legend()

        graficas[1].plot( [-1000000, 1000000], [0, 0], color = "black"  )
        graficas[1].plot( [0, 0], [-1000000, 1000000], color = "black"  )
        graficas[1].axis( (-2*realPotencia, 2*realPotencia, -2*imaginarioPotencia, 2*imaginarioPotencia) )
        graficas[1].legend()
       
        graficaRaices.plot( [-1000000, 1000000], [0, 0], color = "black"  )
        graficaRaices.plot( [0, 0], [-1000000, 1000000], color = "black"  )
        graficaRaices.axis( (-2*x2, 2*x2, -2*y2, 2*y2) )
        graficaRaices.legend()
        

        graficas[0].grid()
        graficas[1].grid()
        graficaRaices.grid()
        plt.show()

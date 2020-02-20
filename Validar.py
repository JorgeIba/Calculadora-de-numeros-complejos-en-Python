from Complejo import *
import re
    
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




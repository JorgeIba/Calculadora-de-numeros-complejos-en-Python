from tkinter import *

class Ventana():

    def __init__(self, title = None):
        self.window = Tk()
        if title != None:
            self.window.title(title)        

    def ocultar(self):
        self.window.withdraw()

    def mostrar(self):
        self.window.update()
        self.window.deiconify()
    


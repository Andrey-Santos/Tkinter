from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()

        self.root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")        
        self.root.configure(background = '#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width = 900, height = 700)   
        self.root.minsize(width = 400, height = 300)   

     

Application()
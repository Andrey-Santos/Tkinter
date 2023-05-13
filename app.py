from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.cria_botoes()
        self.root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")        
        self.root.configure(background = '#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width = 900, height = 700)   
        self.root.minsize(width = 400, height = 300)   

    def frames_da_tela(self):
        self.frame1 = Frame(self.root,bd=4,bg='#dfe3ee',highlightbackground='#759fe6',highlightthickness=3) 
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)       
        self.frame2 = Frame(self.root,bd=4,bg='#dfe3ee',highlightbackground='#759fe6',highlightthickness=3) 
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)       

    def cria_botoes(self):
        ### Criação do botão limpar
        self.bt_limpar = Button(self.frame1, text="Limpar")
        self.bt_limpar.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.15)        

        ### Criação do botão busca
        self.bt_buscar = Button(self.frame1, text="Buscar")
        self.bt_buscar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)        

        ### Criação do botão novo
        self.br_novo = Button(self.frame1, text="Novo")
        self.br_novo.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.15)        

        ### Criação do botão alterar
        self.br_alterar = Button(self.frame1, text="Alterar")
        self.br_alterar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)        

        ### Criação do botão apagar
        self.bt_apagar = Button(self.frame1, text="Apagar")
        self.bt_apagar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)        

Application()
from tkinter import *
janela = Tk()
janela['bg'] = "red"
app = Frame(janela)
app.grid()

from tkinter import*
janela = Tk()
janela["bg"] = "white"
app = Frame(janela)
app.grid()

labelMsg = Label(janela,text="Informe sua idade: " 
            ,font="Times"      
            ,bg="white",foreground="black")
labelMsg.place(x=100,y=50)

entradaDados = Entry(janela,)
entradaDados.place(x=100,y=75)



title="Sistema Tarumã"
janela.title(title)
janela.geometry("800x600")
janela.resizable(False,False)
janela.mainloop()
janela.destroy()
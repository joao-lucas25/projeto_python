import tkinter as tk 
import mysql.connector
#pip install mysql-connector



def conexao():
        try:
                conexao = mysql.connector.connect(
                        host = "localhost",
                        user = "root",
                        passwd = "",
                        db = "usuarios"
                ) 
                print("conectado")
                return conexao
        except mysql.connector.Error as e:
                print(f'Erro ao conectar no Servidor mysql: {e}')
                
       



def cadastrarUsuarios():
    janelaUsuarios = tk.Toplevel(app)
    Nome 
   
   
    
    lblNome = tk.Label(janelaUsuarios,text="Informe o seu nome: " 
            ,font="Times"      
            ,bg="white",foreground="black")
    lblNome.place(x=100,y=50)

    entryNome = tk.Entry(janelaUsuarios)
    entryNome.place(x=230,y=55)
    
    lblSobrenome = tk.Label(janelaUsuarios,text="Informe o seu sobrenome:"
            ,font="Times"
            ,bg="White",foreground="black")
    lblSobrenome.place(x=100, y=75)
    entrySobrenome = tk.Entry(janelaUsuarios)
    entrySobrenome.place(x=260, y=75)
     
    lblDataNascimento = tk.Label(janelaUsuarios,text="Informe a sua data de nascimento:"
            ,font="Times"
            ,bg="White", foreground="black")
    lblDataNascimento.place(x=100, y=90)
    entryDataNascimento = tk.Entry(janelaUsuarios)
    entryDataNascimento.place(x=300, y=100)

    lblCidade = tk.Label(janelaUsuarios,text="Informe sua cidade:"    
            ,font="Times"
            ,bg="White",foreground="black")
    lblCidade.place(x=230, y=125)
    entryCidade = tk.Entry(janelaUsuarios)
    entryCidade.place(x=230, y=125)

    lblEstado = tk.Label(janelaUsuarios, text="Informe o estado: "
             ,font="Times"
             ,bg="White",fireground="black")
    lblEstado.place(x=100,y=150)
    entryEstado = tk.Label(janelaUsuarios)         
    entryEstado.place()

    
    janelaUsuarios.title("Cadastro de Usuários")
    janelaUsuarios.geometry("800x600")
def cadastrarProdutos():
    janelaProduto = tk.Toplevel(app)
    janelaProduto.title("Cadastro de Produtos")
    janelaProduto.geometry("800x600")
app = tk.Tk()

menuPrincipal = tk.Menu(app)
app.config(menu=menuPrincipal)

fileMenu =tk.Menu(menuPrincipal)
fileMenu.add_command(label="Cadastrar Usuários"
            ,command=cadastrarUsuarios)
fileMenu.add_command(label="Cadastrar Produtos"
            ,command=cadastrarProdutos)
menuPrincipal.add_cascade(label="Funcao"
                        ,menu=fileMenu)

#buttonExample
#buttonExample = tk.Button(app,
              #text="Create new window",
              #command=cr)
#buttonExample.place(x=100,y=50)
app.title("Sistema Tarumã")
app.geometry("800x600")
app.mainloop()
app.destroy()             
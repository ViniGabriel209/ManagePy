import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql.cursors
from tkinter.constants import END


# ----- CONEXÃO COM BANCO DE DADOS -----------

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '209213',
    db = 'prototipo',
    charset = 'utf8',
    cursorclass = pymysql.cursors.DictCursor
)

def login():                                               # ----- FUNÇÃO QUE REALIZA CADASTRO NO PROGRAMA
    
    nome = lnome.get()
    cargo = lcargo.get()
    senha = lsenha.get()

    cadastro = False                                       # ----- VARIÁVEL QUE PERMITE O ACESSO DO USUÁRIO

    for linha in funcionarios:
        if nome == linha['nome'] and cargo == linha['cargo'] and senha == linha['senha']:
            cadastro = True
    
    if cadastro == True and cargo == 'Gerente':
        app.destroy()
        import gerente
    
    elif cadastro == True and cargo == 'Caixa':
        app.destroy()
        import caixa

    else:
        messagebox.showerror('Erro', 'Dados de login errados')    
        lnome.delete(0, END)
        lcargo.delete(0, END)
        lsenha.delete(0, END)


# ----- INÍCIO DO PROGRAMA

lista_cargos = ["Gerente", "Caixa"]                        # ----- VALORES DA COMBOBOX

with conexao.cursor() as cursor:                           # ----- LISTA DE FUNCIONÁRIOS PARA SER VERIFICADA PELA FUNÇÃO login
    cursor.execute('select * from funcionarios;')
    funcionarios = cursor.fetchall()

app = tk.Tk()
app.title("ManagePy") 
app.geometry("500x500")
app.configure(background='#ADD8E6')

container0 = tk.Frame(app)
container1 = tk.Frame(app)

container0.pack(side = 'top', pady = 30)
container1.pack(side = 'top', pady = 10)

container0.configure(bg = '#ADD8E6')
container1.configure(bg = '#ADD8E6')

logo = tk.PhotoImage(file = 'logo.png')   

tk.Label(container0, text = '', bg = '#ADD8E6', height = 1).pack(side = 'top')
tk.Label(container0, image = logo, bg = '#ADD8E6', width = 400, height = 100).pack(side = 'top')

linhanome = tk.Frame(container1)
linhacargo = tk.Frame(container1)
linhasenha = tk.Frame(container1)
linhalogin = tk.Frame(container1)

linhanome.pack(side = 'top')
linhacargo.pack(side = 'top')
linhasenha.pack(side = 'top')
linhalogin.pack(side = 'top')

linhanome.configure(bg = '#ADD8E6')
linhacargo.configure(bg = '#ADD8E6')
linhasenha.configure(bg = '#ADD8E6')
linhalogin.configure(bg = '#ADD8E6')

tk.Label(linhanome, text = 'Nome:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
lnome = tk.Entry(linhanome, width = 40)
lnome.pack(side = 'top', pady = 10)

tk.Label(linhacargo, text = 'Cargo:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
lcargo = ttk.Combobox(linhacargo, values = lista_cargos, width = 38)
#lcargo = tk.Entry(linhacargo, width = 40)
lcargo.pack(side = 'top', pady = 10)

tk.Label(linhasenha, text = 'Senha:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
lsenha = tk.Entry(linhasenha, width = 40, show = '*')
lsenha.pack(side = 'top', pady = 10)

login = tk.Button(linhalogin, text = 'LOGIN', bg = '#4682B4', width = 44, command = login)
login.pack(side = 'top', pady = 15)

app.mainloop()

  
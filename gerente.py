import tkinter as tk
from tkinter import Entry, Frame, Label, ttk
from tkinter import *
from tkinter.constants import END
from tkinter import messagebox
from typing import Sized
import pymysql.cursors
from datetime import datetime
from email.message import EmailMessage  
import smtplib

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '209213',
    db = 'prototipo',
    charset = 'utf8',
    cursorclass = pymysql.cursors.DictCursor
)

data = datetime.today().strftime('%Y-%m-%d')
hora = datetime.now().strftime('%H:%M:00')
dia = datetime.today().strftime('%A')

# ============================================ #
# ======== CONSTRUÇÃO GERAL DO FRAME ========= #
# ============================================ #

def atualiza():                                            # ----- FUNÇÃO QUE ATUALIZA A INTERFACE APÓS NOVOS DADOS SEREM INSERIDOS
    app.destroy()
    import gerente_2


def relogio():
    hhora = datetime.now().strftime('%H:%M:%S')
    cabeça.config(text = f'------------ {dia} ------------ {data} ------------ {hhora} ------------')
    cabeça.after(100, relogio) 
    

app = tk.Tk()
app.title("ManagePy")
app.geometry("1200x1200")
app.configure(background="#C0F0E5")

Container0 = tk.Frame(app)
Container1 = tk.Frame(app)

Container0.pack(side = 'top')
Container1.pack(side = 'top')

Container0.configure(bg = 'black')

cabeça = tk.Label(Container0, text = '', bg = 'black', fg = 'white')
cabeça.pack()

abas = ttk.Notebook(Container1)
abas.grid(row = 0, column = 0)

frame0 = Frame(abas)
frame1 = Frame(abas)
frame2 = Frame(abas)
frame3 = Frame(abas)
frame4 = Frame(abas)
frame5 = Frame(abas)
frame6 = Frame(abas)

for frame in (frame0, frame1, frame2, frame3, frame4, frame5, frame6):
    frame.configure(bg = '#ADD8E6')

abas.add(frame0, text = 'CADASTRAR FUNCIONÁRIO')
abas.add(frame1, text = 'VER/PAG FUNCIONÁRIOS')
abas.add(frame2, text = 'CADASTRAR PRODUTO')
abas.add(frame3, text = 'VERIFICAR PRODUTOS')
abas.add(frame4, text = 'CADASTRAR FORNECEDOR')
abas.add(frame5, text = 'FAZER PEDIDO')
abas.add(frame6, text = 'VERIFICAR PEDIDOS')

relogio()                                                  # FUNÇÃO QUE ATUALIZA HORÁRIO

# ============================================ #
# ================ FRAME 0 =================== #
# ============================================ #

def cadastraFuncionario():



    with conexao.cursor() as cursor:
        cursor.execute('select * from funcionarios;')
        funcionarios = cursor.fetchall()   

    nome = lnome.get()
    cpf = lcpf.get()
    cargo = lcargo.get()
    salario = lsal.get()
    telefone = lfone.get()
    email = lmail.get()
    senha = lsenha.get()

    cadastrado = False
    jaCadastrado = False

    for linha in funcionarios:
        if cpf == linha['cpf']:
            jaCadastrado = True
            break

    if jaCadastrado == False:
        with conexao.cursor() as cursor:
            cursor.execute(f'insert into funcionarios values (default, "{nome}", "{cargo}", "{salario}", "{cpf}", "{telefone}", "{email}", "{data}", default, "{senha}");')
            conexao.commit()
        cadastrado = True

    lnome.delete(0, END)
    lcpf.delete(0, END)
    lcargo.delete(0, END)
    lsal.delete(0, END)
    lfone.delete(0, END)
    lmail.delete(0, END)
    lsenha.delete(0, END)

    if cadastrado:
        messagebox.showinfo('Confirmação', 'Funcionário cadastrado!')
    elif jaCadastrado:
        messagebox.showerror('Confirmação', 'Funcionário já cadastrado')
    else:
        messagebox.showerror('Confirmação', 'Erro ao cadastrar!')


container00 = Frame(frame0)
container0 = Frame(frame0)
container1 = Frame(frame0)
container2 = Frame(frame0)

container00.pack(side = 'top')
container2.pack(side = 'bottom')
container0.pack(side = 'left')
container1.pack(side = 'right')

container00.configure(bg = '#ADD8E6')
container0.configure(bg = '#ADD8E6')
container1.configure(bg = '#ADD8E6')
container2.configure(bg = '#ADD8E6')

Label(container00, text = 'Preencha os dados abaixo para cadastrar um novo funcionário', font = ('Verdana', '15'), bg = '#ADD8E6', height = 4).pack()

esquerda = Frame(container0)
direita = Frame(container1)

linhanome = Frame(container0)
linhacpf = Frame(container0)
linhacargo = Frame(container0)
linhasal = Frame(container1)
linhafone = Frame(container1)
linhamail = Frame(container1)
linhasenha = Frame(container2)
linhacadastro = Frame(container2)

esquerda.pack(side = 'left')
direita.pack(side = 'right')

linhanome.pack(side = 'top')
linhacpf.pack(side = 'top')
linhacargo.pack(side = 'top')
linhasal.pack(side = 'top')
linhafone.pack(side = 'top')
linhamail.pack(side = 'top')
linhasenha.pack(side = 'top')
linhacadastro.pack(side = 'top')

esquerda.configure(bg = '#ADD8E6')
direita.configure(bg = '#ADD8E6')

linhanome.configure(bg = '#ADD8E6')
linhacpf.configure(bg = '#ADD8E6')
linhacargo.configure(bg = '#ADD8E6')
linhasal.configure(bg = '#ADD8E6')
linhafone.configure(bg = '#ADD8E6')
linhamail.configure(bg = '#ADD8E6')
linhasenha.configure(bg = '#ADD8E6')
linhacadastro.configure(bg = '#ADD8E6')

Label(esquerda, text = '', bg = '#ADD8E6', width = 8).pack()
Label(direita, text = '', bg = '#ADD8E6', width = 8).pack()

tk.Label(linhanome, text = 'Nome:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhanome, text = '', bg = '#ADD8E6', width = 2).pack(side = 'left')
lnome = tk.Entry(linhanome, width = 40)
lnome.pack(side = 'top', pady = 10)

tk.Label(linhacpf, text = 'CPF:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhacpf, text = '', bg = '#ADD8E6', width = 4).pack(side = 'left')
lcpf = tk.Entry(linhacpf, width = 40)
lcpf.pack(side = 'top', pady = 10)

tk.Label(linhacargo, text = 'Cargo:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhacargo, text = '', bg = '#ADD8E6', width = 2).pack(side = 'left')
lcargo = tk.Entry(linhacargo, width = 40)
lcargo.pack(side = 'top', pady = 10)

tk.Label(linhasal, text = 'Salário:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhasal, text = '', bg = '#ADD8E6', width = 1).pack(side = 'left')
lsal = tk.Entry(linhasal, width = 40)
lsal.pack(side = 'top', pady = 10)

tk.Label(linhafone, text = 'Telefone:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
lfone = tk.Entry(linhafone, width = 40)
lfone.pack(side = 'top', pady = 10)

tk.Label(linhamail, text = 'Email:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhamail, text = '', bg = '#ADD8E6', width = 2).pack(side = 'left')
lmail = tk.Entry(linhamail, width = 40)
lmail.pack(side = 'top', pady = 10)

tk.Label(linhasenha, text = 'Senha:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhasenha, text = '', bg = '#ADD8E6', width = 2).pack(side = 'left')
lsenha = tk.Entry(linhasenha, width = 40)
lsenha.pack(side = 'top', pady = 10)

cadastra = tk.Button(linhacadastro, text = 'CADASTRAR FUNCIONÁRIO', bg = '#4682B4', width = 47, command = cadastraFuncionario)
cadastra.pack(side = 'top', pady = 15)

# ============================================ #
# ================ FRAME 1 =================== #
# ============================================ #

def pagamentos():                                      # ----- FUNÇÃO PARA REALIZAR PAGAMENTO DE FUNCIONARIOS

    """Cadastra na tabela dos funcionários as datas em
    que ocorrem seus pagamentos e atualiza a tabela do
    fluxo de caixa com a subtração do valor dos salários 
    cadastrados"""

    erro = False

    try:                                                  
        with conexao.cursor() as cursor:
            cursor.execute('select * from funcionarios;')
            funcionarios = cursor.fetchall()   
    except:
        erro = True

    listaFuncionario = []                                   # ----- LISTA QUE CONTÉM TODOS OS FUNCIONÁRIOS

    for funcionario in funcionarios:
        listaFuncionario.append(funcionario['nome'])
        listaFuncionario.append(funcionario['salario'])

    n = int(lpag.get())
    nome = listaFuncionario[2*n - 2]
    salario = listaFuncionario[2*n - 1]

    try:
        with conexao.cursor() as cursor:
            cursor.execute(f'insert into fluxo_caixa values (default, "pag {nome}", "{data}", "-{salario}");')
            conexao.commit()
            pago = True
    except:
        erro = True

    p = funcionarios[n - 1]

    if p['hist_pagamento'] == None:
        try:
            with conexao.cursor() as cursor:
                cursor.execute(f'update funcionarios set hist_pagamento = "{data}" where id = "{n}";')
                conexao.commit()
        except:
            Erro = True
    else:
        hist = ''
        hist = p['hist_pagamento'] + ' - ' + data
        try:
            with conexao.cursor() as cursor:
                cursor.execute(f'update funcionarios set hist_pagamento = "{hist}" where id = "{n}";')
                conexao.commit()
        except:
            erro = True

    lpag.delete(0, END)
    
    if pago:
        messagebox.showinfo('Confirmação', 'Pagamento cadastrado!')
    elif erro:
        messagebox.showerror('Confirmação', 'Erro ao cadastrar pagamento')


Label(frame1, text = 'Dados de todos os funcionarios cadastrados', font = ('Verdana', '15'), bg = '#ADD8E6', height = 3).pack()

containerTree = Frame(frame1)
containerTree.configure(bg = '#ADD8E6')
containerTree.pack(ipadx = 0, ipady = 0)

scrollbar_y = Scrollbar(containerTree)
scrollbar_y.pack(side = "right", fill = "y")
scrollbar_x = Scrollbar(containerTree, orient = "horizontal")
scrollbar_x.pack(side = "bottom", fill = "x")

colunay = ttk.Treeview(containerTree, selectmode = "browse",xscrollcommand = scrollbar_x.set, yscrollcommand = scrollbar_y.set, column = ("column 1", "column 2", "column 3", "column 4", "column 5", "column 6","column 7", "column 8", 'column 9'), show ='headings')

colunay.column("column 1", width = 50 , minwidth = 10, stretch = NO)
colunay.heading("#1", text = "ID")

colunay.column("column 2", width = 100 , minwidth = 10, stretch = NO)
colunay.heading("#2", text = "NOME")

colunay.column("column 3", width = 80  , minwidth = 10, stretch = NO)
colunay.heading("#3", text = "CARGO")

colunay.column("column 4", width = 75 , minwidth = 10, stretch = NO)
colunay.heading("#4", text = "SALARIO")

colunay.column("column 5", width = 100 , minwidth = 10, stretch = NO)
colunay.heading("#5", text = "CPF")

colunay.column("column 6", width = 100  , minwidth = 10, stretch = NO)
colunay.heading("#6", text = "TELEFONE")

colunay.column("column 7", width = 150 , minwidth = 10, stretch = NO)
colunay.heading("#7", text = "E-MAIL")

colunay.column("column 8", width = 100  , minwidth = 10, stretch = NO)
colunay.heading("#8", text = "ADMISSÃO")

colunay.column("column 9", width = 140  , minwidth = 10, stretch = NO)
colunay.heading("#9", text = "PAGAMENTOS")

with conexao.cursor() as cursor:
    cursor.execute('select * from funcionarios;')
    funcionario = cursor.fetchall()   

for linhas in funcionario:
    colunay.insert("", "end", values = (linhas["id"],linhas["nome"],linhas["cargo"],linhas["salario"],linhas["cpf"],linhas["telefone"],linhas["email"],linhas["admissao"],linhas["hist_pagamento"]))

colunay.pack(padx = 30, pady = 5)

scrollbar_y.configure(command = colunay.yview)
scrollbar_x.configure(command = colunay.xview)

Label(frame1, text = 'Se desejar cadastrar pagamento, digite o ID no campo abaixo:', font = ('Verdana', '15'), bg = '#ADD8E6', height = 3).pack()

container0 = Frame(frame1)
container1 = Frame(frame1)

container1.pack(side = 'bottom')
container0.pack(side = 'bottom')

container0.configure(bg = '#ADD8E6')
container1.configure(bg = '#ADD8E6')

Label(container0, text = 'ID:', bg = '#ADD8E6').pack(side = 'left')
lpag = Entry(container0, width = 10)
Label(container0, text = '', bg = '#ADD8E6', width = 1).pack(side = 'left')
lpag.pack(side = 'left')

Label(container0, text = '', bg = '#ADD8E6', width = 2).pack(side = 'left')
Button(container0, text = 'ATUALIZAR', bg = '#4682B4', command = atualiza).pack(side = 'right')

Label(container0, text = '', bg = '#ADD8E6', width = 20).pack(side = 'right')
Button(container0, text = 'CADASTRAR PAGAMENTO', bg = '#4682B4', command = pagamentos).pack(side = 'right')

Label(container1, text = '', bg = '#ADD8E6', height = 1).pack(side = 'bottom')


# ============================================ #
# ================ FRAME 2 =================== #
# ============================================ #


def cadastraProduto():                                     # ----- FUNÇÃO PARA CADASTRAR PRODUTO

    """Cadastra os produtos que ainda não existem no estoque e
    que serão vendidos pelo estabelecimento. Após o primeiro pedido
    feito que traz determinado produto para o estoque, este já pode
    ser vendido pelos caixas"""

    with conexao.cursor() as cursor:
        cursor.execute('select * from produto;')
        produtos = cursor.fetchall()

    nome = pnome.get()
    codigo = pcod.get()
    custo = float(pcusto.get())
    preço = float(ppreço.get())
    lucro = preço - custo

    jaCadastrado = False
    cadastrado = False

    for linha in produtos:
        if codigo == linha['codigo']:
            jaCadastrado = True
            print('Código de produto já em uso')
            break
    if jaCadastrado == False:
        try:                                               
            with conexao.cursor() as cursor:
                cursor.execute(f'insert into produto values (default, "{nome}", "{codigo}","{custo}", "{preço}", "{lucro}", "0");')
                conexao.commit()
            cadastrado = True
        except:
            cadastrado = False
    
    pnome.delete(0, END)
    pcod.delete(0, END)
    pcusto.delete(0, END)
    ppreço.delete(0, END)

    if cadastrado:
        messagebox.showinfo('Confirmação', 'Produto cadastrado!')
    elif jaCadastrado:
        messagebox.showerror('Confirmação', 'Produto já cadastrado')
    else:
        messagebox.showerror('Confirmação', 'Erro ao cadastrar!')
        

container00 = Frame(frame2)
container0 = Frame(frame2)
container1 = Frame(frame2)
container2 = Frame(frame2)

container00.pack(side = 'top')
container2.pack(side = 'bottom')
container0.pack(side = 'left')
container1.pack(side = 'right')

container00.configure(bg = '#ADD8E6')
container0.configure(bg = '#ADD8E6')
container1.configure(bg = '#ADD8E6')
container2.configure(bg = '#ADD8E6')

Label(container00, text = 'Preencha os dados abaixo para cadastrar um novo produto', font = ('Verdana', '15'), bg = '#ADD8E6', height = 4).pack()

esquerda = Frame(container0)
direita = Frame(container1)

linhanome = Frame(container0)
linhacod = Frame(container0)
linhacusto = Frame(container1)
linhapreço = Frame(container1)
linhacadastra = Frame(container2)

esquerda.pack(side = 'left')
direita.pack(side = 'right')

linhanome.pack()
linhacod.pack()
linhacusto.pack()
linhapreço.pack()
linhacadastra.pack()

esquerda.configure(bg = '#ADD8E6')
direita.configure(bg = '#ADD8E6')

linhanome.configure(bg = '#ADD8E6')
linhacod.configure(bg = '#ADD8E6')
linhacusto.configure(bg = '#ADD8E6')
linhapreço.configure(bg = '#ADD8E6')
linhacadastra.configure(bg = '#ADD8E6')

Label(esquerda, text = '', bg = '#ADD8E6', width = 8).pack()
Label(direita, text = '', bg = '#ADD8E6', width = 8).pack()

tk.Label(linhanome, text = 'Nome:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhanome, text = '', bg = '#ADD8E6', width = 2).pack(side = 'left')
pnome = tk.Entry(linhanome, width = 40)
pnome.pack(side = 'top', pady = 10)

tk.Label(linhacod, text = 'Código:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhacod, text = '', bg = '#ADD8E6', width = 1).pack(side = 'left')
pcod = tk.Entry(linhacod, width = 40)
pcod.pack(side = 'top', pady = 10)

tk.Label(linhacusto, text = 'Custo:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhacusto, text = '', bg = '#ADD8E6', width = 1).pack(side = 'left')
pcusto = tk.Entry(linhacusto, width = 40)
pcusto.pack(side = 'top', pady = 10)

tk.Label(linhapreço, text = 'Preço:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhapreço, text = '', bg = '#ADD8E6', width = 1).pack(side = 'left')
ppreço = tk.Entry(linhapreço, width = 40)
ppreço.pack(side = 'top', pady = 10)

pcadastra = tk.Button(linhacadastra, text = 'CADASTRAR PRODUTO', bg = '#4682B4', width = 47, command = cadastraProduto)
pcadastra.pack(side = 'top', pady = 15)
Label(linhacadastra, text = '', bg = '#ADD8E6', height = 2).pack()

# ============================================ #
# ================ FRAME 3 =================== #
# ============================================ #

Label(frame3, text = 'Dados de todos os produtos cadastrados', font = ('Verdana', '15'), bg = '#ADD8E6', height = 4).pack()

colunac = ttk.Treeview(frame3, selectmode = "browse", column = ("column 1", "column 2", "column 3", "column 4", "column 5", "column 6","column 7"), show ='headings')

colunac.column("column 1", width = 50 , minwidth = 100, stretch = NO)
colunac.heading("#1", text = "ID")

colunac.column("column 2", width = 150 , minwidth = 100, stretch = NO)
colunac.heading("#2", text = "PRODUTOS")

colunac.column("column 3", width = 100  , minwidth = 100, stretch = NO)
colunac.heading("#3", text = "CODIGO")

colunac.column("column 4", width = 75 , minwidth = 100, stretch = NO)
colunac.heading("#4", text = "CUSTO")

colunac.column("column 5", width = 150 , minwidth = 100, stretch = NO)
colunac.heading("#5", text = "PREÇO DE VENDA")

colunac.column("column 6", width = 100  , minwidth = 100, stretch = NO)
colunac.heading("#6", text = "LUCRO")

colunac.column("column 7", width = 75 , minwidth = 100, stretch = NO)
colunac.heading("#7", text = "ESTOQUE")

with conexao.cursor() as cursor:                        # ----- LISTA DE PRODUTOS ATUALIZADA
    cursor.execute('select * from produto;')
    produto = cursor.fetchall()   

for linhas in produto:
     colunac.insert("", "end", values = (linhas["id"],linhas["nome"],linhas["codigo"],linhas["custo"],linhas["preço"],linhas["lucro"],linhas["estoque"]))

colunac.pack(padx = 30, pady = 25)

Label(frame3, text = '', bg = '#ADD8E6', height = 1).pack()

Button(frame3, text = 'ATUALIZAR', bg = '#4682B4', command = atualiza).pack()

# ============================================ #
# ================ FRAME 4 =================== #
# ============================================ #


def cadastraFornecedor():

    """Função para cadastrar fornecedor ao banco de 
    dados para que seja utilizado em algum pedido"""

    with conexao.cursor() as cursor:
        cursor.execute('select * from fornecedores;')
        fornecedores = cursor.fetchall()

    nome = fnome.get()
    endereco = fend.get()
    cnpj = fcnpj.get()
    email = femail.get()

    jaCadastrado = False

    for linha in fornecedores:
        if cnpj == linha['cnpj']:
            jaCadastrado = True
            break
        
    if jaCadastrado == False:
        try:
            with conexao.cursor() as cursor:
                cursor.execute(f'insert into fornecedores values (default, "{nome}", "{endereco}", "{cnpj}", "{email}");')
                conexao.commit()
            cadastrado = True
        except:
            cadastrado = False 

    fnome.delete(0, END)
    fcnpj.delete(0, END)
    fend.delete(0, END)
    femail.delete(0, END)

    if cadastrado:
        messagebox.showinfo('Confirmação', 'Fornecedor cadastrado!')
    elif jaCadastrado:
        messagebox.showerror('Confirmação', 'Fornecedor já cadastrado')
    

container0 = Frame(frame4)
container1 = Frame(frame4)

container0.pack(side = 'left')
container1.pack(side = 'left')

container0.configure(bg = '#ADD8E6')
container1.configure(bg = '#ADD8E6')

linhanome = Frame(container0)
linhacnpj = Frame(container0)
linhaend = Frame(container0)
linhaemail = Frame(container0)
linhacadastra = Frame(container0)

esquerda = Frame(container0)
direita = Frame(container0)

esquerda.pack(side = 'left')
direita.pack(side = 'right')

Label(esquerda, text = '', bg = '#ADD8E6', width = 5).pack()
Label(direita, text = '', bg = '#ADD8E6', width = 4).pack()

Label(container0, text = 'Preencha os dados para\ncadastrar novo fornecedor', font = ('Verdana', '15'), bg = '#ADD8E6', height = 3).pack()
Label(container1, text = 'Dados dos fornecedores já cadastrados', font = ('Verdana', '15'), bg = '#ADD8E6', height = 3).pack()

linhanome.pack()
linhacnpj.pack()
linhaend.pack()
linhaemail.pack()
linhacadastra.pack()

linhanome.configure(bg = '#ADD8E6')
linhacnpj.configure(bg = '#ADD8E6')
linhaend.configure(bg = '#ADD8E6')
linhaemail.configure(bg = '#ADD8E6')
linhacadastra.configure(bg = '#ADD8E6')

container10 = Frame(container1)
container10.pack(side = 'bottom')
container10.configure(bg = '#ADD8E6')

Button(container10, text = 'ATUALIZAR', bg = '#4682B4', command = atualiza).pack(pady = 20)

scrollbar_y = Scrollbar(container1)
scrollbar_y.pack(side = "right", fill = "y")
scrollbar_x = Scrollbar(container1, orient = "horizontal")
scrollbar_x.pack(side = "bottom", fill = "x")

colunaa = ttk.Treeview(container1, selectmode = "browse", xscrollcommand = scrollbar_x.set, yscrollcommand = scrollbar_y.set, column = ("column 1", "column 2", "column 3", "column 4", "column 5"), show ='headings')

colunaa.column("column 1", width = 40, minwidth = 10, stretch = NO)
colunaa.heading("#1", text = "ID")

colunaa.column("column 2", width = 100, minwidth = 10, stretch = NO)
colunaa.heading("#2", text = "Nome")

colunaa.column("column 3", width = 150, minwidth = 10, stretch = NO)
colunaa.heading("#3", text = "Endereço")

colunaa.column("column 4", width = 70 , minwidth = 10, stretch = NO)
colunaa.heading("#4", text = "cnpj")

colunaa.column("column 5", width = 150 , minwidth = 10, stretch = NO)
colunaa.heading("#5", text = "email")

with conexao.cursor() as cursor:
    cursor.execute('select * from fornecedores;')
    fornecedores = cursor.fetchall() 

for linhas in fornecedores:
     colunaa.insert("", "end", values = (linhas["id"],linhas["nome"],linhas["endereço"],linhas["cnpj"],linhas["email"]))

colunaa.pack(padx = 30, pady = 5)

scrollbar_y.configure(command = colunaa.yview)
scrollbar_x.configure(command = colunaa.xview)

tk.Label(linhanome, text = 'Nome:   ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhanome, text = '', bg = '#ADD8E6', width = 2).pack(side = 'left')
fnome = tk.Entry(linhanome, width = 40)
fnome.pack(side = 'top', pady = 10)

tk.Label(linhacnpj, text = 'CNPJ:   ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhacnpj, text = '', bg = '#ADD8E6', width = 3).pack(side = 'left')
fcnpj = tk.Entry(linhacnpj, width = 40)
fcnpj.pack(side = 'top', pady = 10)

tk.Label(linhaend, text = 'Endereço:', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhaend, text = '', bg = '#ADD8E6', width = 1).pack(side = 'left')
fend = tk.Entry(linhaend, width = 40)
fend.pack(side = 'top', pady = 10)

tk.Label(linhaemail, text = 'Email:', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhaemail, text = '', bg = '#ADD8E6', width = 4).pack(side = 'left')
femail = tk.Entry(linhaemail, width = 40)
femail.pack(side = 'top', pady = 10)

fcadastra = tk.Button(linhacadastra, text = 'CADASTRAR FORNECEDOR', bg = '#4682B4', width = 48, command = cadastraFornecedor)
fcadastra.pack(side = 'top', pady = 15)
Label(linhacadastra, text = '', bg = '#ADD8E6', height = 2).pack()

# ============================================ #
# ================ FRAME 5 =================== #
# ============================================ #

def fazPedido():                                      # ----- FUNÇÃO PARA PEDIR PRODUTOS PARA ESTOQUE

    with conexao.cursor() as cursor:
        cursor.execute('select * from fornecedores;')
        fornecedores = cursor.fetchall()

    # ----- PARA CADA PRODUTO A SER PEDIDO, É NECESSÁRIO ESTE ESTAR PREVIAMENTE CADASTRADO

    meu_email = 'empresa.python@gmail.com'                 # ----- DADOS DO EMAILL CRIADO PARA O PROJETO
    senha = 'trabalhodepython'

    nome = pnome.get()
    cnpj = pcnpj.get()
    cod = lista_codigo.get(0,END)
    cod = list(cod)
    quant = lista_quantidade.get(0,END)
    quant = list(quant)

    for linha in fornecedores:                             # CHECA SE O FORNECEDOR JÁ ESTÁ CADASTRADO
        if cnpj == linha['cnpj'] and nome == linha['nome']:
            with conexao.cursor() as cursor:
                cursor.execute(f'select email from fornecedores where cnpj = "{cnpj}";')
                emailLista = cursor.fetchall()
                for dado in emailLista:
                    email = dado['email']
            break

    pedido = []
    add_pedido = []                                        # LISTA DE LISTAS A SER ADICIONADA NA TABELA PEDIDOS NO BdD (é necessário que o conteúdo da lista sejam listas)
    pega_pedido = []                                       # LISTA A SER ADICIONADA NA LISTA ACIMA

    total = 0

    for i in range(len(cod)):
        codigo = cod[i]
        codigo = int(codigo)
        quantidade = quant[i]                      
        quantidade = int(quantidade)

        with conexao.cursor() as cursor:
              cursor.execute(f'select nome, custo, estoque from produto where codigo = "{codigo}";')
              nota = cursor.fetchone()                     # GERA UM DICIONÁRIO, DIFERENTE DO fetchall, QUE GERA UMA LISta
              pedido.append(nota)

        pega_pedido.append(nota['nome'])
        pega_pedido.append(nota['custo'])
        pega_pedido.append(quantidade)
        add_pedido.append(pega_pedido)
        valor = float(pega_pedido[1] * pega_pedido[2])
        total = valor + total
        pega_pedido = []                                   # LIMPA A LISTA PARA SER ADICIONADA NOVAMENTE DEPOIS

    mensagem = ''

    for c in add_pedido:
        mensagem = f'{mensagem} \n' + f'{c[0]} -- {c[1]} -- x{c[2]}'     # CONTEÚDO DO EMAIL

    msg = EmailMessage()                                   # PARÂMETROS DE ENVIO DO EMAIL PARA FORNECEDOR
    msg['Subject'] = 'Pedido de compra'
    msg['From'] = meu_email
    msg['To'] = email
    msg.set_content(f'Prezado, \nEm nome do Supermercado Genérico, venho solicitar a compra dos seguintes itens: \n{mensagem} \nValor total: R${total:.2f} \nAtenciosamente.')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # ENVIA EMAIL
        smtp.login(meu_email, senha)
        smtp.send_message(msg)

    try:                                                   # ADICIONA PEDIDO AO BdD
        with conexao.cursor() as cursor:
            cursor.execute(f'insert into pedidos (id, pedido, data_emissão, valor) values (default, "{add_pedido}", "{data}", "{total:.2f}");')
            conexao.commit()
    except Exception as e:
        print(f'Erro: {e}') 

    messagebox.showinfo('Confirmação', 'Pedido realizado!')

    for i in colunad.get_children():
        colunad.delete(i)
    app.update()

    lista_codigo.delete(0, END)
    lista_quantidade.delete(0, END)


def inserir():

    try:                                                   # ----- LISTA DE PRODUTOS CADASTRADOS
        with conexao.cursor() as cursor:
            cursor.execute('select * from produto;')
            produtos = cursor.fetchall()
    except:
        print('Erro ao conectar ao banco de dados dos clientes')

    codigo = int(pcod.get())
    quantidade = int(puni.get())

    cadastrado = False

    for linha in produtos:
        if codigo == linha['codigo']:
            nome = linha['nome']
            custo = linha['custo']
            cadastrado = True
            break
        
    if cadastrado:
        colunad.insert("", "end", values = (codigo, nome, custo, quantidade))
        lista_codigo.insert(END, codigo)
        lista_quantidade.insert(END, quantidade )
    else:
        messagebox.showerror('Erro', 'Código inválido')

    pcod.delete(0, END)
    puni.delete(0, END)

    
lista_codigo = Listbox(app)            # ----- LISTBOX INVISIVEL COM OS CODIGOS DOS PRODUTOS
lista_quantidade = Listbox(app)        # ----- LISTBOX INVISIVEL COM AS QUANTIDADES DOS PRODUTOS

container000 = Frame(frame5)
container0 = Frame(frame5)
container1 = Frame(frame5)
container00 = Frame(container0)
container01 = Frame(container0)

container000.pack(side = 'top')
container0.pack(side = 'left', padx = 100)
container1.pack(side = 'right')
container00.pack()
container01.pack()

container000.configure(bg = '#ADD8E6')
container0.configure(bg = '#ADD8E6')
container1.configure(bg = '#ADD8E6')
container00.configure(bg = '#ADD8E6')
container01.configure(bg = '#ADD8E6')

linhanome = Frame(container00)
linhacnpj = Frame(container00)
linhacod = Frame(container01)
linhauni = Frame(container01)
linhacad = Frame(container01)

linhanome.pack()
linhacnpj.pack()
linhacod.pack()
linhauni.pack()
linhacad.pack()

linhanome.configure(bg = '#ADD8E6')
linhacnpj.configure(bg = '#ADD8E6')
linhacod.configure(bg = '#ADD8E6')
linhauni.configure(bg = '#ADD8E6')
linhacad.configure(bg = '#ADD8E6')

Label(container000, text = 'Insira os dados a seguir para realizar compra (Nome e CNPJ do fornecedor)', font = ('Verdana', '15'), bg = '#ADD8E6', height = 4).pack()

tk.Label(linhanome, text = 'Nome:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhanome, text = '', bg = '#ADD8E6', width = 2).pack(side = 'left')
pnome = tk.Entry(linhanome, width = 25)
pnome.pack(side = 'top', pady = 10)

tk.Label(linhacnpj, text = 'CNPJ:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhacnpj, text = '', bg = '#ADD8E6', width = 3).pack(side = 'left')
pcnpj = tk.Entry(linhacnpj, width = 25)
pcnpj.pack(side = 'top', pady = 10)

tk.Label(linhacod, text = 'Código:   ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
tk.Label(linhacod, text = '', bg = '#ADD8E6', width = 1).pack(side = 'left')
pcod = tk.Entry(linhacod, width = 25)
pcod.pack(side = 'top', pady = 10)

tk.Label(linhauni, text = 'Unidades:  ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
puni = tk.Entry(linhauni, width = 25)
puni.pack(side = 'top', pady = 10)

Label(linhacad, text = '', bg = '#ADD8E6', width = 16).pack(side = 'left')
pcad = tk.Button(linhacad, text = 'INSERIR', bg = '#2E8B57', width = 15, command = inserir)
pcad.pack(side = 'right', pady = 15)

Label(container1, text = '', bg = '#ADD8E6', width = 15).pack(side = 'right')

colunad = ttk.Treeview(container1, selectmode = "browse", column = ("column 1", "column 2", "column 3", "column 4"), show ='headings')

colunad.column("column 1", width = 100 , minwidth = 100, stretch = NO)
colunad.heading("#1", text = "Código")

colunad.column("column 2", width = 120 , minwidth = 100, stretch = NO)
colunad.heading("#2", text = "Nome")

colunad.column("column 3", width = 100  , minwidth = 100, stretch = NO)
colunad.heading("#3", text = "Custo")

colunad.column("column 4", width = 100  , minwidth = 100, stretch = NO)
colunad.heading("#4", text = "Quantidade")

colunad.pack()

pfin = Button(container1, text = 'FINALIZAR PEDIDO', bg = '#4682B4', width = 20, command = fazPedido)
pfin.pack(side = 'bottom', pady = 15)

# ============================================ #
# ================ FRAME 6 =================== #
# ============================================ #

def atualizaPedido():                                 # ----- FUNÇÃO PARA DAR BAIXA NOS PEDIDOS E ATUALIZAR ESTOQUE

    listaPedidoString = []                                 # LISTA QUE POSSUI TODOS OS PEDIDOS (strings)
    listaPedidoLista = []                                  # LISTA QUE POSSUI PEDIDOS (lista)
    listaPedido = []                                       # LISTA QUE POSSUI PEDIDOS INDIVIDUALMENTE 
    listaPedidoMenor = []                                  # CONTÉM PRODUTOS INDIVIDUAIS PARA ATUALIZAR ESTOQUE

    for pedidoMaximo in pedidos:
        listaPedidoString.append(pedidoMaximo['pedido'])

    for pedido in listaPedidoString:                       # TRANSFORMA OS ELEMENTOS DA LISTA MÁXIMA (strings) EM LISTA ATRAVÉS DO eval()
        pedidon = eval(pedido)
        listaPedidoLista.append(pedidon)

    n = int(pped.get())

    if n in range(1, len(listaPedidoString) + 1):

        with conexao.cursor() as cursor:
            cursor.execute(f'select data_entregue from pedidos where id = "{n}"')
            entregue = cursor.fetchone()

        if entregue['data_entregue'] == None:                  # ----- IMPEDE QUE O MESMO PEDIDO SEJA ENTREGUE + DE UMA VEZ

            with conexao.cursor() as cursor:
                cursor.execute(f'UPDATE pedidos SET data_entregue = "{data}" WHERE id = "{n}";')
                conexao.commit()

            with conexao.cursor() as cursor:                   # ----- LISTA DE PEDIDOS ATUALIZADA 
                cursor.execute('select * from pedidos;')       #
                pedidu = cursor.fetchall()                     #

            # ----- ATUALIZAR ESTOQUE

            for situação in pedidu:                                

                if situação['data_entregue'] != None and situação['id'] == n:  
                    num = int(situação['id'] - 1)
                    listaPedido.append(listaPedidoLista[num])
                    for produtin in listaPedido:
                        for unidade in produtin:
                            with conexao.cursor() as cursor:
                                cursor.execute(f'select estoque from produto where nome = "{unidade[0]}";')
                                meuproduto = cursor.fetchone()

                            listaPedidoMenor.append(unidade[0])
                            listaPedidoMenor.append(int(meuproduto['estoque']))
                            listaPedidoMenor.append(int(unidade[2]))

                            with conexao.cursor() as cursor:
                                cursor.execute(f'update produto set estoque = "{listaPedidoMenor[1] + listaPedidoMenor[2]}" where nome = "{listaPedidoMenor[0]}";')
                                conexao.commit()

                            listaPedidoMenor = []                  # REINICIA LISTA
                            
                    listaPedido = []                               # REINICIA LISTA

            # ----- ATUALIZAR FLUXO DE CAIXA

            with conexao.cursor() as cursor:                        
                cursor.execute(f"select valor from pedidos where id = '{n}';")
                valor = cursor.fetchone()                  # GERA UM DICIONÁRIO, DIFERENTE DO fetchall, QUE GERA UMA LISTA
                    
            with conexao.cursor() as cursor:
                cursor.execute(f"insert into fluxo_caixa values (default, 'pagamento de pedido {n}', '{data}', '-{valor['valor']}');")
                conexao.commit()

            messagebox.showinfo('Confirmação', f'Atestada a entrega do pedido n° {n}')

        else:
            messagebox.showerror('Erro', 'Pedido entregue anteriormente')    

    else:
        messagebox.showerror('Erro', 'ID inválido')

    pped.delete(0, END)


Label(frame6, text = 'Dados de todos os pedidos realizados', font = ('Verdana', '15'), bg = '#ADD8E6', height = 3).pack()

containerTree = Frame(frame6)
containerTree.configure(bg = '#ADD8E6')
containerTree.pack(ipadx = 0, ipady = 0)

scrollbar_y = Scrollbar(containerTree)
scrollbar_y.pack(side = "right", fill = "y")
scrollbar_x = Scrollbar(containerTree, orient = "horizontal")
scrollbar_x.pack(side = "bottom", fill = "x")

colunap = ttk.Treeview(containerTree, selectmode = "browse",xscrollcommand = scrollbar_x.set, yscrollcommand = scrollbar_y.set, column = ("column 1", "column 2", "column 3", "column 4", "column 5"), show ='headings')

colunap.column("column 1", width = 40 , minwidth = 10, stretch = NO)
colunap.heading("#1", text = "ID")

colunap.column("column 2", width = 600 , minwidth = 10, stretch = NO)
colunap.heading("#2", text = "PEDIDO")

colunap.column("column 3", width = 130  , minwidth = 10, stretch = NO)
colunap.heading("#3", text = "DATA EMISSÃO")

colunap.column("column 4", width = 130 , minwidth = 10, stretch = NO)
colunap.heading("#4", text = "DATA ENTREGA")

colunap.column("column 5", width = 100 , minwidth = 10, stretch = NO)
colunap.heading("#5", text = "VALOR")

with conexao.cursor() as cursor:
    cursor.execute('select * from pedidos;')
    pedidos = cursor.fetchall() 

for linhas in pedidos:
     colunap.insert("", "end", values = (linhas["id"],linhas["pedido"],linhas["data_emissão"],linhas["data_entregue"],linhas["valor"]))

colunap.pack(padx = 30, pady = 5)

scrollbar_y.configure(command = colunap.yview)
scrollbar_x.configure(command = colunap.xview)

Label(frame6, text = 'Se desejar dar baixa em pedido, digite o ID no campo abaixo:', font = ('Verdana', '15'), bg = '#ADD8E6', height = 3).pack()

container0 = Frame(frame6)
container1 = Frame(frame6)

container1.pack(side = 'bottom')
container0.pack(side = 'bottom')

container0.configure(bg = '#ADD8E6')
container1.configure(bg = '#ADD8E6')

Label(container0, text = 'ID:', bg = '#ADD8E6').pack(side = 'left')
pped = Entry(container0, width = 10)
Label(container0, text = '', bg = '#ADD8E6', width = 1).pack(side = 'left')
pped.pack(side = 'left')

Label(container0, text = '', bg = '#ADD8E6', width = 2).pack(side = 'left')
Button(container0, text = 'DAR BAIXA', bg = '#4682B4', command = atualizaPedido).pack(side = 'left')
Label(container0, text = '', bg = '#ADD8E6', width = 28).pack(side = 'left')

Button(container0, text = 'ATUALIZAR', bg = '#4682B4', command = atualiza).pack(side = 'right')
Label(container1, text = '', bg = '#ADD8E6', height = 1).pack(side = 'bottom')

# ----- FIM DOS FRAMES

app.mainloop()

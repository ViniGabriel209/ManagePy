from tkinter import*
from tkinter import ttk
import pymysql.cursors
from datetime import datetime
from tkinter import messagebox


# ----- CONEXÃO COM BANCO DE DADOS -----------

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '209213',
    db = 'prototipo',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

data = datetime.today().strftime('%Y-%m-%d')
hora = datetime.now().strftime('%H:%M:00')
dia = datetime.today().strftime('%A')

# ----------------- FUNÇÕES ---------------------------

def salvaDados():                                          # ----- SALVA  OS DADOS IMPORTANTES QUE SÃO INSERIDOS NA INTERFACE ALÉM DE INSERIR OS DAODS NA TABELA
    
    cadastrado = False                                     # ----- VARIÁVEL QUE VERIFICA SE O CÓDIGO DO PRODUTO É CORRETO

    valor_produto = 0
    codigo = int(pcod.get())
    quantidade = int(pquant.get())

    for linha in produtos:
        if codigo == linha['codigo']:
            nome = linha['nome']
            preco = float(linha['preço'])
            valor_produto = valor_produto + preco * quantidade
            coluna.insert("", "end", values = (codigo, nome, preco, quantidade))
            lista_codigo.insert(END, codigo)
            lista_quantidade.insert(END, quantidade)
            cadastrado = True
            break

    if cadastrado == False:
        messagebox.showerror('Erro', 'Código inválido')

    lista_valor_produtos.insert(END, valor_produto )   

    pcod.delete(0, END)
    pquant.delete(0, END)


def mostraTotal():                                         # ----- CALCULA O VALOR TOTAL DA COMPRA
    
    valor_total = 0
    a = lista_valor_produtos.get(0, END)
    a = list(a)

    global total

    for i in range(len(a)):
        valor = a[i]
        valor_total = valor_total + valor

    lista_valor_total.insert(END, valor_total)
    total = lista_valor_total.get(END)
    listaTotalDoDia.append(total)                          # ----- ADICIONA VALOR DA COMPRA À LISTA QUE TEM O VALOR TOTAL DE VENDA DO EXPEDIENTE
    ltot.configure(text = f'Total (R$):  {total:.2f}')

    lista_valor_produtos.delete(0, END)                    # ----- REINICIA O VALOR DA LISTA PARA A PRÓXIMA COMPRA  


def mostraTroco():                                         # ----- CALCULA O TROCO
    
    a = float(lista_valor_total.get(END))
    pag = float(ppag.get())
    troco = pag - a
    if pag < total:                                        # ----- IMPEDE QUE O PAGAMENTO SEJA MENOR QUE O VALOR TOTAL DA COMPRA
        messagebox.showerror('Erro', 'Troco menor')
    else:
        ltro.configure(text = f'Troco (R$):  {troco:.2f}')


def atualizaEstoque():                                     # ----- ATUALIZA O ESTOQUE CONFORME A COMPRA É FINALIZADA
    a = lista_quantidade.get(0,END)
    a = list(a)
    b = lista_codigo.get(0,END)                            
    b = list(b)

    for linha in produtos:
        for i in range(len(a)):
            if b[i] == linha['codigo']:
                with conexao.cursor() as cursor:
                    cursor.execute(f"update produto set estoque = \'{linha['estoque'] - a[i]}\' where codigo = \'{b[i]}\'")
                    conexao.commit()

    ppag.delete(0, END)
    messagebox.showinfo('Confirmação', 'Compra realizada!')

    for i in coluna.get_children():
        coluna.delete(i)
    app.update()

    ltot.configure(text = 'Total (R$):  ')
    ltro.configure(text = 'Troco (R$):  ')

    with conexao.cursor() as cursor:
        cursor.execute(f"insert into horario_compra values (default, '{data}', '{dia}', '{hora}', '{total}');")
        conexao.commit()


def finExpediente():

    totalDia = sum(listaTotalDoDia)                        # ----- VARIÁVEL QUE CONTÉM A SOMA DE TODAS AS COMPRAS REALIZADAS NO EXPEDIENTE

    with conexao.cursor() as cursor:
        cursor.execute(f'insert into fluxo_caixa values (default, "Dia de vendas", "{data}", "{totalDia}")')
        conexao.commit()

    messagebox.showinfo('Confirmação', 'Expediente finalizado')

    app.destroy()


listaTotalDoDia = []                                      # ----- LISTA QUE CONTERÁ O VALOR DE CADA COMPRA REALIZADA

# ----- CONSTRUÇÃO DO FRAME

def relogio():
    hhora = datetime.now().strftime('%H:%M:%S')
    cabeça.config(text = f'------ Vinicius Gabriel ------ {dia} ------ {data} ------ {hhora} ------')
    cabeça.after(100, relogio)


#listaTotalDoDia = []
#totalDia = sum(listaTotalDoDia)

with conexao.cursor() as cursor:
    cursor.execute('select * from produto;')
    produtos = cursor.fetchall()

app = Tk()
app.title("ManagePy") 
app.geometry("1200x1200")
app.configure(background='#ADD8E6')

container0 = Frame(app)
container1 = Frame(app)
container2 = Frame(app)
container3 = Frame(app)

container0.pack(side = 'top')
container3.pack(side = 'bottom')
container1.pack(side = 'left')
container2.pack(side = 'right')

container0.configure(bg = '#ADD8E6')
container1.configure(bg = '#ADD8E6')
container2.configure(bg = '#ADD8E6')
container3.configure(bg = '#ADD8E6')

cabeça = Label(container0, text = '', bg = 'black', fg = 'white')
cabeça.pack()

relogio()

# ------------------- CRIANDO A LISTBOX INVISIVEL COM OS CODIGOS DOS PRODUTOS -------------------

lista_codigo = Listbox(app)

# ------------------- CRIANDO A LISTBOX INVISIVEL COM AS QUANTIDADES DOS PRODUTOS ---------------

lista_quantidade = Listbox(app)

# ------------------- CRIANDO A LISTBOX INVISIVEL COM OS VALORES PARCIAIS DOS PRODUTOS ----------

lista_valor_produtos = Listbox(app)

 #------------------- CRIANDO A LISTBOX INVISIVEL COM OS VALORES TOTAIS DOS PRODUTOS ------------

lista_valor_total = Listbox(app)

# -------------------------
# ----- WIDGETS DA ESQUERDA

esquerda = Frame(container1)
linhacod = Frame(container1)
linhaquant = Frame(container1)
linhainsere = Frame(container1)

esquerda.pack(side = 'left')
linhacod.pack()
linhaquant.pack()
linhainsere.pack()

esquerda.configure(bg = '#ADD8E6')
linhacod.configure(bg = '#ADD8E6')
linhaquant.configure(bg = '#ADD8E6')
linhainsere.configure(bg = '#ADD8E6')

Label(esquerda, text = '', bg = '#ADD8E6', width = 20).pack()

Label(linhacod, text = '', bg = '#ADD8E6', height = 2).pack()
Label(linhacod, text = 'Código:', bg = '#ADD8E6').pack(side = 'left', pady = 10)
Label(linhacod, text = '', bg = '#ADD8E6', width = 5).pack(side = 'left')
pcod = Entry(linhacod, width = 10)
pcod.pack(side = 'top', pady = 10)

Label(linhaquant, text = 'Quantidade: ', bg = '#ADD8E6').pack(side = 'left', pady = 10)
Label(linhaquant, text = '', bg = '#ADD8E6', width = 1).pack(side = 'left')
pquant = Entry(linhaquant, width = 10)
pquant.pack(side = 'top', pady = 10)

pcadastra = Button(linhainsere, text = 'INSERIR', bg = '#2E8B57', width = 20, command = salvaDados)
pcadastra.pack(side = 'top', pady = 15)
Label(linhainsere, text = '', bg = '#ADD8E6', height = 2).pack()

# ----- TREEVIEW

coluna = ttk.Treeview(container2, selectmode = "browse", column = ("column 1", "column 2", "column 3", "column 4"), show ='headings')

coluna.column("column 1", width = 175 , minwidth = 100, stretch = NO)
coluna.heading("#1", text = "Codigo do produto")

coluna.column("column 2", width = 150 , minwidth = 100, stretch = NO)
coluna.heading("#2", text = "Nome do produto")

coluna.column("column 3", width = 175  , minwidth = 100, stretch = NO)
coluna.heading("#3", text = "custo unitario")

coluna.column("column 4", width = 175  , minwidth = 100, stretch = NO)
coluna.heading("#4", text = "Quantidade desejada")

Label(container2, text = '', bg = '#ADD8E6', width = 20).pack(side = 'right')

coluna.pack()

# ----- WIDGETS DE BAIXO

linhatot = Frame(container3)
linhapag = Frame(container3)
linhafin = Frame(container3)
sul = Frame(container3)

sul.pack(side = 'bottom')
linhatot.pack(side = 'left')
linhapag.pack(side = 'left')
linhafin.pack(side = 'left')

linhatot.configure(bg = '#ADD8E6')
linhapag.configure(bg = '#ADD8E6')
linhafin.configure(bg = '#ADD8E6')
sul.configure(bg = '#ADD8E6')

Label(sul, text = '', height = 3, bg = '#ADD8E6').pack()
pfinexp = Button(sul, text = 'FINALIZAR EXPEDIENTE', bg = '#E9967A', width = 78, font = ('Verdana', '15'), command = finExpediente)
pfinexp.pack()
Label(sul, text = '', height = 7, bg = '#ADD8E6').pack()

Label(linhatot, text = '', bg = '#ADD8E6', width = 28).pack(side = 'right')

Label(linhatot, text = '', height = 2, bg = '#ADD8E6').pack()
tot = Button(linhatot, text = 'TOTAL', bg = '#4682B4', width = 20, command = mostraTotal)
tot.pack()
ltot = Label(linhatot, text = "Total (R$) : ", bg = '#ADD8E6')
ltot.pack(pady = 10)

Label(linhapag, text = '', bg = '#ADD8E6', width = 28).pack(side = 'right')

ltro = Label(linhapag, text = 'Troco (R$):  ', bg = '#ADD8E6')
ltro.pack(side = 'bottom', pady = 10)

tot = Button(linhapag, text = 'TROCO', bg = '#4682B4', width = 23, command = mostraTroco)
tot.pack(side = 'bottom')

Label(linhapag, text = 'Total pago:', bg = '#ADD8E6').pack(side = 'left', pady = 10)
Label(linhapag, text = '', bg = '#ADD8E6', width = 5).pack(side = 'left')
ppag = Entry(linhapag, width = 10)
ppag.pack(side = 'top', pady = 10)

pfin = Button(linhafin, text = 'FINALIZAR COMPRA', width = 20, bg = '#4682B4', command = atualizaEstoque)
pfin.pack()

app.mainloop()

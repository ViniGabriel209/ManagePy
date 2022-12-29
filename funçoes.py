from typing import List
import pymysql.cursors                                 # ----- CONECTA AO BdD
from datetime import datetime                          # ----- DATA
import os                                              # ----- BIBLIOTECAS PARA ENVIO DE EMAIL ↓
import smtplib
from email.message import EmailMessage

# ----- CONEXÃO COM BANCO DE DADOS -----------

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '209213',
    db = 'prototipo',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

# --------------------------------------------

data = datetime.today().strftime('%Y-%m-%d')
hora = datetime.now().strftime('%H:%M:00')
dia = datetime.today().strftime('%A')

# ----- CONSTRUÇÃO DAS FUNÇÕES

def nivel_acesso_funcionarios():                       # ----- FUNÇÃO QUE REALIZA CADASTRO NO PROGRAMA

    objetivo = False

    while objetivo == False:
        nome = input('Digite seu nome: ')
        cargo = input('Digite o seu cargo na empresa: ')
        senha = input('Digite a senha do login: ')
        for linha in funcionarios:
            if nome == linha['nome'] and cargo == linha['cargo'] and senha == linha['senha']:
                nivel_acesso = cargo
                objetivo = True
                break

        if objetivo==False:
            print('Funcionario não autorizado!')
            a=input('deseja uma nova tentativa? [Y/N]')
            if a == 'n' or a == 'N':
                nivel_acesso = 'Programa abortado!!!'
                objetivo=True

    return(nivel_acesso)   

def cadastrarFuncionario():                            # ----- FUNÇÃO PARA CADASTRAR FUNCIONÁRIO

    nome = input('Digite o nome: ')
    cpf = int(input('Digite seu CPF: '))
    cargo = input('Digite o cargo: ')
    salario = input('Digite o salário: ')
    telefone = input('Digite o telefone: ')

    for linha in funcionarios:
        if cpf == linha['cpf']:
            print('Funcionário já cadastrado anteriormente')
            break
        else:
            try:
                with conexao.cursor() as cursor:
                    cursor.execute(f'insert into funcionarios values (default, "{nome}", "{cargo}", "{salario}", "{cpf}", "{telefone}", "email@dominio.br", "{data}", "20923");')
                    conexao.commit()
                print('----------------------\nFuncionário cadastrado\n----------------------')
                break
            except Exception as e:
                print(f'Erro: {e}')

def cadastrarProduto():                                # ----- FUNÇÃO PARA CADASTRAR PRODUTO
    
    jaCadastrado = False

    while True:
        p = input('Digite:\n1 para ver produtos cadastrados\n2 para cadastrar produtos\n3 para sair\n-')
        if p == '1':
            
            for produto in produtos:
                print(produto['nome'], produto['codigo'], produto['custo'], produto['lucro'])
        
        elif p == '2':
            nome = input('Digite o nome do produto: ')
            codigo = int(input('Digite o código de 3 dígitos do produto: '))
            custo = float(input('Digite o custo do produto: '))
            preço = float(input('Digite o preço de venda do produto: '))
            lucro = preço - custo

            for linha in produtos:
                if codigo == linha['codigo']:
                    jaCadastrado = True
                    print('Código de produto já em uso')
                    break
            
            if jaCadastrado == False:
                try:                                               
                    with conexao.cursor() as cursor:
                        cursor.execute(f'insert into produto values (default, "{nome}", "{codigo}","{custo}", "{preço}", "{lucro}", "10");')
                        conexao.commit()
                        print('------------------\nProduto cadastrado\n------------------')
                except:
                    print('Erro ao cadastrar produto')

        elif p == '3':
            break
        
        else:
            print(f'Comando {p} inválido, tente 1, 2 ou 3')

'''
def cadastrarCliente():                                # ----- FUNÇÃO PARA CADASTRAR CLIENTE NO CAIXA
    
    jaCadastrado = False

    nome = input('Digite o nome do cliente: ')
    cpf = int(input('Digite o CPF do cliente: '))
    cartao = random.randint(100000, 999999)
    credito = float(input('Depósito inicial: '))

    for linha in clientes:
        if cpf == linha['cpf']:
            jaCadastrado = True
            print('CPF já cadastrado')
            break
    
    if jaCadastrado == False:
        try:
            with conexao.cursor() as cursor:
                cursor.execute(f'insert into clientes values (default, "{nome}", "{cpf}", "{cartao}", "{credito}");')
                conexao.commit()
                print('Cliente cadastrado')
        except:
            print('Erro ao cadastrar cliente')
        #except Exception as e: 
        #    print(f'Erro: {e}')
'''

def compraCaixa():                                     # ----- FUNÇÃO PARA PASSAR COMPRAS NO CAIXA

    vendas = []                                            # ----- LISTA QUE CONTERÁ O TOTAL DAS VENDAS DO DIA
    todo = 0                                               # ----- VARIÁVEL QUE CONTÉM O VALOR TOTAL DAS VENDAS DO DIA

    while True:

        print('=-' * 6)
        print('NOVA COMPRA')
        print('=-' * 6)

        compra = []

        while True:

            total = 0
            p = int(input('Digite o código do produto (99 para finalizar): '))

            if p >= 100 and p < 120:
                with conexao.cursor() as cursor:
                    cursor.execute(f'select nome, preço, estoque from produto where codigo = "{p}";')
                    nota = cursor.fetchone()               # ----- GERA UM DICIONÁRIO, DIFERENTE DO fetchall, QUE GERA UMA LISTA
                print(nota['nome'], nota['preço'])
                compra.append(nota)
                    
            elif p < 99 or p > 110:
                print('Código inválido')
            elif p == 99:
                print('=-' * 20)
                break

        for item in compra:
            print(f"{item['nome']} -- {item['preço']}")

        for preço in compra:
            valor = float(preço['preço'])
            total = total + valor

        vendas.append(total)                               # ----- COLOCA O TOTAL DA COMPRA NA LISTA vendas PARA SER INSERIDA NO BANCO DE DADOS

        print(f'Total: R${total:.2f}')

        pag = float(input('Valor pago: '))
        troco = pag - total

        print(f'Troco: R${troco:.2f}')

        for produto in compra:                             # ----- ATUALIZA O ESTOQUE CONFORME A COMPRA É FINALIZADA
            n = compra.count(produto)                      # ----- VARIÁVEL QUE DETERMINA A QUANTIDADE DE CADA PRODUTO DIFERENTE NA COMPRA
            try:
                with conexao.cursor() as cursor:
                    cursor.execute(f"update produto set estoque = \'{produto['estoque'] - n}\' where nome = \'{produto['nome']}\'")
                    conexao.commit()
            except:
                print('Erro ao atualizar estoque')

        with conexao.cursor() as cursor:
            cursor.execute(f"insert into horario_compra values (default, '{data}', '{dia}', '{hora}', '{total}');")
            conexao.commit()

        compra = []

        novo = input('Nova compra? [S/N]').upper()

        if novo == 'N':
            break

    for i in range(0, len(vendas)):
        todo = todo + vendas[i]

    print('*********************\nExpediente finalizado\n*********************')

    with conexao.cursor() as cursor:
        cursor.execute(f"insert into fluxo_caixa values (default, 'Dia de vendas', '{data}', '{todo}');")
        conexao.commit()

def pedido():                                          # ----- FUNÇÃO PARA PEDIR PRODUTOS PARA ESTOQUE

    # ----- PARA CADA PRODUTO A SER PEDIDO, É NECESSÁRIO ESTE ESTAR PREVIAMENTE CADASTRADO

    antigo = False                                         # VARIÁVEL DEFINE SE O FORNECEDOR JÁ ESTÁ CADASTRADO

    meu_email = 'empresa.python@gmail.com'
    senha = 'trabalhodepython'

    nome = input('Digite o nome do fornecedor: ')
    cnpj = input('Digite o CNPJ do fornecedor da compra: ')

    for linha in fornecedores:                             # CHECA SE O FORNECEDOR JÁ ESTÁ CADASTRADO
        if cnpj == linha['cnpj'] and nome == linha['nome']:
            print('Fornecedor antigo, continue a compra')
            with conexao.cursor() as cursor:
                cursor.execute(f'select email from fornecedores where cnpj = "{cnpj}";')
                emailLista = cursor.fetchall()
                for dado in emailLista:
                    email = dado['email']
            antigo = True
            break

    if antigo == False:
        endereço = input('Digite o endereço do fornecedor: ')
        email = input('Digite o email do fornecedor para enviar pedido: ')
        try:
            with conexao.cursor() as cursor:
                cursor.execute(f'insert into fornecedores values (default, "{nome}", "{endereço}", "{cnpj}", "{email}");')
                conexao.commit()
        except:
            print('Erro ao cadastrar fornecedor')
    
    pedido = []
    add_pedido = []                                        # LISTA DE LISTAS A SER ADICIONADA NA TABELA PEDIDOS NO BdD (é necessário que o conteúdo da lista sejam listas)
    pega_pedido = []                                       # LISTA A SER ADICIONADA NA LISTA ACIMA

    while True:

        total = 0
        p = int(input('Digite o código do produto (99 para finalizar): '))

        if p == 99:
            print('=-' * 20)
            break

        n = int(input('Digite a quantidade de unidades do produto: '))

        if p >= 100 and p < 120:
            for q in range(0, n):
                with conexao.cursor() as cursor:
                    cursor.execute(f'select nome, custo, estoque from produto where codigo = "{p}";')
                    nota = cursor.fetchone()               # GERA UM DICIONÁRIO, DIFERENTE DO fetchall, QUE GERA UMA LISTA
                #print(nota['nome'], nota['custo'])
                pedido.append(nota)
            
            pega_pedido.append(nota['nome'])
            pega_pedido.append(nota['custo'])
            pega_pedido.append(n)
            add_pedido.append(pega_pedido)
            ultimo = f"{pega_pedido[0]} -- {pega_pedido[1]} -- x{pega_pedido[2]}"  # VARIÁVEL A SER PRINTADA DEPOIS DE CADA PRODUTO SELECIONADO
            print(ultimo)
            pega_pedido = []                               # LIMPA A LISTA PARA SER ADICIONADA NOVAMENTE DEPOIS

        elif p < 99 or p > 110:
            print('Código inválido')

    for item in add_pedido:
        print(f"{item[0]} -- R${item[1]} -- x{item[2]}")

    for custo in pedido:
        valor = float(custo['custo'])
        total = total + valor   

    print(f'Total: R${total:.2f}')

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

def verPedidos():                                      # ----- FUNÇÃO PARA VER PEDIDOS COMO ENTREGUE OU PENDENTE

    listaPedidoString = []                                 # LISTA QUE POSSUI TODOS OS PEDIDOS (strings)
    listaPedidoLista = []                                  # LISTA QUE POSSUI PEDIDOS (lista)
    listaPedido = []                                       # LISTA QUE POSSUI PEDIDOS INDIVIDUALEMENTE E SUA SITUAÇÃO (pendente ou entregue)
    
    try:                                                   # ----- LISTA DE PEDIDOS
        with conexao.cursor() as cursor:
            cursor.execute('select * from pedidos;')
            pedidu = cursor.fetchall()
    except:
        print('Erro ao conectar ao banco de dados dos pedidos')

    for pedidoMaximo in pedidu:
        listaPedidoString.append(pedidoMaximo['pedido'])

    for pedido in listaPedidoString:                       # TRANSFORMA OS ELEMENTOS DA LISTA MÁXIMA (strings) EM LISTA ATRAVÉS DO eval()
        pedidon = eval(pedido)
        listaPedidoLista.append(pedidon)

    for situação in pedidos:
        if situação['data_entregue'] == None:
            num = int(situação['id'] - 1)
            listaPedido.append(situação['id'])
            listaPedido.append(listaPedidoLista[num])
            listaPedido.append('Pendente')
        else:
            num = int(situação['id'] - 1)
            listaPedido.append(situação['id'])
            listaPedido.append(listaPedidoLista[num])
            listaPedido.append('Entregue')

    for i in range(0, len(listaPedido), 3):
        print(listaPedido[i], *listaPedido[i+1], listaPedido[i+2])

    '''
    for situação in pedidos:
        if situação['data_entregue'] == None:
            num = int(situação['id'] - 1)
            listaPedidosMinimaPendente = []
            listaPedidosMinimaPendente.append(listaPedidoLista[num])
            listaPedidosMinimaPendente.append('Pendente')
            print(listaPedidosMinimaPendente)
        else:
            num = int(situação['id'] - 1)
            listaPedidosMinimaEntregue = []
            listaPedidosMinimaEntregue.append(listaPedidoLista[num])
            listaPedidosMinimaEntregue.append('Entregue')
            print(listaPedidosMinimaEntregue)
    '''

def atualizaPedidos():                                 # ----- FUNÇÃO PARA DAR BAIXA NOS PEDIDOS E ATUALIZAR ESTOQUE

    listaPedidoString = []                                 # LISTA QUE POSSUI TODOS OS PEDIDOS (strings)
    listaPedidoLista = []                                  # LISTA QUE POSSUI PEDIDOS (lista)
    listaPedido = []                                       # LISTA QUE POSSUI PEDIDOS INDIVIDUALEMENTE 
    listaPedidoMenor = []                                  # CONTÉM PRODUTOS INDIVIDUAIS PARA ATUALIZAR ESTOQUE

    for pedidoMaximo in pedidos:
        listaPedidoString.append(pedidoMaximo['pedido'])

    for pedido in listaPedidoString:                       # TRANSFORMA OS ELEMENTOS DA LISTA MÁXIMA (strings) EM LISTA ATRAVÉS DO eval()
        pedidon = eval(pedido)
        listaPedidoLista.append(pedidon)

    while True:

        n = int(input('Qual pedido deseja dar baixa (-1 para encerrar)? '))

        if n in range(1, len(listaPedidoString) + 1):
            try:
                with conexao.cursor() as cursor:
                    cursor.execute(f'update pedidos set data_entregue = "{data}" where id = "{n}";')
                    conexao.commit()
                print(f'Atestada a entrega do pedido n° {n}')
            except:
                print('Erro ao dar baixa no pedido')

            try:                                                   # ----- LISTA DE PEDIDOS ATUALIZADA
                with conexao.cursor() as cursor:                   #
                    cursor.execute('select * from pedidos;')       #
                    pedidu = cursor.fetchall()                     #
            except:
                print('Erro ao conectar ao banco de dados dos pedidos')

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
            
                            try:
                                with conexao.cursor() as cursor:
                                    cursor.execute(f'update produto set estoque = "{listaPedidoMenor[1] + listaPedidoMenor[2]}" where nome = "{listaPedidoMenor[0]}";')
                                    conexao.commit()
                            except Exception as e:
                                print(f'Erro: {e}')
                                print('Erro ao atualizar estoque')

                            listaPedidoMenor = []                  # REINICIA LISTA
                            
                    listaPedido = []                               # REINICIA LISTA

            with conexao.cursor() as cursor:
                cursor.execute(f"select valor from pedidos where id = '{n}';")
                valor = cursor.fetchone()                  # GERA UM DICIONÁRIO, DIFERENTE DO fetchall, QUE GERA UMA LISTA
                    
            with conexao.cursor() as cursor:
                cursor.execute(f"insert into fluxo_caixa values (default, 'pagamento de pedido {n}', '{data}', '-{valor['valor']}');")
                conexao.commit()

        elif n == -1:
            break
        else:
            print(f'Dígito {n} inválido. Tente novamente')

def pagamentos():                                      # ----- FUNÇÃO PARA REALIZAR PAGAMENTO DE FUNCIONARIOS

    listaFuncionario = []                                   # ----- LISTA QUE CONTÉM TODOS OS FUNCIONÁRIOS

    for funcionario in funcionarios:
        print(f"{funcionario['id']}: {funcionario['nome']} - {funcionario['cargo']} - {funcionario['salario']} - {funcionario['hist_pagamento']}")
        listaFuncionario.append(funcionario['nome'])
        listaFuncionario.append(funcionario['salario'])

    n = int(input('Cadastrar pagamento de qual funcionário? '))
    nome = listaFuncionario[2*n - 2]
    salario = listaFuncionario[2*n - 1]

    print(listaFuncionario)
    print(nome, salario)

    try:
        with conexao.cursor() as cursor:
            cursor.execute(f'insert into fluxo_caixa values (default, "pag {nome}", "{data}", "-{salario}");')
            conexao.commit()
    except:
        print('Erro ao atualizar pagamento no fluxo de caixa')

    p = funcionarios[n - 1]

    print(p['hist_pagamento'])

    if p['hist_pagamento'] == None:
        try:
            with conexao.cursor() as cursor:
                cursor.execute(f'update funcionarios set hist_pagamento = "{data}" where id = "{n}";')
                conexao.commit()
        except Exception as e:
            print(f'Erro: {e}')
    else:
        hist = ''
        hist = p['hist_pagamento'] + ' - ' + data
        try:
            with conexao.cursor() as cursor:
                cursor.execute(f'update funcionarios set hist_pagamento = "{hist}" where id = "{n}";')
                conexao.commit()
        except Exception as e:
            print(f'Erro: {e}')


# ----- GERAÇÃO DE LISTAS DE DICIONÁRIOS COM AS LINHAS DO BANCO DE DADOS 

try:                                                   # ----- LISTA DE FUNCIONÁRIOS
    with conexao.cursor() as cursor:
        cursor.execute('select * from funcionarios;')
        funcionarios = cursor.fetchall()   
except:
    print('Erro ao conectar ao banco de dados dos funcionários')

'''
try:                                                   # ----- LISTA DE CLIENTES CADASTRADOS
    with conexao.cursor() as cursor:
        cursor.execute('select * from clientes;')
        clientes = cursor.fetchall()
except:
    print('Erro ao conectar ao banco de dados dos clientes')
'''

try:                                                   # ----- LISTA DE PRODUTOS CADASTRADOS
    with conexao.cursor() as cursor:
        cursor.execute('select * from produto;')
        produtos = cursor.fetchall()
except:
    print('Erro ao conectar ao banco de dados dos clientes')

try:                                                   # ----- LISTA DE FORNECEDORES CADASTRADOS
    with conexao.cursor() as cursor:
        cursor.execute('select * from fornecedores;')
        fornecedores = cursor.fetchall()
except:
    print('Erro ao conectar ao banco de dados dos fornecedores')

try:                                                   # ----- LISTA DE PEDIDOS
    with conexao.cursor() as cursor:
        cursor.execute('select * from pedidos;')
        pedidos = cursor.fetchall()
except:
    print('Erro ao conectar ao banco de dados dos pedidos')

# ----- AQUI DEVEM VIR AS FUNÇÕES (após as listas de dicionários, as funções dependem destas listas)

# ----- PODEM SER TESTADAS INDIVIDUALMENTE PARA CONSULTA DO FUNCIONAMENTO DA FUNÇÃO NO TERMINAL

#nivel_acesso_funcionarios()
#cadastrarFuncionario()
#cadastrarProduto()
#compraCaixa()
#pedido()
#verPedidos()
#atualizaPedidos()
#pagamentos()
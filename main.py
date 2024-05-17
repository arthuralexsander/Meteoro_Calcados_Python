import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QTabWidget, QErrorMessage
from sqlite3 import Cursor
import mysql
import mysql.connector
from mysql.connector import Error

#Conectar ao banco de dados
banco = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='123456',
    database='meteoro_calcados'
    )


app = QtWidgets.QApplication ([])



#Definir função da tela para chamar, fechar,etc
def chamar_principal():
    global nomeusuario
    nomeusuario = login.inserir_usuario.text()
    senhausuario = login.inserir_senha.text()
    
    ##criar o cursor para conectar e varrer as telas
    Cursor = banco.cursor()
    
    #Realizar a busca através do select
    busca = ("SELECT email_funcionario, cpf_funcionario FROM  funcionario WHERE email_funcionario = %s and cpf_funcionario = %s")
    b2 = (nomeusuario,senhausuario)
    
    
    #Executar a busca
    Cursor.execute(busca,b2)
    
    #Laço de repetição para varrer linha por linha
    for(email_funcionario, cpf_funcionario) in Cursor.fetchall():
        
        #comprarar e analisar 
        if nomeusuario == email_funcionario and senhausuario == cpf_funcionario:
            login.hide()
            principal.show()
        else:
            erro = QWidget
            erro = QErrorMessage.msg("Usuário ou Senha Inválido")
            erro.exec_()


#função de cadastrar produtos
def cadastrarprodutos():
    nomeproduto = cadastroprod.inserir_nome_produto.text()
    tamanho = cadastroprod.inserir_tamanho.text()
    precocusto = cadastroprod.inserir_preco_custo.text()
    precovenda = cadastroprod.inserir_preco_venda.text()
    modelo = cadastroprod.inserir_modelo.text()
    cor = cadastroprod.inserir_cor.text()
    marca = cadastroprod.inserir_marca.text()
    quantidade = cadastroprod.inserir_qntd_recebida.text()
    #habilitar cursor e inserir na tabela
    Cursor = banco.cursor()
    cadastro = ("INSERT INTO produtos(nome_produto,tamanho_produto,modelo_produto,cor_produto,marca_produto,preco_custo,preco_venda,qtd_produto) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
    produtos = (nomeproduto,tamanho,modelo,cor,marca,precocusto,precovenda,quantidade)
    Cursor.execute(cadastro,produtos)
    banco.commit()
    Cursor.close()
    #definir os espaços em branco após cadastro
    nomeproduto = cadastroprod.inserir_nome_produto.setText('')
    tamanho = cadastroprod.inserir_tamanho.setText('')
    precocusto = cadastroprod.inserir_preco_custo.setText('')
    precovenda = cadastroprod.inserir_preco_venda.setText('')
    modelo = cadastroprod.inserir_modelo.setText('')
    cor = cadastroprod.inserir_cor.setText('')
    marca = cadastroprod.inserir_marca.setText('')
    quantidade = cadastroprod.inserir_qntd_recebida.setText('')

#função para cadastrar pessoas
def cadastrar():
    #extrair valores
    nome = cadastro.inserirnome.text()
    sobrenome = cadastro.inserirsobrenome.text()
    cpf = cadastro.inserircpf.text()
    telefone = cadastro.inserirtelefone.text()
    email = cadastro.inseriremail.text()
    cep = cadastro.inserircep.text()
    rua = cadastro.inserirrua.text()
    numero = cadastro.inserirnumerorua.text()
    bairro = cadastro.inserirbairro.text()
    cidade = cadastro.inserircidade.text()
    estado = cadastro.inserirestado.currentText()
    Cursor = banco.cursor()
    #cadastro no banco de dados de acordo com o botao marcado
    if cadastro.op_cliente.isChecked():
        tabela = ("INSERT INTO cliente(nome_cliente,sobrenome_cliente,cpf_cliente,telefone_cliente,email_cliente) VALUES (%s,%s,%s,%s,%s)")
        sttm = (nome,sobrenome,cpf,telefone,email)
        endereco = ("INSERT INTO endereco (cep,estado,cidade,bairro,rua,numero_casa) VALUES(%s,%s,%s,%s,%s,%s)")
        sttm2 = (cep,estado,cidade,bairro,rua,numero)
    if cadastro.op_funcionario.isChecked():
        tabela = ("INSERT INTO funcionario(nome_funcionario,sobrenome_funcionario,cpf_funcionario,telefone_funcionario,email_funcionario) VALUES (%s,%s,%s,%s,%s)")
        sttm = (nome,sobrenome,cpf,telefone,email)
        endereco = ("INSERT INTO endereco_funcionario (cep,estado,cidade,bairro,rua,numero_casa) VALUES(%s,%s,%s,%s,%s,%s)")
        sttm2 = (cep,estado,cidade,bairro,rua,numero)
    Cursor.execute(tabela,sttm)
    Cursor.execute(endereco,sttm2)
    banco.commit()
    print('CADASTRO efetuado')
    #limpar campos
    nome = cadastro.inserirnome.setText('')
    sobrenome = cadastro.inserirsobrenome.setText('')
    cpf = cadastro.inserircpf.setText('')
    telefone = cadastro.inserirtelefone.setText('')
    email = cadastro.inseriremail.setText('')
    cep = cadastro.inserircep.setText('')
    rua = cadastro.inserirrua.setText('')
    numero = cadastro.inserirnumerorua.setText('')
    bairro = cadastro.inserirbairro.setText('')
    cidade = cadastro.inserircidade.setText('')

#função para chamar tela de cad produtos
def chamar_cadprodutos():
    principal.hide()
    cadastroprod.show()

#função para chamar estoque
def chamar_estoque():
    principal.hide()
    estoque.show()

#função para chamar cad pessoas
def chamar_cadpessoas():
    principal.hide()
    cadastro.show()

def chamar_vendas():
    principal.hide()
    vendas.show()

#funções para o botao de voltar
def voltar_cadprodutos():
    cadastroprod.close()
    principal.show()


def voltar_estoque():
    estoque.close()
    principal.show()


def voltar_cadpessoas():
    cadastro.close()
    principal.show()

#função voltar para o login
def voltar_principal():
    principal.close()
    login.show()

def voltar_vendas():
    vendas.close()
    principal.show()

def verestoque():
    cadastroprod.close()
    estoque.show()
#função de limpar e logo abaixo de apagar campos
def limpar():
    nome = cadastro.inserirnome.setText('')
    sobrenome = cadastro.inserirsobrenome.setText('')
    cpf = cadastro.inserircpf.setText('')
    telefone = cadastro.inserirtelefone.setText('')
    email = cadastro.inseriremail.setText('')
    cep = cadastro.inserircep.setText('')
    rua = cadastro.inserirrua.setText('')
    numero = cadastro.inserirnumerorua.setText('')
    bairro = cadastro.inserirbairro.setText('')
    cidade = cadastro.inserircidade.setText('')

def apagar():
    nomeproduto = cadastroprod.inserir_nome_produto.setText('')
    tamanho = cadastroprod.inserir_tamanho.setText('')
    precocusto = cadastroprod.inserir_preco_custo.setText('')
    precovenda = cadastroprod.inserir_preco_venda.setText('')
    modelo = cadastroprod.inserir_modelo.setText('')
    cor = cadastroprod.inserir_cor.setText('')
    marca = cadastroprod.inserir_marca.setText('')
    quantidade = cadastroprod.inserir_qntd_recebida.setText('')

#funções de consulta
def consultar_cliente():
    #código
    bCod = cadastro.inserir_codigopessoas.text()
    Cursor = banco.cursor()
    #consultar cliente pelo código
    if cadastro.op_cliente.isChecked():
        #iniciando a consulta pelo codigo digitado
        query = f"SELECT * FROM cliente WHERE cod_cliente = '{bCod}'"
        Cursor.execute(query)
        #varrer banco de dados pelos dados
        selecionar = Cursor.fetchall()
        #definindo os valores do campos de acordo com a busca
        cNome = cadastro.inserirnome.setText(str(selecionar[0][1]))
        cSobrenome = cadastro.inserirsobrenome.setText(str(selecionar[0][2]))
        cCpf = cadastro.inserircpf.setText(str(selecionar[0][3]))
        cTelefone = cadastro.inserirtelefone.setText(str(selecionar[0][4]))
        cEmail = cadastro.inseriremail.setText(str(selecionar[0][5]))
        #definindo valores dos campos de acordo com endereco
        query2 = f"SELECT * FROM endereco WHERE cod_endereco = '{bCod}'"
        Cursor.execute(query2)
        selecionar2 = Cursor.fetchall()
        #varrer banco de dados
        cCep = cadastro.inserircep.setText(str(selecionar2[0][1]))
        cEstado = cadastro.inserirestado.setCurrentText(str(selecionar2[0][2]))
        cCidade = cadastro.inserircidade.setText(str(selecionar2[0][3]))
        cBairro = cadastro.inserirbairro.setText(str(selecionar2[0][4]))
        cRua = cadastro.inserirrua.setText(str(selecionar2[0][5]))
        cNumero = cadastro.inserirnumerorua.setText(str(selecionar2[0][6]))

    if cadastro.op_funcionario.isChecked():
        query = f"SELECT * FROM funcionario WHERE cod_funcionario = '{bCod}'"
        Cursor.execute(query)
        selecionar = Cursor.fetchall()
        cNome = cadastro.inserirnome.setText(str(selecionar[0][1]))
        cSobrenome = cadastro.inserirsobrenome.setText(str(selecionar[0][2]))
        cCpf = cadastro.inserircpf.setText(str(selecionar[0][3]))
        cTelefone = cadastro.inserirtelefone.setText(str(selecionar[0][4]))
        cEmail = cadastro.inseriremail.setText(str(selecionar[0][5]))
        query2 = f"SELECT * FROM endereco_funcionario WHERE cod_endereco = '{bCod}'"
        Cursor.execute(query2)
        selecionar2 = Cursor.fetchall()
        cCep = cadastro.inserircep.setText(str(selecionar2[0][1]))
        cEstado = cadastro.inserirestado.setCurrentText(str(selecionar2[0][2]))
        cCidade = cadastro.inserircidade.setText(str(selecionar2[0][3]))
        cBairro = cadastro.inserirbairro.setText(str(selecionar2[0][4]))
        cRua = cadastro.inserirrua.setText(str(selecionar2[0][5]))
        cNumero = cadastro.inserirnumerorua.setText(str(selecionar2[0][6]))    

def consultarestoque():
    Cursor = banco.cursor()
    sql = "SELECT * from produtos"
    Cursor.execute(sql)
    selecao = Cursor.fetchall()
    #loop de repetição para matriz dos numeros
    estoque.dados_estoque.setRowCount(len(selecao))
    estoque.dados_estoque.setColumnCount(7)
    for i in range(0,len(selecao)):
        for j in range (0,7):
            estoque.dados_estoque.setItem(i,j,QtWidgets.QTableWidgetItem(str(selecao[i][j])))

def atualizarcadastro():
    bCod = cadastro.inserir_codigopessoas.text()
    nome = cadastro.inserirnome.text()
    sobrenome = cadastro.inserirsobrenome.text()
    cpf = cadastro.inserircpf.text()
    telefone = cadastro.inserirtelefone.text()
    email = cadastro.inseriremail.text()
    cep = cadastro.inserircep.text()
    rua = cadastro.inserirrua.text()
    numero = cadastro.inserirnumerorua.text()
    bairro = cadastro.inserirbairro.text()
    cidade = cadastro.inserircidade.text()
    estado = cadastro.inserirestado.currentText()
    Cursor = banco.cursor()
    #cadastro no banco de dados de acordo com o botao marcado
    if cadastro.op_cliente.isChecked():
        #atualizar dados cliente
        tabela = (f"UPDATE cliente SET nome_cliente = %s, sobrenome_cliente = %s, cpf_cliente = %s, telefone_cliente = %s, email_cliente = %s WHERE cod_cliente = {bCod}")
        sttm = (nome, sobrenome,cpf, telefone, email)
        Cursor.execute(tabela,sttm)
        #atualizar dados cliente
        endereco = (f"UPDATE endereco SET cep = %s, estado = %s, cidade = %s , bairro = %s, rua = %s, numero_casa = %s WHERE cod_endereco = {bCod}")
        sttm2 = (cep,estado,cidade,bairro,rua,numero)
        Cursor.execute(endereco,sttm2)
        print('atualizado')
    if cadastro.op_funcionario.isChecked():
        #atualizar dados cliente
        tabela = (f"UPDATE funcionario SET nome_funcionario = %s, sobrenome_funcionario = %s, cpf_funcionario = %s, telefone_funcionario = %s, email_funcionario = %s WHERE cod_funcionario = {bCod}")
        sttm = (nome,sobrenome,cpf,telefone,email)
        Cursor.execute(tabela,sttm)
        #atualizar dados cliente
        endereco = (f"UPDATE endereco_funcionario SET cep = %s, estado = %s, cidade = %s , bairro = %s, rua = %s, numero_casa = %s WHERE cod_endereco = {bCod}")
        sttm2 = (cep,estado,cidade,bairro,rua,numero)
        Cursor.execute(endereco,sttm2)
        print('atualizado')
    
    # salvar alterações
    banco.commit()
    bCod = cadastro.inserir_codigopessoas.setText('')
    nome = cadastro.inserirnome.setText('')
    sobrenome = cadastro.inserirsobrenome.setText('')
    cpf = cadastro.inserircpf.setText('')
    telefone = cadastro.inserirtelefone.setText('')
    email = cadastro.inseriremail.setText('')
    cep = cadastro.inserircep.setText('')
    rua = cadastro.inserirrua.setText('')
    numero = cadastro.inserirnumerorua.setText('')
    bairro = cadastro.inserirbairro.setText('')
    cidade = cadastro.inserircidade.setText('')
    Cursor = banco.cursor()
          
#consultando produtos
def consultarprodutos():
    pCod = cadastroprod.inserir_cod.text()
    Cursor = banco.cursor()
    Query = f"SELECT * from produtos where cod_produto = {pCod}"
    Cursor.execute(Query)
    selecao = Cursor.fetchall()
    nomeproduto = cadastroprod.inserir_nome_produto.setText(str(selecao[0][1]))
    modelo = cadastroprod.inserir_modelo.setText(str(selecao[0][2]))
    cor = cadastroprod.inserir_cor.setText(str(selecao[0][3]))
    marca = cadastroprod.inserir_marca.setText(str(selecao[0][4]))
    tamanho = cadastroprod.inserir_tamanho.setText(str(selecao[0][5]))
    precocusto = cadastroprod.inserir_preco_custo.setText(str(selecao[0][6]))
    precovenda = cadastroprod.inserir_preco_venda.setText(str(selecao[0][7]))
    quantidade = cadastroprod.inserir_qntd_recebida.setText(str(selecao[0][8]))


# atualizar produtos existentes 
def atualizarprodutos():
    pCod = cadastroprod.inserir_cod.text()
    nomeproduto = cadastroprod.inserir_nome_produto.text()
    tamanho = cadastroprod.inserir_tamanho.text()
    precocusto = cadastroprod.inserir_preco_custo.text()
    precovenda = cadastroprod.inserir_preco_venda.text()
    modelo = cadastroprod.inserir_modelo.text()
    cor = cadastroprod.inserir_cor.text()
    marca = cadastroprod.inserir_marca.text()
    quantidade = cadastroprod.inserir_qntd_recebida.text()
    Cursor = banco.cursor()
    # atualizacao
    cadastro = (f"UPDATE produtos SET nome_produto = %s, modelo_produto = %s, cor_produto = %s, marca_produto = %s, tamanho_produto = %s, preco_custo = %s, preco_venda = %s, qtd_produto = %s WHERE cod_produto = {pCod}")
    produtos = (nomeproduto,modelo,cor,marca,tamanho,precocusto,precovenda,quantidade)
    Cursor.execute(cadastro,produtos)
    banco.commit()

    print('atualizado')

#excluir cadastros
def excluircadastro():
    eCod = int(cadastro.inserir_codigopessoas.text()) 
    Cursor = banco.cursor()
    # condições para deletar de acordo com o que for selecionado
    if cadastro.op_cliente.isChecked():
        excluir = "DELETE FROM cliente WHERE cod_cliente = '{}'".format(eCod)
        excluire = "DELETE FROM endereco WHERE cod_endereco = '{}'".format(eCod)
        print('excluido cliente')
    if cadastro.op_funcionario.isChecked():
        excluir = "DELETE FROM funcionario WHERE cod_funcionario = '{}'".format(eCod)
        excluire = "DELETE FROM endereco_funcionario WHERE cod_endereco = '{}'".format(eCod)
        print('excluido funcionario')

    Cursor.execute(excluir)
    Cursor.execute(excluire)
    banco.commit()
    bCod = cadastro.inserir_codigopessoas.setText('')
    nome = cadastro.inserirnome.setText('')
    sobrenome = cadastro.inserirsobrenome.setText('')
    cpf = cadastro.inserircpf.setText('')
    telefone = cadastro.inserirtelefone.setText('')
    email = cadastro.inseriremail.setText('')
    cep = cadastro.inserircep.setText('')
    rua = cadastro.inserirrua.setText('')
    numero = cadastro.inserirnumerorua.setText('')
    bairro = cadastro.inserirbairro.setText('')
    cidade = cadastro.inserircidade.setText('')

#deletar produtos pelo codigo
def excluirprodutos():
    eCod = cadastroprod.inserir_cod.text()
    Cursor = banco.cursor()
    # delete produto
    exclusao = "DELETE FROM produtos WHERE cod_produto = '{}'".format(eCod)
    Cursor.execute(exclusao)
    banco.commit()
    eCod = cadastroprod.inserir_cod.setText('')
    nomeproduto = cadastroprod.inserir_nome_produto.setText('')
    tamanho = cadastroprod.inserir_tamanho.setText('')
    precocusto = cadastroprod.inserir_preco_custo.setText('')
    precovenda = cadastroprod.inserir_preco_venda.setText('')
    modelo = cadastroprod.inserir_modelo.setText('')
    cor = cadastroprod.inserir_cor.setText('')
    marca = cadastroprod.inserir_marca.setText('')
    quantidade = cadastroprod.inserir_qntd_recebida.setText('')

#fazer consulta para que 
def consultavenda():
    vCod = vendas.inserircod.text()
    Cursor = banco.cursor()
    Query = f"SELECT * from produtos where cod_produto = {vCod}"
    Cursor.execute(Query)
    selecao = Cursor.fetchall()
    nomeproduto = vendas.modelo.setText(str(selecao[0][1]))
    marca = vendas.marca.setText(str(selecao[0][4]))
    tamanho = vendas.tamanho.setText(str(selecao[0][5]))
    valor = vendas.mvalor.setText(str(selecao[0][7]))

#definir o subtotal ao trocar a linha 
def subtotal():
    precounit = vendas.mvalor.text()
    qtd = vendas.inserirqtd.text()
    subtotal = float(qtd)*float(precounit)
    subtotal1 = vendas.subtotal.setText(str(subtotal))

#adicionar item ao carrinho
def adicionaritem():
    vCod = vendas.inserircod.text()
    nome = vendas.modelo.text()
    marca = vendas.marca.text()
    precounit = vendas.mvalor.text()
    tamanho = vendas.tamanho.text()
    qtd = vendas.inserirqtd.text()
    subtotal = vendas.subtotal.text()
    Cursor = banco.cursor()
    cart = "INSERT INTO carrinho VALUES(%s,%s,%s,%s,%s,%s,%s)"
    sttm = (vCod,nome,marca,tamanho,qtd,precounit,subtotal)
    Cursor.execute(cart,sttm)
    banco.commit()
    print('Foi pro cart')

#limpar campos ao adicionar
def limpar():
    nome = vendas.modelo.setText('')
    marca = vendas.marca.setText('')
    precounit = vendas.mvalor.setText('')
    tamanho = vendas.tamanho.setText('')
    qtd = vendas.inserirqtd.setText('')
    subtotal = vendas.subtotal.setText('')

def apagarvendas():
    rCod = vendas.inserircod.setText('')
    nome = vendas.modelo.setText('')
    marca = vendas.marca.setText('')
    precounit = vendas.mvalor.setText('')
    tamanho = vendas.tamanho.setText('')
    qtd = vendas.inserirqtd.setText('')
    subtotal = vendas.subtotal.setText('')

#mostrar carrinho
def mostrarcart():
    Cursor = banco.cursor()
    sql = "SELECT * from carrinho"
    Cursor.execute(sql)
    selecao = Cursor.fetchall()
    vendas.tabcarrinho.setRowCount(len(selecao))
    vendas.tabcarrinho.setColumnCount(7)
    for i in range(0,len(selecao)):
        for j in range (0,7):
            vendas.tabcarrinho.setItem(i,j,QtWidgets.QTableWidgetItem(str(selecao[i][j])))
    total = "Select SUM(subtotal) as total from carrinho"
    Cursor.execute(total)
    ptotal = Cursor.fetchall()
    ptotal1 = vendas.valortotal.setText(str(ptotal[0][0]))

#finalizar o pagamento
def finalizar():
    pagamento.show()
    Cursor = banco.cursor()
    total = "Select SUM(subtotal) as total from carrinho"
    Cursor.execute(total)
    ptotal = Cursor.fetchall()
    pagamento1 = pagamento.valortotal.setText(str(ptotal[0][0]))
#remover um item do carrinho
def remover():
    rCod = vendas.inserircod.text()
    Cursor = banco.cursor()
    apagar = f"DELETE from carrinho WHERE cod = {rCod}"
    Cursor.execute(apagar)
    banco.commit()
    print('removido')

#Carregamento de Telas
principal = uic.loadUi('pag_inicial.ui')
login = uic.loadUi('pag_login.ui')
estoque = uic.loadUi('pag_estoque.ui')
cadastro = uic.loadUi('pag_cadastro.ui')
cadastroprod = uic.loadUi('pag_cadastroprod.ui')
vendas = uic.loadUi('vendas.ui')
pagamento = uic.loadUi('pagamento.ui')



#Definir função no botão e chamar
login.bt_login.clicked.connect(chamar_principal)

#botoes principal
principal.bt_tela_cad.clicked.connect(chamar_cadprodutos)
principal.bt_estoque.clicked.connect(chamar_estoque)
principal.bt_telacadpessoas.clicked.connect(chamar_cadpessoas)
principal.bt_voltarinicial.clicked.connect(voltar_principal)
principal.bt_vendas.clicked.connect(chamar_vendas)

#botoes cadastro pessoas
cadastro.bt_voltarcadpessoas.clicked.connect(voltar_cadpessoas)
cadastro.bt_cadastrar.clicked.connect(cadastrar)
cadastro.bt_limpar.clicked.connect(limpar)
cadastro.bt_consultar.clicked.connect(consultar_cliente)
cadastro.bt_atualizar.clicked.connect(atualizarcadastro)
cadastro.bt_deletar.clicked.connect(excluircadastro)

#botoes estoque
estoque.bt_voltarestoque.clicked.connect(voltar_estoque)
estoque.bt_consultar.clicked.connect(consultarestoque)

#botoes de cadastro produto
cadastroprod.bt_cadastrar.clicked.connect(cadastrarprodutos)
cadastroprod.bt_apagar.clicked.connect(apagar)
cadastroprod.bt_voltarcadprod.clicked.connect(voltar_cadprodutos)
cadastroprod.bt_consultar.clicked.connect(consultarprodutos)
cadastroprod.bt_atualizar.clicked.connect(atualizarprodutos)
cadastroprod.bt_deletar.clicked.connect(excluirprodutos)
cadastroprod.bt_ver_estoque.clicked.connect(verestoque)

#botoes tela de venda
vendas.bt_voltarvendas.clicked.connect(voltar_vendas)
vendas.bt_buscar.clicked.connect(consultavenda)
vendas.bt_adicionar.clicked.connect(adicionaritem)
vendas.bt_adicionar.clicked.connect(mostrarcart)
vendas.bt_adicionar.clicked.connect(limpar)
vendas.inserirqtd.editingFinished.connect(subtotal)
vendas.bt_finalizar.clicked.connect(finalizar)
vendas.bt_remover.clicked.connect(remover)
vendas.bt_remover.clicked.connect(mostrarcart)
vendas.bt_apagar.clicked.connect(apagarvendas)

#iniciar mostrando o login
login.show()

#executar app
app.exec_()
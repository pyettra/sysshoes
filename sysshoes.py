

### SISTEMA DE GERENCIAMENTO DE VENDAS SYSSHOES ###

### Importações ###
from tkinter import *
from random import randint
import sqlite3
import io

print("\n\n\n\n \t********** BEM-VINDO **********\n\n\n\n")


print("Escolha uma opção:\n")
print("a - Cadastro Cliente")
print("b - Cadastro Funcionario")
print("c - Cadastro Produto")
print("d - Controle Vendas")

n = input()

if n == 'a':

    ### Globais ###
   
    conn = sqlite3.connect("ppr.db")
    
    cursor = conn.cursor()

    def criarTabela1():
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cpfcliente INTEGER NOT NULL PRIMARY KEY,
                nomecliente TEXT NOT NULL,
                numero INTEGER NOT NULL 
            ); 
        """) #definições das aplicações em banco de dados#

    criarTabela1()

    #### Definições da Aplicação Principal ###
    principal = Tk()
    principal.title("SysShoes - Adicionar Cliente")
    principal.geometry("700x450")
    principal.resizable(TRUE, TRUE)

    #### Funções ###
    def adicionar_cliente():
        cpfcliente = etCpfcliente.get()
        nomecliente = etNomecliente.get()
        numero = etNumero.get()
        cursor.execute("""
            INSERT INTO clientes (cpfcliente, nomecliente, numero) VALUES (?, ?, ?)""", (cpfcliente, nomecliente, numero))
        conn.commit()
        lstClientes.insert(END, (cpfcliente, nomecliente, numero))

    def deletar_cliente():
        cpfcliente_cliente = etCpfclienteDeletar.get()
        cursor.execute("""
            DELETE FROM clientes WHERE cpfcliente=?""", (cpfcliente_cliente,))
        conn.commit()
        lstClientes.delete(0, END)
        lista = cursor.execute("""
            SELECT * FROM clientes;
            """)
        for i in lista:
            lstClientes.insert(END, i)

    def mudar_numero():
        cpfcliente_cliente = etCpfclienteMudar.get()
        novo_numero = etNovoNumero.get()
        cursor.execute("""
            UPDATE clientes SET numero = ? WHERE cpfcliente = ?""", (novo_numero, cpfcliente_cliente))
        conn.commit()
        lstClientes.delete(0, END)
        lista = cursor.execute("""
            SELECT * FROM Clientes;
            """)
        for i in lista:
            lstClientes.insert(END, i)

    def exportar1():
        with io.open('clientes.sql', 'w') as f:
            for linha in conn.iterdump():
                f.write('%s\n' % linha)
        cursor.execute("""
            SELECT * FROM clientes;
        """)
        with io.open('clientes.txt', 'w') as f:
            for linha in cursor.fetchall():
                linha = str(linha)
                f.write('%s\n' % linha)

    ### Widgets - Principal ###
    lblTitulo = Label(principal, text="SysShoes")
    lblNomeNumero = Label(principal, text="CPF / Nome / Numero")

    ### Widgets - Adicionar Cliente ###
    lblAdicionarCliente = Label(principal, text="Adicionar Cliente")
    lblCpfcliente = Label(principal, text="CPF: ")
    lblNomecliente = Label(principal, text="Nome do Cliente: ")
    lblNumero = Label(principal, text="Número do Cliente: ")
    etCpfcliente = Entry(principal)
    etNomecliente = Entry(principal)
    etNumero = Entry(principal)
    btnAdd = Button(principal, text="Adicionar", command=adicionar_cliente)

    ### Widgets - Deletar Cliente ###
    lblDeletarCliente = Label(principal, text="Deletar Cliente")
    lblCpfclienteDeletar = Label(principal, text="CPF: ")
    etCpfclienteDeletar = Entry(principal, width=10)
    btnDel = Button(principal, text="Deletar", command=deletar_cliente)

    ### Widgets - Mudar Numero ###
    lblMudarNumero = Label(principal, text="Mudar Numero")
    lblCpfclienteMudar = Label(principal, text="CPF: ")
    lblNovoNumero = Label(principal, text="Novo Numero: ")
    etCpfclienteMudar = Entry(principal)
    etNovoNumero = Entry(principal)
    btnMudarNumero = Button(principal, text="Mudar Numero", command=mudar_numero)

    ### Widgets - Listar Clientes ###
    scrollbar = Scrollbar(principal)
    lstClientes = Listbox(principal, width=35, height=16)
    lstClientes.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lstClientes.yview)
    lista = cursor.execute("""
        SELECT * FROM clientes;
        """)
    for i in lista:
        lstClientes.insert(END, i)

    ### Posicionamento de Widgets - Principal ###
    lblTitulo.place(x=10)
    lblNomeNumero.place(x=450, y=30)

    ### Posicionamento de Widgets - Listar Clientes ####
    lstClientes.place(x=450, y=60)
    scrollbar.place()

    ### Posicionamento de Widgets - Adicionar Cliente ###
    lblAdicionarCliente.place(x=10, y=30)
    lblCpfcliente.place(x=10, y=52)
    etCpfcliente.place(x=200, y=50)
    lblNomecliente.place(x=10, y=82)
    etNomecliente.place(x=200, y=80)
    lblNumero.place(x=10, y=112)
    etNumero.place(x=200, y=110)
    btnAdd.place(x=200, y=145)

    ### Posicionamento de Widgets - Deletar Cliente ###
    lblDeletarCliente.place(x=10, y=175)
    lblCpfclienteDeletar.place(x=10, y=200)
    etCpfclienteDeletar.place(x=200, y=200)
    btnDel.place(x=200, y=230)

    ### Posicionamento de Widgets - Mudar Numero ###
    lblMudarNumero.place(x=10, y=260)
    lblCpfclienteMudar.place(x=10, y=280)
    etCpfclienteMudar.place(x=200, y=280)
    lblNovoNumero.place(x=10, y=310)
    etNovoNumero.place(x=200, y=310)
    btnMudarNumero.place(x=200, y=340)

    principal.mainloop() 

if n == 'b':
    print("Digite a senha do administrador")
    m = input()
    if m == '12345':            
            ### Globais ###
        conn = sqlite3.connect("ppr.db")
        

        cursor = conn.cursor()

        def criarTabela2():
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS funcionarios (
                    cpffuncionario INTEGER NOT NULL PRIMARY KEY,
                    nomefuncionario TEXT NOT NULL,
                    numero INTEGER NOT NULL 
                ); 
            """) #definições das aplicações em banco de dados#

        criarTabela2()

        #### Definições da Aplicação Principal ###
        principal = Tk()
        principal.title("SysShoes - Adicionar Funcionario")
        principal.geometry("700x450")
        principal.resizable(TRUE, TRUE)

        #### Funções ###
        def adicionar_funcionario():
            cpffuncionario = etCpffuncionario.get()
            nomefuncionario = etNomefuncionario.get()
            numero = etNumero.get()
            cursor.execute("""
                INSERT INTO funcionarios (cpffuncionario, nomefuncionario, numero) VALUES (?, ?, ?)""", (cpffuncionario, nomefuncionario, numero))
            conn.commit()
            lstFuncionarios.insert(END, (cpffuncionario, nomefuncionario, numero))

        def deletar_funcionario():
            cpffuncionario_funcionario = etCpffuncionarioDeletar.get()
            cursor.execute("""
                DELETE FROM funcionarios WHERE cpffuncionario=?""", (cpffuncionario_funcionario,))
            conn.commit()
            lstFuncionarios.delete(0, END)
            lista = cursor.execute("""
                SELECT * FROM funcionarios;
                """)
            for i in lista:
                lstFuncionarios.insert(END, i)

        def mudar_numero():
            cpffuncionario_funcionario = etCpffuncionarioMudar.get()
            novo_numero = etNovoNumero.get()
            cursor.execute("""
                UPDATE funcionarios SET numero = ? WHERE cpffuncionario = ?""", (novo_numero, cpffuncionario_funcionario))
            conn.commit()
            lstFuncionarios.delete(0, END)
            lista = cursor.execute("""
                SELECT * FROM Funcionarios;
                """)
            for i in lista:
                lstFuncionarios.insert(END, i)

        def exportar2():
            with io.open('funcionarios.sql', 'w') as f:
                for linha in conn.iterdump():
                    f.write('%s\n' % linha)
            cursor.execute("""
                SELECT * FROM funcionarios;
            """)
            with io.open('funcionarios.txt', 'w') as f:
                for linha in cursor.fetchall():
                    linha = str(linha)
                    f.write('%s\n' % linha)

        ### Widgets - Principal ###
        lblTitulo = Label(principal, text="SysShoes")
        lblNomeNumero = Label(principal, text="CPF / Nome / Numero")

        ### Widgets - Adicionar Funcionario ###
        lblAdicionarFuncionario = Label(principal, text="Adicionar Funcionario")
        lblCpffuncionario = Label(principal, text="CPF: ")
        lblNomefuncionario = Label(principal, text="Nome do Funcionario: ")
        lblNumero = Label(principal, text="Número do Funcionario: ")
        etCpffuncionario = Entry(principal)
        etNomefuncionario = Entry(principal)
        etNumero = Entry(principal)
        btnAdd = Button(principal, text="Adicionar", command=adicionar_funcionario)

        ### Widgets - Deletar Funcionario ###
        lblDeletarFuncionario = Label(principal, text="Deletar Funcionario")
        lblCpffuncionarioDeletar = Label(principal, text="CPF: ")
        etCpffuncionarioDeletar = Entry(principal, width=10)
        btnDel = Button(principal, text="Deletar", command=deletar_funcionario)

        ### Widgets - Mudar Numero ###
        lblMudarNumero = Label(principal, text="Mudar Numero")
        lblCpffuncionarioMudar = Label(principal, text="CPF: ")
        lblNovoNumero = Label(principal, text="Novo Numero: ")
        etCpffuncionarioMudar = Entry(principal)
        etNovoNumero = Entry(principal)
        btnMudarNumero = Button(principal, text="Mudar Numero", command=mudar_numero)

        ### Widgets - Listar Funcionarios ###
        scrollbar = Scrollbar(principal)
        lstFuncionarios = Listbox(principal, width=35, height=16)
        lstFuncionarios.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lstFuncionarios.yview)
        lista = cursor.execute("""
            SELECT * FROM funcionarios;
            """)
        for i in lista:
            lstFuncionarios.insert(END, i)

        ### Posicionamento de Widgets - Principal ###
        lblTitulo.place(x=10)
        lblNomeNumero.place(x=450, y=30)

        ### Posicionamento de Widgets - Listar Funcionarios ####
        lstFuncionarios.place(x=450, y=60)
        scrollbar.place()

        ### Posicionamento de Widgets - Adicionar Funcionario ###
        lblAdicionarFuncionario.place(x=10, y=30)
        lblCpffuncionario.place(x=10, y=52)
        etCpffuncionario.place(x=200, y=50)
        lblNomefuncionario.place(x=10, y=82)
        etNomefuncionario.place(x=200, y=80)
        lblNumero.place(x=10, y=112)
        etNumero.place(x=200, y=110)
        btnAdd.place(x=200, y=145)

        ### Posicionamento de Widgets - Deletar Funcionario ###
        lblDeletarFuncionario.place(x=10, y=175)
        lblCpffuncionarioDeletar.place(x=10, y=200)
        etCpffuncionarioDeletar.place(x=200, y=200)
        btnDel.place(x=200, y=230)

        ### Posicionamento de Widgets - Mudar Numero ###
        lblMudarNumero.place(x=10, y=260)
        lblCpffuncionarioMudar.place(x=10, y=280)
        etCpffuncionarioMudar.place(x=200, y=280)
        lblNovoNumero.place(x=10, y=310)
        etNovoNumero.place(x=200, y=310)
        btnMudarNumero.place(x=200, y=340)

        principal.mainloop() 

    else:
        print("senha incorreta - acesso negado")


if n == 'c':
            ### Globais ###
    conn = sqlite3.connect("ppr.db")
    

    cursor = conn.cursor()

    def criarTabela3():
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                codigo INTEGER NOT NULL PRIMARY KEY,
                nome TEXT NOT NULL,
                tipo TEXT NOT NULL,
                tamanho INTEGER NOT NULL,
                cor TEXT NOT NULL,
                preco INTEGER NOT NULL 
            ); 
        """) #definições das aplicações em banco de dados#

    criarTabela3()

    #### Definições da Aplicação Principal ###
    principal = Tk()
    principal.title("SysShoes - Adicionar Produto")
    principal.geometry("1000x1000")
    principal.resizable(TRUE, TRUE)

    #### Funções ###
    def adicionar_produto():
        codigo = etCodigo.get()
        nome = etNome.get()
        tipo = etTipo.get()
        tamanho = etTamanho.get()
        cor = etCor.get()
        preco = etPreco.get()
        cursor.execute("""
            INSERT INTO produtos (codigo, nome, tipo, tamanho, cor, preco) VALUES (?, ?, ?, ?, ?, ?)""", (codigo, nome, tipo, tamanho, cor, preco))
        conn.commit()
        lstProdutos.insert(END, (codigo, nome, tipo, tamanho, cor, preco))

    def deletar_produto():
        codigo_produto = etCodigoDeletar.get()
        cursor.execute("""
            DELETE FROM produtos WHERE codigo=?""", (codigo_produto,))
        conn.commit()
        lstProdutos.delete(0, END)
        lista = cursor.execute("""
            SELECT * FROM produtos;
            """)
        for i in lista:
            lstProdutos.insert(END, i)

    def atualizar_produto():
        codigo_produto = etCodigoMudar.get()
        novo_nome = etNovoNome.get()
        novo_tipo = etNovoTipo.get()
        novo_tamanho = etNovoTamanho.get()
        nova_cor = etNovaCor.get()
        novo_preco = etNovoPreco.get()
        cursor.execute("""
            UPDATE produtos SET nome = ?, tipo = ?, tamanho = ?, cor = ?, preco = ? WHERE codigo = ?""", (novo_nome, novo_tipo, novo_tamanho, nova_cor, novo_preco,codigo_produto))
        conn.commit()
        lstProdutos.delete(0, END)
        lista = cursor.execute("""
            SELECT * FROM Produtos;
            """)
        for i in lista:
            lstProdutos.insert(END, i)

    def exportar3():
        with io.open('produtos.sql', 'w') as f:
            for linha in conn.iterdump():
                f.write('%s\n' % linha)
        cursor.execute("""
            SELECT * FROM produtos;
        """)
        with io.open('produtos.txt', 'w') as f:
            for linha in cursor.fetchall():
                linha = str(linha)
                f.write('%s\n' % linha)

    ### Widgets - Principal ###
    lblTitulo = Label(principal, text="SysShoes")
    lblNomeNumero = Label(principal, text="\t\t\t\tCodigo / Nome do produto / Tipo / Tamanho / Cor / Preço")

    ### Widgets - Adicionar Produto ###
    lblAdicionarProduto = Label(principal, text="Adicionar Produto")
    lblCodigo = Label(principal, text="Código do produto: ")
    lblNome = Label(principal, text="Nome do produto: ")
    lblTipo = Label(principal, text="Tipo do produto: ")
    lblTamanho = Label(principal, text="Tamanho: ")
    lblCor = Label(principal, text="Cor: ")
    lblPreco = Label(principal, text="Preço: ")
    etCodigo = Entry(principal)
    etNome = Entry(principal)
    etTipo = Entry(principal)
    etTamanho = Entry(principal)
    etCor = Entry(principal)
    etPreco = Entry(principal)
    btnAdd = Button(principal, text="Adicionar", command=adicionar_produto)

    ### Widgets - Deletar Produto ###
    lblDeletarProduto = Label(principal, text="Deletar Produto")
    lblCodigoDeletar = Label(principal, text="Código do produto: ")
    etCodigoDeletar = Entry(principal,  width=10)
    btnDel = Button(principal, text="Deletar", command=deletar_produto)

    ### Widgets - Atualizar produto ###
    lblAtualizarProduto = Label(principal, text="Atualizar Produto")
    lblCodigoMudar = Label(principal, text="Código: ")
    lblNovoNome = Label(principal, text="Novo Nome do produto: ")
    lblNovoTipo = Label(principal, text="Novo Tipo: ")
    lblNovoTamanho = Label(principal, text="Novo Tamanho: ")
    lblNovaCor = Label(principal, text="Nova Cor: ")
    lblNovoPreco = Label(principal, text="Novo Preço: ")
    etCodigoMudar = Entry(principal)
    etNovoNome = Entry(principal)
    etNovoTipo = Entry(principal)
    etNovoTamanho = Entry(principal)
    etNovaCor = Entry(principal)
    etNovoPreco = Entry(principal)
    btnAtualizarProduto = Button(principal, text="Atualizar Produto", command=atualizar_produto)

    ### Widgets - Listar Produtos ###
    scrollbar = Scrollbar(principal)
    lstProdutos = Listbox(principal, width=50, height=30)
    lstProdutos.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lstProdutos.yview)
    lista = cursor.execute("""
        SELECT * FROM produtos;
        """)
    for i in lista:
        lstProdutos.insert(END, i)

    ### Posicionamento de Widgets - Principal ###
    lblTitulo.place(x=275)
    lblNomeNumero.place(x=308, y=30)

    ### Posicionamento de Widgets - Listar Produtos ####
    lstProdutos.place(x=500, y=52)
    scrollbar.place()

    ### Posicionamento de Widgets - Adicionar Produto ###
    lblAdicionarProduto.place(x=200, y=30)
    lblCodigo.place(x=10, y=52)
    etCodigo.place(x=200, y=50)
    lblNome.place(x=10, y=82)
    etNome.place(x=200, y=80)
    lblTipo.place(x=10, y=112)
    etTipo.place(x=200, y=110)
    lblTamanho.place(x=10, y=142)
    etTamanho.place(x=200, y=140)
    lblCor.place(x=10, y=172)
    etCor.place(x=200, y=170)
    lblPreco.place(x=10, y=202)
    etPreco.place(x=200, y=200)
    btnAdd.place(x=200, y=230)

    ### Posicionamento de Widgets - Deletar Produto ###
    lblDeletarProduto.place(x=200, y=280)
    lblCodigoDeletar.place(x=10, y=300)
    etCodigoDeletar.place(x=200, y=300)
    btnDel.place(x=200, y=330)

    ### Posicionamento de Widgets - Atualizar Produto ###
    lblAtualizarProduto.place(x=200, y=390)
    lblCodigoMudar.place(x=10, y=420)
    etCodigoMudar.place(x=200, y=420)
    lblNovoNome.place(x=10, y=450)
    etNovoNome.place(x=200, y=450)
    lblNovoTipo.place(x=10, y=480)
    etNovoTipo.place(x=200, y=480)
    lblNovoTamanho.place(x=10, y=510)
    etNovoTamanho.place(x=200, y=510)
    lblNovaCor.place(x=10, y=540)
    etNovaCor.place(x=200, y=540)
    lblNovoPreco.place(x=10, y=570)
    etNovoPreco.place(x=200, y=570)
    btnAtualizarProduto.place(x=200, y=600)



    principal.mainloop() 

if n == 'd':
            ### Globais ###
    
    conn = sqlite3.connect("ppr.db")
    
    cursor = conn.cursor()

    def criarTabela4():
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendas (
                codvenda INTEGER NOT NULL PRIMARY KEY,
                cpffuncionario INTEGER NOT NULL,
                cpfcliente INTEGER NOT NULL,
                codigo INTEGER NOT NULL    
            ); 
        """) #definições das aplicações em banco de dados#

    criarTabela4()

    #### Definições da Aplicação Principal ###
    principal = Tk()
    principal.title("SysShoes - Realizar Venda")
    principal.geometry("1000x450")
    principal.resizable(TRUE, TRUE)

    #### Funções ###
    def realizar_venda():
        codvenda = randint(0,1000)
        cpffuncionario = etCpffuncionario.get()
        cpfcliente = etCpfcliente.get()
        codigo = etCodigo.get()
        cursor.execute("""
            INSERT INTO vendas (codvenda, cpffuncionario, cpfcliente, codigo) VALUES (?, ?, ?, ?)""", (codvenda, cpffuncionario, cpfcliente, codigo))
        conn.commit()
        lstVendas.insert(END, (codvenda, cpffuncionario, cpfcliente, codigo))
        cursor.execute("""
            DELETE FROM produtos WHERE codigo=?""", (codigo,))
        conn.commit()
        lstProdutos.delete(0, END)
        lista = cursor.execute("""
            SELECT * FROM produtos;
            """)
        for i in lista:
            lstProdutos.insert(END, i)

    def exportar4():
        with io.open('vendas.sql', 'w') as f:
            for linha in conn.iterdump():
                f.write('%s\n' % linha)
        cursor.execute("""
            SELECT * FROM vendas;
        """)
        with io.open('vendas.txt', 'w') as f:
            for linha in cursor.fetchall():
                linha = str(linha)
                f.write('%s\n' % linha)
        
        with io.opne('produtos.sql', 'w') as f:
            for linha in conn.iterdump():
                f.write('%s\n' % linha)
            cursor.execute("""
                SELECT * FROM produtos;
            """)
        with io.open('produtos.txt', 'w') as f:
            for linha in cursor.fetchall():
                linha = str(linha)
                f.write('%s\n' % linha)

    ### Widgets - Principal ###
    lblTitulo = Label(principal, text="SysShoes")
    lblNomeNumero = Label(principal, text="\t\t\t\tCodigo da venda / CPF Funcionário / CPF Cliente / Código Produto")

    ### Widgets - Realizar Venda ###
    lblRealizarVenda = Label(principal, text="Realizar Venda")
    lblCodvenda = Label(principal, text="Código da Venda: ")
    lblCpffuncionario = Label(principal, text="CPF do Funcionário: ")
    lblCpfcliente = Label(principal, text="CPF do Cliente: ")
    lblCodigo = Label(principal, text="Código do Produto: ")
    etCodvenda = Entry(principal)
    etCpffuncionario = Entry(principal)
    etCpfcliente = Entry(principal)
    etCodigo = Entry(principal)
    btnAdd = Button(principal, text="Vender", command=realizar_venda)

    ### Widgets - Listar Vendas ###
    scrollbar = Scrollbar(principal)
    lstVendas = Listbox(principal, width=70, height=15)
    lstVendas.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lstVendas.yview)
    lista = cursor.execute("""
        SELECT * FROM vendas;
        """)
    for i in lista:
        lstVendas.insert(END, i)

    ### Posicionamento de Widgets - Principal ###
    lblTitulo.place(x=10)
    lblNomeNumero.place(x=220, y=30)

    ### Posicionamento de Widgets - Listar Produtos ####
    lstVendas.place(x=400, y=60)
    scrollbar.place()

    ### Posicionamento de Widgets - Realizar Venda ###
    lblRealizarVenda.place(x=10, y=30)
    lblCodvenda.place(x=10, y=52)
    etCodvenda.place(x=200, y=50)
    lblCpffuncionario.place(x=10, y=82)
    etCpffuncionario.place(x=200, y=80)
    lblCpfcliente.place(x=10, y=112)
    etCpfcliente.place(x=200, y=110)
    lblCodigo.place(x=10, y=142)
    etCodigo.place(x=200, y=140)
    btnAdd.place(x=200, y=170)

    principal.mainloop()     
  


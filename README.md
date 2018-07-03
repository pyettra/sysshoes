# sysshoes

Projeto do software SysShoes para gerenciamento de loja de calçados :shoe: :sandal: :boot: :high_heel:.

SysShoes is a software project for shoes store's management :shoe: :sandal: :boot: :high_heel:.


## Instruções do projeto

O objetivo deste trabalho é desenvolver as diversas competências técnicas necessárias para o projeto de programas de computador. O sistema a ser desenvolvido será um sistema de gestão para uma loja de sapatos, o qual foi denominado de SysShoes. O SysShoes deve permitir que um funcionário da loja possa registrar as vendas realizadas, cadastrar novos clientes, controlar o estoque de produtos, além de demais funcionalidades necessárias para a gestão da loja.

## Project's instructions

The main goal in this project is to develop the many technical skills wanted for this software. The software we are up to develop will assist the shoe store's management, which we have given the name SysShoes. SysShoes will allow that an employee adds sales status, records new clients, new products and any other required features. 

## Requisitos do software

A implementação desse software conta com alguns requisitos essencias. Dentre eles, temos:

### Gerenciamento de Clientes :person_with_blond_hair:
  Realização de cadastros de clientes. O usuário deve entrar com o nome, CPF e número de telefone do cliente para cadastrá-lo. A chave primária para identificação do cliente é o CPF, que é também único. O usuário poderá também editar o número de telefone do cliente, fornecendo seu CPF. É possível também excluir clientes já cadastrados, também fornecendo o CPF. Essa função de gerenciamento dos clientes é permitida tanto para funcionários quanto administradores da loja.
  
### Gerenciamento de Funcionários :construction_worker:
   Realização de cadastros de funcionários. O usuário deve entrar com o nome, CPF e número de telefone do funcionário para cadastrá-lo. A chave primária para identificação do funcionário é o CPF, que é também único. O usuário poderá também editar o número de telefone do funcionário, fornecendo seu CPF. É possível também excluir funcionários já cadastrados, também fornecendo o CPF. Essa função de gerenciamento dos funcionários é permitida apenas para administradores da loja, sendo necessária uma senha de acesso ao Gerenciamento de Funcionários.
   
### Gerenciamento de Produtos :high_heel:
   Realização de cadastros de produtos. O usuário deve entrar com o código, nome, tipo, tamanho, cor e preço do produto para cadastrá-lo. A chave primária para identificação do produto é o código, que é também único. O usuário poderá também editar todos os campos do produto, fornecendo seu código. É possível também excluir produtos já cadastrados, também fornecendo o código. Essa função de gerenciamento dos produtos é permitida tanto para funcionários quanto administradores da loja.
  
### Gerenciamento de Vendas :package:
  Realização de vendas de produtos. O usuário deve entrar com o código de venda, CPF do funcionário, CPF do cliente e código do produto a ser vendido. Essa função automaticamente retira do estoque de produtos aquele produto que foi vendido e é uma função executada tanto por administradores quanto funcionários.
  
## Software requirements

This software development involves some essential requeriments. Among them, we have:

### Client's Management :person_with_blond_hair:
  Manipulate clients data. The user must provide name, CPF and cellphone number in order to add a new client. The primary key is the client's CPF, which is unique. Also, the user will be able to edit the clients data, by providing the CPF. Further more, the user can delete clients by also providing a specific CPF. This function is open for both types of user: employees and administrators.
  
### Employee's Management :construction_worker:
 Manipulate employees data. The user must provide name, CPF and cellphone number in order to add a new employee. The primary key is the employee's CPF, which is unique. Also, the user will be able to edit the employees data, by providing the CPF. Further more, the user can delete employees by also providing a specific CPF. This function is only avaliable for administrators, and they must provide the correct password to acess employee's management.
 
 ### Product's Management :high_heel:
  Manipulate products data. The user must provide a code, name, type, size, colour and price in order to add a new product. The primary key is the product's code, which is unique. Also, the user will be able to edit the products data, by providing the specific code. Further more, the user can delete products by providing a specific code. This function is open for both types of user: employees and administrators.
  
### Sale's Management :package:
  Manipulate sales data. The user must provide the sale's code, employee's CPF, client's CPF and product's code to be sold. This function will delete the product from products database, by default. Further more, this function is avaliable for both employees and administrators.
  
## Implementação :computer:
  Para realizar a implementação, utilizei a linguagem Python na versão 3.6.5. O editor de código utilizado foi o Visual Studio Code. A principal biblioteca utilizada para manipulação de banco de dados foi a sqlite 3. Para mais informações e downloads dos instrumentos utilizados, temos:
  
  ### Python 3.6.5
  - [Informações e download do python](https://www.python.org/downloads/release/python-365/)
  
  ### Visual Studio Code
  - [Informações e download do VSCode](https://code.visualstudio.com)
  
  ### sqlite 3
  - [Informações do sqlite3 para Python](http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html)
  
  
  ## Implementation :computer:
   In order to put in practice our code, I've used 3.6.5 Python's version and Visual Studio Code as my code editor. Also, I've been working with a special database library, sqlite3 for Python. For more informations and downloads, we have:
   
   ### Python 3.6.5
   - [Informations and download](https://www.python.org/downloads/release/python-365/)
   
   ### Visual Studio Code
   - [Informations and download](https://code.visualstudio.com)
  
   ### sqlite3 
   - [Informations about sqlite3 for Python](https://docs.python.org/2/library/sqlite3.html) 
  

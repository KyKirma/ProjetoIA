#Criando uma classe - um novo tipo de dados. No nosso caso a Classe
#tem o nome de Cliente e possuí quatro atributos(características)
#cpf,nome,idade,telefone.
class Cliente:
    #Método Construtor chamado __init__. É o método responsável por
    #reservar o espaço na memória no momento que uma variável(objeto
    #ou instância da classe) é criada. No nosso caso além dos quatro
    #atributos recebe como parâmetro o atributo self. Que faz referência
    #a variável que será criada.
    def __init__(self,cpf,nome,idade,telefone):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

#Variável opção irá controlar o while que regula o menu. Inicialmente ele
#deve possuir qualquer valor diferente de 5, para que o menu seja executado
#pelo menos uma vez
opção = 0
#Variável que armazena a lista de clientes. Inicialmente acresentamos 4
# clientes na nossa lista: Rodrigo, Ricardo, Ana e Letícia.
#clientes = ["Rodrigo", "Ricardo", "Ana", "Letícia"]
#Novo maneira de inicializar a lista de clientes. Ao invés de fixarmos
#a lista de clientes. Iremos fazer a leitura desse dados de um arquivo de
#texto.
#Criamos uma lista de Clientes Vazia - sem nenhum cliente
clientes = []
#O comando open abre um arquivo e lê o mesmo. O comando possui dois parametros
#Endereço do Arquivo no HD - C:/Users/29963905803/Documents/clientes.txt no
#nosso caso. E o segundo parametro indica o que poderemos fazer no arquivo
#No nosso caso o parâmetro é o "r" - que indica que apenas iremos ler o
#o arquivo
arquivo = open("C:/Users/29963905803/Documents/clientes.txt", "r")
contadorDelinha = 0
#Percorre todas as linhas do arquivo através do comando readlines()
for linha in arquivo.readlines():
    #Cada linha do nosso arquivo indica o nome de um cliente.
    #Dessa forma iremos acrescentar cada linha do arquivo na lista
    #de cliente atráves do comando Append
    #O arquivo traz consigo as quebras de linha. Por isso utilizamos
    # o comando strip para retirar as quebras de linha.
    if(contadorDelinha%4==0):
        cpf = linha.strip('\n')
    elif(contadorDelinha%4==1):
        nome = linha.strip('\n')
    elif(contadorDelinha%4==2):
        idade = linha.strip('\n')
    elif(contadorDelinha%4==3):
        telefone = linha.strip('\n')
        novoCliente = Cliente(cpf,nome,idade,telefone)
        clientes.append(novoCliente)
    contadorDelinha = contadorDelinha + 1
#Fecha o arquivo após extrair todos os dados nele existentes.
arquivo.close()

#Início do Menu. O while regula o menu. Enquanto o usuário não digitar
#a opção 5. O programa irá ficar em execução.
while(opção!=5):
    #Sequência de 6 comandos print que irão imprimir o menu enquanto o usuário
    #não digitar a opção 5.
    print("Sistema do Supermercado")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3- Alterar Cliente")
    print("4 - Remover Cliente")
    print("5 - Sair")
    #Entrada de Dados. Nesse ponto do programa o comando input irá ler
    #através do teclado a opção que o usuário deseja executar.
    opção = int(input("Digite a opção desejada: "))
    #Estrutura Condicional que irá direcionar o programa para a opção
    #escolhida pelo usuário.
    if(opção==1):
        #Opção realiza o cadastro do Cliente
        print("Você escolheu a opção 1 - Cadastrar Cliente")
        #Leitura do nome do novo cliente via teclado através do comando
        #input, o novo cliente ficará armazenado na variável nome
        nome = input("Entre com o nome do novo cliente: ")
        cpf = input("Entre com o CPF do novo cliente: ")
        idade = input("Entre com a idade do novo cliente: ")
        telefone = input("Entre com o telefone do novo cliente: ")
        novoCliente = Cliente(cpf,nome,idade,telefone)
        #O Comando append inclui um novo cliente(variável nome)
        # na lista de clientes
        clientes.append(novoCliente)
    elif(opção==2):
        #Opção realiza a listagem dos clientes cadastrados no supermercado
        print("Você escolheu a opção 2 - Listar Clientes")
        #O Comando for irá percorrer a lista de clientes e o comando print
        #irá imprimir cada um dos clientes cadastrados
        for i in clientes:
            #Impressão de cada um dos clientes.
            print("Nome: ", i.nome)
            print("CPF: ", i.cpf)
            print("Idade: ", i.idade)
            print("Telefone: ", i.telefone)

    elif(opção==3):
        #Opção que realiza a alteração do nome de um cliente
        #já cadastrado
        print("Você escolheu a opção 3 - Alterar Cliente")
        # Inicialmente o sistema imprime os clientes cadastrados para que o
        # usuário possa escolher qual cliente irá remover.
        print("Clientes:")
        for i in clientes:
            print("Nome: ", i.nome)
            print("CPF: ", i.cpf)
            print("Idade: ", i.idade)
            print("Telefone: ", i.telefone)

        #Perguntar ao usuário qual cliente ele deseja alterar.
        nome = input("Digite o nome do cliente que você deseja alterar: ")
        #Sabendo o cliente que queremos alterar iremos retirar o mesmo da lista
        #de clientes
        for cliente in clientes:
            if (cliente.nome == nome):
                clientes.remove(cliente)
        #Perguntar ao usúário o novo nome do cliente.
        nome = input("Digite o novo nome do cliente: ")
        cpf = input("Digite o CPF do cliente: ")
        idade = input("Digite a idade do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        novoCliente = Cliente(cpf,nome,idade,telefone)
        #Inserir o novo nome do cliente na lista de clientes.
        clientes.append(novoCliente)
    elif(opção==4):
        #Opção que realiza a remoção de um cliente cadastrado
        print("Você escolheu a opção 4 - Remover Cliente")
        #Inicialmente o sistema imprime os clientes cadastrados para que o
        #usuário possa escolher qual cliente irá remover.
        print("Clientes:")
        for i in clientes:
            print("Nome: ", i.nome)
        #Após a impressão dos clientes cadastrados o Sistema pergunta o
        #nome do cliente que será removido e armazena o mesmo na variável nome
        nome = input("Entre com o nome do cliente que você quer remover:")
        #O comando remove irá remover o nome da lista de clientes
        for cliente in clientes:
            if (cliente.nome == nome):
                clientes.remove(cliente)

    elif(opção==5):
        #Impressão da Saída do Sistema - após o usuário "escolher" a opção 5
        print("Você escolheu a opção 5 - Sair")
    else:
        #Impressão da mensagem de opção inválida. Caso o usuário digite
        #um número fora do intervalo do menu(1 a 5).
        print("Você escolheu uma opção inválida")

#Após a finalização do sistema pelo usuário. Ou seja após o usuário escolher
#a opção 5, devemos gravar as informações no arquivo novamente.
arquivo = open("C:/Users/29963905803/Documents/clientes.txt", "w")
#Percorre a lista de clientes
for i in clientes:
    #Acrescenta o cliente ao arquivo final
    arquivo.write(i.cpf+'\n')
    arquivo.write(i.nome + '\n')
    arquivo.write(i.idade + '\n')
    arquivo.write(i.telefone + '\n')
#Fecha o Arquivo
arquivo.close()
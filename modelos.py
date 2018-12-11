from datetime import *


class Pessoa:
    def __init__(self, nome, data_de_nascimento):
        self.__nome = nome
        self.__data_de_nascimento = datetime.strptime(data_de_nascimento, '%d-%m-%Y')

    @property
    def nome(self):
        return self.__nome

    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento):
        self.__data_de_nascimento = datetime.strptime(data_de_nascimento, '%d %b %Y')

    def __str__(self):
        return f'Nome: {self.nome}, Data de nascimento: {self.data_de_nascimento}'


class Funcionario(Pessoa):
    def __init__(self, nome, data_de_nascimento, salario, nome_de_usuario, senha):
        super().__init__(nome, data_de_nascimento)
        self.__salario = float(salario)
        self.__nome_de_usuario = nome_de_usuario
        self.__senha = senha

    @property
    def salario(self):
        return self.__salario

    @property
    def nome_de_usuario(self):
        return self.__nome_de_usuario

    @property
    def senha(self):
        return self.__senha

    @salario.setter
    def salario(self, salario):
        self.__salario = float(salario)

    @nome_de_usuario.setter
    def nome_de_usuario(self, nome_de_usuario):
        self.nome_de_usuario = nome_de_usuario

    @senha.setter
    def senha(self, senha):
        self.senha = senha

    def __str__(self):
        return f'Nome: {self.nome}, Data de nascimento: {self.data_de_nascimento}, ' \
               f'Salario: {self.salario}, Usuario: {self.nome_de_usuario} '


class Gerente(Funcionario):
    def __init__(self, nome, data_de_nascimento, salario, nome_de_usuario, senha, matricula):
        super().__init__(nome, data_de_nascimento, salario, nome_de_usuario, senha)
        self.__matricula = matricula
        self.__menu = ('cirurgias', 'salas', 'gerentes', 'medicos', 'clientes')

    @property
    def matricula(self):
        return self.__matricula

    @property
    def menu(self):
        return self.__menu

    def __str__(self):
        return f'Nome: {self.nome}, Data de nascimento: {self.data_de_nascimento}, ' \
               f'Salario: {self.salario}, Usuario: {self.nome_de_usuario}, Matricula: {self.matricula} '


class Medico(Funcionario):
    def __init__(self, nome, data_de_nascimento, salario, nome_de_usuario, senha, crm):
        super().__init__(nome, data_de_nascimento, salario, nome_de_usuario, senha)
        self.__crm = crm
        self.__lista_de_clientes = []
        self.__menu = ('cirurgias', 'clientes')

    @property
    def crm(self):
        return self.__crm

    @property
    def menu(self):
        return self.__menu

    @property
    def lista_de_clientes(self):
        return self.__lista_de_clientes

    def adicionar_cliente(self, cliente):
        self.__lista_de_clientes.append(cliente.cpf)

    def remover_cliente(self, cliente):
        self.__lista_de_clientes.remove(cliente.cpf)

    def __str__(self):
        return f'Nome: {self.nome}, Data de nascimento: {self.data_de_nascimento}, ' \
               f'Salario: {self.salario}, Usuario: {self.nome_de_usuario},' \
               f' CRM: {self.crm}'


class Cliente(Pessoa):
    def __init__(self, nome, data_de_nascimento, cpf):
        super().__init__(nome, data_de_nascimento)
        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    def __str__(self):
        return f'Nome: {self.nome}, Data de nascimento: {self.data_de_nascimento}, CPF: {self.cpf}'


class Sala:
    def __init__(self, numero, andar):
        self.__numero = int(numero)
        self.__andar = int(andar)
        self.__id = str(numero) + str(andar)

    @property
    def numero(self):
        return self.__numero

    @property
    def andar(self):
        return self.__andar

    @property
    def id(self):
        return self.__id

    @numero.setter
    def numero(self, numero):
        self.__numero = int(numero)
        self.__id = str(numero) + str(self.__andar)

    @andar.setter
    def andar(self, andar):
        self.__andar = int(andar)
        self.__id = str(self.__numero) + str(andar)


class Cirurgia:
    def __init__(self, cliente, medico, sala, data, hora):
        self.__cliente = cliente
        self.__medico = medico
        self.__sala = sala
        self.__hora = datetime.strptime(hora, '%H:%M').time()
        self.__data = datetime.strptime(data, '%d-%m-%Y')
        self.__feedback = ''
        self.__id = None

    def dar_feedback(self, feedback):
        self.__feedback = feedback

    @property
    def id(self, id):
        return self.__id

    @property
    def feedback(self):
        return self.__feedback

    @property
    def cliente(self):
        return self.__cliente

    @property
    def medico(self):
        return self.__medico

    @property
    def sala(self):
        return self.__sala

    @property
    def hora(self):
        return self.__hora

    @property
    def data(self):
        return self.__data

    @property
    def feedback(self):
        return self.__feedback

    @property
    def id(self):
        return self.__id

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @medico.setter
    def medico(self, medico):
        self.__medico = medico

    @sala.setter
    def sala(self, sala):
        self.__sala = sala

    @hora.setter
    def hora(self, hora):
        self.__hora = time.strftime(hora, '%I:%M')

    @data.setter
    def data(self, data):
        self.__data = date.strftime(data, '%d %b %Y')

    @id.setter
    def id(self, id):
        self.__id = id

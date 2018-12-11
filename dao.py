from modelos import *

CRIA_MEDICO = 'INSERT INTO Medico (nome, data_de_nascimento, salario, nome_de_usuario, senha, crm) VALUES (%s, %s, %s,%s, %s, %s)'
CRIA_CLIENTE = 'INSERT INTO Cliente (nome, data_de_nascimento, cpf) VALUES (%s, %s, %s);'
CRIA_CIRURGIA = 'INSERT INTO Cirurgia (cliente, medico, sala, data, hora, feedback) VALUES (%s, %s, %s,%s, %s, %s)'
CRIA_SALA = 'INSERT INTO Sala (andar, numero, id) VALUES (%s, %s, %s) '

MODIFICA_MEDICO = 'UPDATE Medico SET nome=%s, data_de_nascimento=%s, salario=%s, nome_de_usuario=%s , senha=%s , crm=%s WHERE crm=%s'
MODIFCA_CLIENTE = 'UPDATE Cliente SET nome=%s, data_de_nascimento=%s, cpf=%s WHERE cpf=%s;'
MODIFICA_CIRURGIA = 'UPDATE Cirurgia SET cliente=%s, medico=%s, sala=%s, data=%s, hora=%s, feedback=%s WHERE id=%s '
MODIFCA_SALA = 'UPDATE Sala SET numero=%s, andar=%s , id=%s WHERE id=%s;'

LISTAR_MEDICO = 'SELECT  nome, data_de_nascimento, salario , nome_de_usuario, senha, crm FROM Medico'
LISTAR_CLIENTE = 'SELECT nome, data_de_nascimento, cpf FROM Cliente'
LISTAR_CIRURGIA = 'SELECT cliente , medico, sala, data, hora, feedback, id from Cirurgia'
LISTAR_GERENTE = 'SELECT nome, nome_de_usuario, matricula FROM Gerente'
LISTAR_SALA = 'SELECT  numero, andar, id FROM Sala'

BUSCA_MEDICO = 'SELECT  nome, data_de_nascimento, salario , nome_de_usuario, senha, crm FROM Medico WHERE nome_de_usuario=%s'
BUSCA_GERENTE = 'SELECT nome, data_de_nascimento, salario, nome_de_usuario, senha, matricula FROM Gerente WHERE  nome_de_usuario=%s'

DELETA_MEDICO = 'DELETE FROM Medico WHERE crm=%s'
DELETA_CLIENTE = 'DELETE FROM Cliente WHERE cpf=%s'
DELETE_CIRURGIA = 'DELETE FROM Cirurgia WHERE id=%s'
DELETA_SALA = 'DELETE FROM Sala WHERE id=%s'

DAR_FEEDBACK = 'UPDATE Cirurgia SET feedback=%s WHERE id=%s '
MUDAR_SALA = 'UPDATE Cirurgia SET sala=%s WHERE id=%s)'
ADICIONAR_A_LISTA = 'INSERT INTO Lista_de_clientes (medico_crm, cliente_cpf) VALUE (%s, %s)'
RETORNA_DA_LISTA = 'SELECT  medico_crm, cliente_cpf FROM Lista_de_clientes WHERE medico_crm=%s'


class ClienteDao:
    def __init__(self, db):
        self.__db = db

    def criar_cliente(self, cliente, medico):
        cursor = self.__db.connection.cursor()
        cursor.execute(CRIA_CLIENTE, (cliente.nome, cliente.data_de_nascimento, cliente.cpf))
        self.__db.connection.commit()

        cursor.execute(ADICIONAR_A_LISTA, medico.crm, cliente.cpf)
        self.__db.connection.commit()

    def atualiza_cliente(self, cliente):
        cursor = self.__db.connection.cursor()
        cursor.execute(MODIFCA_CLIENTE, ((cliente.nome, cliente.data_de_nascimento, cliente.cpf, cliente.cpf)))
        self.__db.connection.commit()

    def lista_cliente(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(LISTAR_CLIENTE)
        clientes = traduz_clientes(cursor.fetchall())
        return clientes

    def deleta_cliente(self, cpf):
        cursor = self.__db.connection.cursor()
        cursor.execute(DELETA_CLIENTE, cpf)
        self.__db.connection.commit()


class GerenteDao:
    def __init__(self, db):
        self.__db = db

    def lista_gerente(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(LISTAR_GERENTE)
        gerentes = traduz_gerente(cursor.fetchall())
        return gerentes

    def busca_por_nome_de_usuario(self, nome_de_usuario):
        cursor = self.__db.connection.cursor()
        cursor.execute(BUSCA_GERENTE, (nome_de_usuario))
        tupla = cursor.fetchone()
        return traduz_gerente(tupla)


class MedicoDao:
    def __init__(self, db):
        self.__db = db

    def busca_por_nome_de_usuario(self, nome_de_usuario):
        cursor = self.__db.connection.cursor()
        cursor.execute(BUSCA_MEDICO, (nome_de_usuario))
        tupla = cursor.fetchone()
        return traduz_medico(tupla)

    def criar_medico(self, medico):
        cursor = self.__db.connection.cursor()
        cursor.execute(CRIA_MEDICO, medico.nome, medico.data_de_nascimento, medico.salario,
                       medico.nome_de_usuario, medico.senha, medico.crm)
        self.__db.connection.commit()

    def atualiza_medico(self, medico):
        cursor = self.__db.connection.cursor()
        cursor.execute(MODIFICA_MEDICO, medico.nome, medico.data_de_nascimento, medico.salario,
                       medico.nome_de_usuario, medico.senha, medico.crm, medico.crm)
        self.__db.connection.commit()

    def lista_medico(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(LISTAR_MEDICO)
        medicos = traduz_medicos(cursor.fetchall())
        return medicos

    def deleta_medico(self, crm):
        cursor = self.__db.connection.cursor()
        cursor.execute(DELETA_MEDICO, crm)
        self.__db.connection.commit()

    def dar_feedback(self, feedback):
        cursor = self.__db.connection.cursor()
        cursor.execute(DAR_FEEDBACK, feedback)
        self.__db.connection.commit()

    def mudar_sala(self, sala):
        cursor = self.__db.connection.cursor()
        cursor.execute(MUDAR_SALA, sala.id)
        self.__db.connection.commit()


class CirurgiaDao:
    def __init__(self, db):
        self.__db = db

    def criar_cirurgia(self, cirurgia):
        cursor = self.__db.connection.cursor()
        cursor.execute(CRIA_CIRURGIA, cirurgia.cliente, cirurgia.medico,
                       cirurgia.sala, cirurgia.data,
                       cirurgia.hora, cirurgia.feedback)
        self.__db.connection.commit()

    def atualiza_cirurgia(self, cirurgia):
        cursor = self.__db.connection.cursor()
        cursor.execute(MODIFICA_CIRURGIA, cirurgia.cliente, cirurgia.medico,
                       cirurgia.sala, cirurgia.data,
                       cirurgia.hora, cirurgia.feedback, cirurgia.id)
        self.__db.connection.commit()

    def lista_cirurgia(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(LISTAR_CIRURGIA)
        cirurgias = traduz_cirurgias(cursor.fetchall())
        return cirurgias

    def deleta_cirurgia(self, cirurgia):
        cursor = self.__db.connection.cursor()
        cursor.execute(DELETE_CIRURGIA, cirurgia.id)
        self.__db.connection.commit()


class SalaDao:
    def criar_sala(self, sala):
        cursor = self.__db.connection.cursor()
        cursor.execute(CRIA_SALA, sala.andar, sala.numero, sala.id)
        self.__db.connection.commit()

    def atualiza_sala(self, sala):
        cursor = self.__db.connection.cursor()
        cursor.execute(MODIFCA_SALA, sala.andar, sala.numero, sala.id)
        self.__db.connection.commit()

    def lista_sala(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(LISTAR_SALA)
        salas = traduz_salas(cursor.fetchall())
        return salas

    def deleta_sala(self, sala):
        cursor = self.__db.connection.cursor()
        cursor.execute(DELETA_SALA, sala.id)
        self.__db.connection.commit()


def traduz_cliente(tupla):
    return Cliente(tupla[0], tupla[1], tupla[2])


def traduz_clientes(clientes):
    return list(map(traduz_cliente, clientes))


def traduz_gerente(tupla):
    return Gerente(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5])


def traduz_gerentes(gerente):
    return list(map(traduz_gerente, gerente))


def traduz_medico(tupla):
    return Medico(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5])


def traduz_medicos(medicos):
    return list(map(traduz_medico, medicos))


def traduz_cirurgia(tupla):
    criada = Cirurgia(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5])
    criada.id = tupla[6]
    return criada


def traduz_cirurgias(cirurgias):
    return list(map(traduz_cirurgia, cirurgias))


def traduz_sala(tupla):
    return Sala(tupla[0], tupla[1])


def traduz_salas(salas):
    return list(map(traduz_sala, salas))

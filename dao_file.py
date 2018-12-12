import pickle


def salva_clientes(lista_clientes):
    with open("dao/cliente_lista.txt", "wb") as fp:
        pickle.dump(lista_clientes, fp)


def carrega_clientes():
    with open("dao/cliente_lista.txt", "rb") as fp:
        return pickle.load(fp)


def salva_medicos(lista_medicos):
    with open("dao/medicos_lista.txt", "wb") as fp:
        pickle.dump(lista_medicos, fp)


def carrega_medicos():
    with open("dao/medicos_lista.txt", "rb") as fp:
        return pickle.load(fp)


def salva_gerentes(lista_gerentes):
    with open("dao/gerentes_lista.txt", "wb") as fp:
        pickle.dump(lista_gerentes, fp)


def carrega_gerentes():
    with open("dao/gerentes_lista.txt", "rb") as fp:
        return pickle.load(fp)


def salva_salas(lista_salas):
    with open("dao/salas_lista.txt", "wb") as fp:
        pickle.dump(lista_salas, fp)


def carrega_salas():
    with open("dao/salas_lista.txt", "rb") as fp:
        return pickle.load(fp)


def salva_cirurgias(lista_cirurgias):
    with open("dao/cirurgias_lista.txt", "wb") as fp:
        pickle.dump(lista_cirurgias, fp)


def carrega_cirurgias():
    with open("dao/cirurgias_lista.txt", "rb") as fp:
        return pickle.load(fp)

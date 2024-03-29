from flask import Flask, render_template, request, redirect, session, url_for, flash, sessions
from modelos import Cliente, Medico, Gerente, Sala, Cirurgia
from dao_file import *
import secrets


app = Flask(__name__)
app.secret_key = secrets.secret_key

lista_clientes = carrega_clientes()
lista_medicos = carrega_medicos()
lista_gerentes = carrega_gerentes()
lista_salas = carrega_salas()
lista_cirurgias = carrega_cirurgias()



@app.route('/')
def login():  # Tela de login que vai confimar se é um Médico ou Gerente, e setar na sessão do navegador
    return render_template('login.html', titulo='Hospital Tô de BOAS')


@app.route('/autenticar', methods=['POST', ])
def autenticacao():
    usuario = request.form['nome_de_usuario']
    senha = request.form['senha']
    for medico in lista_medicos:
        print('Etapa 0')
        if medico.nome_de_usuario == usuario:
            print('Etapa 1')
            if medico.senha == senha:
                print('Etapa 2')
                session['medico_logado'] = usuario
                flash(usuario + ' logou com sucesso')
                return redirect(url_for('area_de_trabalho'))
            else:
                flash('Você errou algo, tente novamente!')
                return redirect(url_for('login'))
                print('Etapa 3')

    for gerente in lista_gerentes:
        if gerente.nome_de_usuario == usuario:
            if gerente.senha == senha:
                session['gerente_logado'] = usuario
                flash(usuario + ' logou com sucesso')
                return redirect(url_for('area_de_trabalho'))
            else:
                flash('Você errou algo, tente novamente!')
                return redirect(url_for('login'))

    flash('Você errou algo, tente novamente!')
    return redirect(url_for('login'))



@app.route('/logout')
def sair():
    session['gerente_logado'] = None
    session['medico_logado'] = None
    flash('Nenhum usuário logado')
    return redirect(url_for('login'))


@app.route('/workspace')
def area_de_trabalho():
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            for medico in lista_medicos:
                if medico.nome_de_usuario == session['medico_logado']:
                    return render_template('workspace.html', titulo='Workspace', lista=medico.menu)
    else:
        for gerente in lista_gerentes:
            if gerente.nome_de_usuario == session['gerente_logado']:
                return render_template('workspace.html', titulo='Workspace', lista=gerente.menu)

@app.route('/confirmacao')
def confirmacao():
    mensagem = request.args.get('titulo')
    origem = request.args.get('origem')
    destino = request.args.get('destino')
    return render_template('confirmacao.html', destino=destino, origem=origem)


@app.route('/listarCirurgia')
def cirurgias():  # todo Confirmação se é o Gerente ou o medico

    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            cirurgias_do_medico = []

            for medico in lista_medicos:
                if medico.nome_de_usuario == session['medico_logado']:
                    for cirurgia in lista_cirurgias:
                        if cirurgia.medico == medico.crm:
                            cirurgias_do_medico.append(cirurgia)

            return render_template('listagem_objetos.html', titulo='Cirurgias do Medico', cirurgias=cirurgias_do_medico)


    else:
        return render_template('listagem_objetos.html', titulo='Cirurgias', cirurgias=lista_cirurgias)


@app.route('/listarGerente')
def gerentes():
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            flash('Você não tem permissão!')
            return redirect(url_for('area_de_trabalho'))
    else:
        return render_template('listagem_pessoas.html', titulo='Gerentes', pessoas=lista_gerentes)


@app.route('/listaCliente')
def clientes():
    lista = []
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            for medico in lista_medicos:
                if medico.nome_de_usuario == session['medico_logado']:
                    for id in medico.lista_de_clientes:
                        for cliente in lista_clientes:
                            if cliente.cpf == id:
                                lista.append(cliente)
                    return render_template('listagem_pessoas.html', titulo='Clientes', pessoas=lista)
    else:
        return render_template('listagem_pessoas.html', titulo='Clientes', pessoas=lista_clientes)


@app.route('/listarMedicos')
def medicos():
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            flash('Você não tem permissão!')
            return redirect(url_for('area_de_trabalho'))
    else:
        return render_template('listagem_pessoas.html', titulo='Medicos', pessoas=lista_medicos)


@app.route('/listarSalas')
def salas():
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            flash('Você não tem permissão!')
            return redirect(url_for('area_de_trabalho'))
    else:
        return render_template('listagem_objetos.html', titulo='Salas', salas=lista_salas)


@app.route('/addCliente')
def adicionar_cliente():
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            flash('Você não tem permissão!')
            return redirect(url_for('area_de_trabalho'))
    else:
        return render_template('novo_pessoas.html', titulo='Adicionar Cliente', medicos=lista_medicos)


@app.route('/addMedico')
def adicionar_medico():
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            flash('Você não tem permissão!')
            return redirect(url_for('area_de_trabalho'))
    else:
        return render_template('novo_pessoas.html', titulo='Adicionar Medico')


@app.route('/addCirurgia')
def adicionar_cirurgia():
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            flash('Você não tem permissão!')
            return redirect(url_for('area_de_trabalho'))
    else:
        return render_template('novo_objetos.html', titulo='Adicionar Cirurgia', medicos=lista_medicos,
                           clientes=lista_clientes, salas=lista_salas)


@app.route('/addSala')
def adicionar_sala():
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            flash('Você não tem permissão!')
            return redirect(url_for('area_de_trabalho'))
    else:
        return render_template('novo_objetos.html', titulo='Adicionar Sala')


@app.route('/criaCliente', methods=['POST', ])
def criar_cliente():
    nome = request.form['nome']
    data = request.form['data_de_nascimento']
    cpf = request.form['cpf']
    new_cliente = Cliente(nome, data, cpf)
    crm = request.form['medico_cliente']
    for medico in lista_medicos:
        if medico.crm == crm:
            medico.adicionar_cliente(new_cliente)
    lista_clientes.append(new_cliente)
    salva_clientes(lista_clientes)
    salva_medicos(lista_medicos)
    return redirect(url_for('area_de_trabalho'))


@app.route('/criarMedico', methods=['POST', ])
def cria_medico():
    nome = request.form['nome']
    data = request.form['data_de_nascimento']
    salario = request.form['salario']
    usurio = request.form['nome_de_usuario']
    senha = request.form['senha']
    crm = request.form['crm']

    new_medico = Medico(nome, data, salario, usurio, senha, crm)
    lista_medicos.append(new_medico)
    salva_medicos(lista_medicos)
    return redirect(url_for('area_de_trabalho'))


@app.route('/criarCirurgia', methods=['POST', ])
def criar_cirurgia():
    medico = request.form['medico_cirurgia']
    paciente = request.form['paciente_cirurgia']
    sala = request.form['sala_cirurgia']
    data = request.form['data_da_cirurgia']
    hora = request.form['hora_da_cirurgia']

    new_cirurgia = Cirurgia(paciente, medico, sala, data, hora)
    lista_cirurgias.append(new_cirurgia)
    salva_cirurgias(lista_cirurgias)
    return redirect(url_for('area_de_trabalho'))


@app.route('/criarSala', methods=['POST', ])
def criar_sala():
    numero = request.form['numero']
    andar = request.form['andar']

    new_sala = Sala(numero, andar)

    lista_salas.append(new_sala)
    salva_salas(lista_salas)
    return redirect(url_for('area_de_trabalho'))


@app.route('/editCliente')
def editar_cliente():
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            flash('Você não tem permissão!')
            return redirect(url_for('area_de_trabalho'))
    else:
        id = request.args.get('id')
        for cliente in lista_clientes:
            if cliente.cpf == id:
                return render_template('edita_pessoas.html', titulo='Editando Cliente', pessoa=cliente,
                                       medicos=lista_medicos,
                                       id=id)


@app.route('/editMedico')
def editar_medico():
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            flash('Você não tem permissão!')
            return redirect(url_for('area_de_trabalho'))
    else:
        id = request.args.get('id')
        tipo = request.args.get('tipo')
        for medico in lista_medicos:
            if medico.crm == id:
                return render_template('edita_pessoas.html', titulo='Editando Medico', pessoa=medico, id=id, tipo=tipo)


@app.route('/editCirurgia')
def editar_cirurgia():
    id = request.args.get('id')
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:

            for cirurgia in lista_cirurgias:
                if cirurgia.id == id:
                    return render_template('edita_cirurgia_medico.html', objeto=cirurgia, titulo='Editar Cirurgia',
                                           medicos=lista_medicos, clientes=lista_clientes, salas=lista_salas, id=id)
    else:
        for cirurgia in lista_cirurgias:
            if cirurgia.id == id:
                return render_template('edita_objetos.html', objeto=cirurgia, titulo='Editar Cirurgia',
                                       medicos=lista_medicos, clientes=lista_clientes, salas=lista_salas, id=id)


@app.route('/editSala')
def editar_sala():
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            flash('Você não tem permissão!')
            return redirect(url_for('area_de_trabalho'))
    else:
        id = request.args.get('id')
        for sala in lista_salas:
            if sala.id == id:
                return render_template('edita_objetos.html', objeto=sala, titulo='Editar Sala', id=id)


@app.route('/upCliente', methods=['POST', ])
def atualiza_cliente():
    id = request.args.get('id')
    nome = request.form['nome']
    data = request.form['data_de_nascimento']
    cpf = request.form['cpf']
    new_cliente = Cliente(nome, data, cpf)
    crm = request.form['medico_cliente']
    for medico in lista_medicos:
        for paciente in medico.lista_de_clientes:
            if paciente == id:
                for cliente in lista_clientes:
                    if cliente.cpf == id:
                        medico.remover_cliente(cliente)
        if medico.crm == crm:
            medico.adicionar_cliente(new_cliente)

    for cliente in lista_clientes:
        if cliente.cpf == id:
            lista_clientes.remove(cliente)
            lista_clientes.append(new_cliente)
            salva_clientes(lista_clientes)
    return redirect(url_for('clientes'))


@app.route('/upMedico', methods=['POST', ])
def atualiza_medico():
    id = request.args.get('id')
    nome = request.form['nome']
    data = request.form['data_de_nascimento']
    salario = request.form['salario']
    usurio = request.form['nome_de_usuario']
    senha = request.form['senha']
    crm = request.form['crm']

    new_medico = Medico(nome, data, salario, usurio, senha, crm)

    for medico in lista_medicos:
        if medico.crm == id:
            lista_medicos.remove(medico)
            lista_medicos.append(new_medico)
            salva_medicos(lista_medicos)

    return redirect(url_for('medicos'))


@app.route('/upCirurgia', methods=['POST', ])
def atualiza_cirurgia():
    id = request.args.get('id')
    medico = request.form['medico_cirurgia']
    paciente = request.form['paciente_cirurgia']
    sala = request.form['sala_cirurgia']
    data = request.form['data_da_cirurgia']
    hora = request.form['hora_da_cirurgia']

    new_cirurgia = Cirurgia(paciente, medico, sala, data, hora)
    for cirurgia in lista_cirurgias:
        if cirurgia.id == id:
            lista_cirurgias.remove(cirurgia)
            lista_cirurgias.append(new_cirurgia)
            salva_cirurgias(lista_cirurgias)

    return redirect(url_for('cirurgias'))


@app.route('/upSala', methods=['POST', ])
def atualizar_sala():
    id = request.args.get('id')
    numero = request.form['numero']
    andar = request.form['andar']

    new_sala = Sala(numero, andar)

    for sala in lista_salas:
        if sala.id == id:
            lista_salas.remove(sala)
            lista_salas.append(new_sala)
            salva_salas(lista_salas)

    return redirect(url_for('salas'))


@app.route('/feedback', methods=['POST', ])
def dar_feedback():
    id = request.args.get('id')
    for cirurgia in lista_cirurgias:
        if cirurgia.id == id:
            medico = cirurgia.medico
            paciente = cirurgia.cliente
            sala = request.form['sala_cirurgia']
            data = request.form['data_da_cirurgia']
            hora = request.form['hora_da_cirurgia']
            feedback = request.form['feedback']
            new_cirurgia = Cirurgia(paciente, medico, sala, data, hora)
            new_cirurgia.dar_feedback(feedback)
            lista_cirurgias.remove(cirurgia)
            lista_cirurgias.append(new_cirurgia)
            salva_cirurgias(lista_cirurgias)
            return redirect(url_for('cirurgias'))

    return redirect(url_for('cirurgias'))


@app.route('/delCliente')
def deletar_cliente():
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            flash('Você não tem permissão!')
            return redirect(url_for('area_de_trabalho'))
    else:
        id = request.args.get('id')
        for cliente in lista_clientes:
            if cliente.cpf == id:
                lista_clientes.remove(cliente)
                salva_clientes(lista_clientes)
                for medico in lista_medicos:
                    for cliente in medico.lista_de_clientes:
                        if cliente == id:
                            medico.remover_cliente(cliente)
                            salva_medicos(lista_medicos)
        return redirect(url_for('clientes'))




@app.route('/delMedico')
def deletar_medico():
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            flash('Você não tem permissão!')
            return redirect(url_for('area_de_trabalho'))
    else:
        id = request.args.get('id')
        for medico in lista_medicos:
            if medico.crm == id:
                lista_medicos.remove(medico)
                salva_medicos(lista_medicos)

        return redirect(url_for('medicos'))


@app.route('/delCirurgia')
def deletar_cirurgia():
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            flash('Você não tem permissão!')
            return redirect(url_for('area_de_trabalho'))
    else:
        id = request.args.get('id')
        for cirurgia in lista_cirurgias:
            if cirurgia.id == id:
                lista_cirurgias.remove(cirurgia)
                salva_cirurgias(lista_cirurgias)

        return redirect(url_for('cirurgias'))




@app.route('/delSala')
def deletar_sala():
    if 'gerente_logado' not in session or session['gerente_logado'] == None:
        if 'medico_logado' not in session or session['medico_logado'] == None:
            flash('Você não tem acesso, faça o login e tente novamente!')
            return redirect(url_for('login'))
        else:
            flash('Você não tem permissão!')
            return redirect(url_for('area_de_trabalho'))
    else:
        id = request.args.get('id')
        for sala in lista_salas:
            if sala.id == id:
                lista_salas.remove(sala)
                salva_salas(lista_salas)

        return redirect(url_for('salas'))




if __name__ == '__main__':
    app.run()

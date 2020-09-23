from flask import Blueprint, jsonify, request
from . import db
from .models import Consultas, Medicos, Pacientes, Agendas
from datetime import datetime

main = Blueprint('main', __name__)



@main.route('/medicos/')
def ListMedicos():
    consultas = Medicos.query.all()
    mdcs = []

    for m in consultas:
        mdcs.append[{'id': m.id, 'nome': m.nome, 'email': m.email, 'telefone': m.telefone, 'especialidade': m.especialidade, }]
    return jsonify(mdcs), 200

########################################################  Consultas de pacientes  ######################################################################
@main.route('/consulta/')
def ListConsult():
    consultar = Consultas.query.all()

    atds = []

    for u in consultar:
        atds.append({'id': u.id, 'title': u.title, 'paciente': u.paciente, 'medico': u.nomemedico,'data': 'data', 'descricao': u.descricao,})

    return jsonify(atds), 200



@main.route ('/consulta/<cod>/')
def ListConsultId(cod):
    consult = Consultas.query.filter(Consultas.id == cod)
    atds = []

    for u in consult:
        atds.append({'id': u.id, 'title': u.title, 'paciente': u.paciente, 'medico': u.nomemedico, 'data': 'data', 'descricao': u.descricao})

    return jsonify(atds), 201





@main.route('/consulta/', methods=['POST'])
def Add_Consult():
    consult_date = request.get_json()

    new_consult = Consultas(title=consult_date['title'], paciente=consult_date['paciente'], nomemedico=consult_date['nomemedico'],data=datetime.now(), descricao=consult_date['descricao'])
    db.session.add(new_consult)
    db.session.commit()
    return 'Done, Consult Added!', 201




@main.route('/consulta/<cod>/', methods= ['PUT', 'PATCH'])
def Update_Consult(cod):
    query = Consultas.query.filter(Consultas.id == cod)
    query.update(request.json)
    db.session.commit()

    return 'Done, Consult Update!', 201



@main.route('/consulta/<cod>/', methods=['DELETE'])
def Delete_Consult(cod):
    query = Consultas.query.filter(Consultas.id == cod)
    query.delete()
    db.session.commit()

    return 'Done, Deleted Sucess!', 201





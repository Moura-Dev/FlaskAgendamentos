from . import db

class Medicos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(70))
    email = db.Column(db.String(40))
    telefone = db.Column(db.Integer())
    especialidade = db.Column(db.String(30))
    tipouser = db.Column(db.Integer, default=1)
    login = db.Column(db.String(20), nullable =False , unique=True)
    senha = db.Column(db.String(15))
    ConsultaMarcada = db.relationship('Consultas', backref='medicos', lazy=False)
    Agendamento = db.relationship('Agendas', backref='medicos', lazy=False) 
    

class Pacientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(70))
    email = db.Column(db.String(40))
    telefone = db.Column(db.Integer())
    datanascimento = db.Column(db.String(10))
    tipouser = db.Column(db.Integer, default=2)
    ConsultaMarcada = db.relationship('Consultas', backref='pacientes', lazy=False)
    Agendamento = db.relationship('Agendas', backref='pacientes', lazy=False) 


class Consultas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    paciente = db.Column(db.String(50))
    nomemedico = db.Column(db.String(50))
    data = db.Column(db.DATETIME)
    descricao = db.Column(db.String(300))
    idmedico = db.Column(db.Integer, db.ForeignKey('medicos.id'),
        nullable=False)
    idpaciente = db.Column(db.Integer, db.ForeignKey('pacientes.id'),
        nullable=False)


class Agendas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dataconsulta = db.Column(db.String(10))
    idmedico = db.Column(db.Integer, db.ForeignKey('medicos.id'),
        nullable=False)
    idpaciente = db.Column(db.Integer, db.ForeignKey('pacientes.id'),
        nullable=False)
    descricao = db.Column(db.String(300))
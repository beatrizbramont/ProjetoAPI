from flask import jsonify
from models.modelProfessor import professorPorID
from config import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100))
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    ativo = db.Column(db.String(100))

    alunos = db.relationship('Aluno', backref='Turma', lazy=True) 

    def __init__(self, descricao, professor_id, ativo):
        self.descricao = descricao
        self.professor_id = professor_id
        self.ativo = ativo

    def to_dict(self):
        return {'id': self.id, 
                'descricao': self.descricao,
                'professor_id': self.professor_id,
                'ativo': self.ativo}

def verificar_campo_null(dados):
    for chave, valor in dados.items():
        if valor == None:
            return jsonify({"error": f"O campo {chave} informado é obrigatório."}), 400
        

# CREATE
def createTurma(dados):
    vazio = verificar_campo_null(dados)
    if vazio:
        return vazio
        
    professor_existente = professorPorID(dados['professor_id'])
    if not professor_existente:
        return jsonify({"error": "Professor não encontrado"}), 404
        
    
        
    nova_turma = Turma(
        descricao=dados['descricao'],
        professor_id=dados['professor_id'],
        ativo=dados['ativo']
    )
    
    db.session.add(nova_turma)
    db.session.commit()
    
    return jsonify(nova_turma.to_dict()), 200

# GET 
def todasTurmas():
    turmas = Turma.query.all()
    return jsonify([turma.to_dict() for turma in turmas])
 
def turmaPorID(idTurma):
    turma = Turma.query.get(idTurma)
    if turma:
        return jsonify(turma.to_dict())
    return jsonify({"error": "Turma não encontrada"})

# UPDATE 
def updateTurma(idTurma, dados):
    vazio = verificar_campo_null(dados)
    if vazio:
        return vazio

    turma = Turma.query.get(idTurma)
    if not turma:
        return jsonify({"error": "Turma não encontrada"}), 404

    for chave, valor in dados.items():
        if hasattr(turma, chave):
            setattr(turma, chave, valor)

    db.session.commit()
    return jsonify(turma.to_dict()), 200

# DELETE 
def deleteTurma(idTurma):
    turma = Turma.query.get(idTurma)
    if not turma:
        return jsonify({"error": "Turma não encontrada"}), 400

    db.session.delete(turma)
    db.session.commit()
    return jsonify({"message": "Turma deletada com sucesso."}), 200

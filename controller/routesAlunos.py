from flask import Blueprint, request, jsonify
from models import modelAluno

alunos_bp = Blueprint('alunos', __name__) #Criando uma instância

#Create
@alunos_bp.route('/alunos', methods=['POST'])
def createAluno():
    try:
        dados = request.json
             
        modelAluno.createAluno(dados)
        return jsonify(dados), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#Get
@alunos_bp.route('/alunos', methods=['GET'])
def getAluno():
    try:
        return modelAluno.todosAlunos()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@alunos_bp.route('/alunos/<int:idAluno>', methods=['GET'])
def aluno_Id(id_aluno):
    try:
        modelAluno.alunoPorID(id_aluno)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#Put
@alunos_bp.route("/alunos/<int:idAluno>", methods=['PUT'])
def updateAlunos(idAluno):
    try:
        dados = request.json

        aluno = modelAluno.updateAluno(idAluno, dados)
        return jsonify(aluno)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#Delete
@alunos_bp.route('/alunos/<int:idAluno>', methods=['DELETE'])
def delete_aluno(idAluno):
    modelAluno.deleteAluno(idAluno) 
    if modelAluno.deleteAluno() == True:
        return jsonify("Aluno excluído com sucesso"), 200
    
    else:
        return ("Aluno não encontrado"), 404
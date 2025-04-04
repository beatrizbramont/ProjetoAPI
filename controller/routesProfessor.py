from flask import Blueprint, request, jsonify
from models import modelProfessor

professor_bp = Blueprint('professor', __name__) #Criando uma instância

#Create
@professor_bp.route('/professor', methods=['POST'])
def createProfessores():
    try:
        dados = request.json

        modelProfessor.createProfessores(dados)          
        return jsonify(dados), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#GET
@professor_bp.route("/professor", methods=['GET'])
def getProfessor():
    try:
        return modelProfessor.todosProfessores()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@professor_bp.route('/professor/<int:id_professor>', methods=['GET'])
def professor_Id(id_professor):
    try:
        modelProfessor.professor_porID(id_professor)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#PUT
@professor_bp.route("/professor/<int:idProfessor>", methods=['PUT'])
def updateProfessores(idProfessor):
    try:
        dados = request.json
        
        professor = modelProfessor.updateProfessor(idProfessor, dados)
        return jsonify(professor)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#DELETE
   
@professor_bp.route('/professor/<int:idProfessor>', methods=['DELETE'])
def delete_professor(idProfessor):
    modelProfessor.deleteProfessor(idProfessor) 
    if modelProfessor.deleteProfessor() == True:
        return jsonify("Professor excluído com sucesso"), 200
    
    else:
        return ("Professor não encontrado"), 404
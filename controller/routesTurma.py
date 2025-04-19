from flask import Blueprint, request, jsonify
from models import modelTurma

turma_bp = Blueprint('turma', __name__) #Criando uma instância
 
# POST (CREATE)

@turma_bp.route('/turma', methods=['POST'])
def createTurma():
    try:
        dados = request.json
        return modelTurma.createTurma(dados)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET (READ) - TURMA  
  
@turma_bp.route('/turma', methods=['GET'])
def getTurma():
    try: 
        return modelTurma.todasTurmas() 
    except Exception as e:
        return jsonify ({"error": str(e)}), 500

@turma_bp.route('/turma/<int:id_turma>', methods=['GET'])
def turma_Id(id_turma):
    try:
        return modelTurma.turmaPorID(id_turma)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# PUT (UPDATE)

@turma_bp.route("/turma/<int:idTurma>", methods=['PUT'])
def updateTurma(idTurma):
    try:
        dados = request.json
        turma_response, status_code = modelTurma.updateTurma(idTurma, dados)
        return turma_response, status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#DELETE

@turma_bp.route('/turma/<int:idTurma>', methods=['DELETE'])
def delete_turma(idTurma):
    return modelTurma.deleteTurma(idTurma)


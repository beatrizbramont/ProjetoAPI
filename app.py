from flask import Flask, jsonify, request
from models import modelAluno, modelProfessor, modelTurma

app = Flask(__name__)


# POST (CREATE)

@app.route('/turma', methods=['POST'])
def createTurma():
    try:
        dados = request.json

        modelTurma.createTurma(dados)
        return jsonify(dados), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    

    
# GET (READ) - PROFESSOR

    
# GET (READ) - TURMA    
@app.route('/turma', methods=['GET'])
def getTurma():
    try: 
        return modelTurma.todasTurmas() 
    except Exception as e:
        return jsonify ({"error": str(e)}), 500

@app.route('/turma/<int: id_turma>', methods=['GET'])
def turma_Id(id_turma):
    try:
        modelTurma.turmaPorID(id_turma)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# PUT (UPDATE)




@app.route("/turma/<int:idTurma>", methods=['PUT'])
def updateTurma(idTurma):
    try:
        dados = request.json

        turma = modelTurma.updateTurma(idTurma, dados)
        return jsonify(turma)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


#DELETE

    
 
    

@app.route('/turma/<int:idTurma>', methods=['DELETE'])
def delete_turma(idTurma):
    modelTurma.deleteTurma(idTurma)
    if modelTurma.deleteTurma() == True:
        return jsonify({"Turma excluída com sucesso."}), 200
    else:
        return jsonify({"Turma não encontrada."}), 404



if __name__ == '__main__':
    app.run(debug=True)

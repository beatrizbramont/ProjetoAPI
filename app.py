from flask import Flask, jsonify, request
from models import modelAluno, modelProfessor, modelTurma

app = Flask(__name__)


# POST (CREATE)
@app.route('/alunos', methods=['POST'])
def createAluno():
    try:
        dados = request.json
             
        modelAluno.createAluno(dados)
        return jsonify(dados), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/professor', methods=['POST'])
def createProfessores():
    try:
        dados = request.json

        modelProfessor.createProfessores(dados)          
        return jsonify(dados), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/turma', methods=['POST'])
def createTurma():
    try:
        dados = request.json

        modelTurma.createTurma(dados)
        return jsonify(dados), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET (READ) - ALUNO
@app.route('/alunos', methods=['GET'])
def getAluno():
    try:
        return modelAluno.todosAlunos()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/alunos/<int: idAluno>', methods=['GET'])
def aluno_Id(id_aluno):
    try:
        modelAluno.alunoPorID(id_aluno)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# GET (READ) - PROFESSOR
@app.route("/professor", methods=['GET'])
def getProfessor():
    try:
        return modelProfessor.todosProfessores()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/professor/<int: id_professor>', methods=['GET'])
def professor_Id(id_professor):
    try:
        modelProfessor.professor_porID(id_professor)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
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
@app.route("/alunos/<int:idAluno>", methods=['PUT'])
def updateAlunos(idAluno):
    try:
        dados = request.json

        aluno = modelAluno.updateAluno(idAluno, dados)
        return jsonify(aluno)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/professor/<int:idProfessor>", methods=['PUT'])
def updateProfessores(idProfessor):
    try:
        dados = request.json
        
        professor = modelProfessor.updateProfessor(idProfessor, dados)
        return jsonify(professor)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/turma/<int:idTurma>", methods=['PUT'])
def updateTurma(idTurma):
    try:
        dados = request.json

        turma = modelTurma.updateTurma(idTurma, dados)
        return jsonify(turma)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


#DELETE
@app.route('/alunos/<int:idAluno>', methods=['DELETE'])
def delete_aluno(idAluno):
    modelAluno.deleteAluno(idAluno) 
    if modelAluno.deleteAluno() == True:
        return jsonify("Aluno excluído com sucesso"), 200
    
    else:
        return ("Aluno não encontrado"), 404
    
    
@app.route('/professor/<int:idProfessor>', methods=['DELETE'])
def delete_professor(idProfessor):
    modelProfessor.deleteProfessor(idProfessor) 
    if modelProfessor.deleteProfessor() == True:
        return jsonify("Professor excluído com sucesso"), 200
    
    else:
        return ("Professor não encontrado"), 404
    

@app.route('/turma/<int:idTurma>', methods=['DELETE'])
def delete_turma(idTurma):
    modelTurma.deleteTurma(idTurma)
    if modelTurma.deleteTurma() == True:
        return jsonify({"Turma excluída com sucesso."}), 200
    else:
        return jsonify({"Turma não encontrada."}), 404



if __name__ == '__main__':
    app.run(debug=True)

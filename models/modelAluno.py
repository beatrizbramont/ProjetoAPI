from flask import Flask, jsonify, request
from models.modelTurma import turmaPorID

dici = {
    "alunos": [
        {
            "id": 1,
            "nome": "Nome do aluno",
            "idade": 0,
            "data_nascimento": "Data de nascimento",
            "nota_primeiro_semestre": 0,
            "nota_segundo_semestre": 0,
            "media_final": 0,
            "turma_id": 1
        }
    ]
}

def verificar_duplicacao(id, lista, tipo):
    if any(item['id'] == id for item in lista):
        return jsonify({"error": f"{tipo} com ID {id} já existe."}), 400
    return None

def verificar_campo_null(dados):
    for chave, valor in dados.items():
        if valor == None:
            return jsonify({"error": "O campo " + chave + " informado é obrigatório."})

# Create
def createAluno(dados):    

    vazio = verificar_campo_null(dados)
    if vazio:
        return vazio, 400
    
    turma_existente = turmaPorID(dados['turma_id'])
    if turma_existente == False:
        return jsonify({"error": "Turma não existe"}), 404
                
    duplicacao = verificar_duplicacao(dados['id'], dici["alunos"], "Aluno")
    if duplicacao:
        return duplicacao

    dici['alunos'].append(dados)
    return jsonify(dados), 200

# Get      
def todosAlunos():
    return dici['alunos']
    
def alunoPorID(idAluno):
    lista_alunos = dici['alunos']
    for aluno in lista_alunos:
        if aluno['id'] == idAluno:
            return aluno
    return False

# Put
def updateAluno(idAluno, dados):
    vazio = verificar_campo_null(dados)
    if vazio:
        return vazio, 400
            
    aluno = next((aluno for aluno in dici["alunos"] if aluno["id"] == idAluno), None)
    if not aluno:
        return jsonify({"error": "Aluno nao encontrado"}), 404
            
    aluno.update(dados)  
    return jsonify(aluno), 200
    # aluno = alunoPorID(idAluno, dados)
    # if aluno:
    #     aluno.update(dados)
    #     return jsonify(aluno), 200
    # return jsonify({"error": "Erro ao atualizar o aluno"}), 500

# Delete

def deleteAluno(idAluno):
    aluno = alunoPorID(idAluno)
    if aluno:
        dici['alunos'].remove(aluno)
        return True
    
    return False
    
            
    
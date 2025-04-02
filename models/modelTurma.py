from flask import Flask, jsonify, request

dici = {
    "turma": [
        {
            "id": 1,
            "descricao": "Descriçaõ da turma",
            "professor_id": 1,
            "ativo": "Status"
        }
    ]
}


# CREATE
def createTurma(dados):
    dici['turma'].append(dados)
    return True

# GET 
def todasTurmas():
    return dici['turma']
 
def turma_porID(id_turma):
    lista_turmas = dici['turma']
    for turma in lista_turmas:
        if turma['id'] == id_turma:
            return turma
    return False

# UPDATE 
def updateTurma(id_turma, dados):
    turma = turma_porID(id_turma)
    if turma:
        turma.update(dados)
        return turma
    return False

# DELETE 
def deleteTurma(id_turma):
    turma = turma_porID(id_turma)
    if turma:
        dici['turma'].remove(turma)
        return True
    return False


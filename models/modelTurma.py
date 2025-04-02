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
 
def turmaPorID(idTurma):
    lista_turmas = dici['turma']
    for turma in lista_turmas:
        if turma['id'] == idTurma:
            return turma
        
    return False

# UPDATE 
def updateTurma(idTurma, dados):
    turma = turmaPorID(idTurma)
    if turma:
        turma.update(dados)
        return turma
    return False

# DELETE 
def deleteTurma(idTurma):
    turma = turmaPorID(idTurma)
    if turma:
        dici['turma'].remove(turma)
        return True
    
    return False


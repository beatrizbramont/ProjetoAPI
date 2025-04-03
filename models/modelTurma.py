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

def verificar_duplicacao(id, lista, tipo):
    if any(item['id'] == id for item in lista):
        return jsonify({"error": f"{tipo} com ID {id} já existe."}), 400
    return None

def verificar_campo_null(dados):
    for chave, valor in dados.items():
        if valor == None:
            return jsonify({"error": "O campo " + chave + " informado é obrigatório."})
        

# CREATE
def createTurma(dados):
    vazio = verificar_campo_null(dados)
    if vazio:
        return vazio, 400
        
    professor_existente = next((professor for professor in dici["professor"] if professor["id"] == dados["professor_id"]), None)
    if not professor_existente:
        return jsonify({"error": "Professor não encontrado."}), 404
        
    duplicacao = verificar_duplicacao(dados['id'], dici["turma"], "Turma")
    if duplicacao:
        return duplicacao
        
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
    vazio = verificar_campo_null(dados)
    if vazio:
        return vazio, 400
        
    turma = next((turma for turma in dici["turma"] if turma["id"] == idTurma), None)
    if not turma:
        return jsonify({"error": "Turma não encontrada"}), 404
        
    duplicacao = verificar_duplicacao(dados['id'], dici["turma"], "Turma")
    if duplicacao:
        return duplicacao
                
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


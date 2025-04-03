from flask import Flask, jsonify, request


dici = {
    "professor": [
        {
            "id": 1,
            "nome": "Nome do professor",
            "idade": 0,
            "materia": "Nome da materia",
            "observacoes": "Observacao sobre o professor"
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

#CREATE

def createProfessores(dados):
    vazio = verificar_campo_null(dados)
    if vazio:
        return vazio, 400
        
    duplicacao = verificar_duplicacao(dados['id'], dici["professor"], "Professor")
    if duplicacao:
        return duplicacao
        
    dici['professor'].append(dados)
    return True

#GET

def todosProfessores():
      return dici['professor']

def professor_porID(id_professor):
    lista_professores = dici['professor']
    for professor in lista_professores:
          if professor['id'] == id_professor:
                return professor
    return False


#PUT 

def updateProfessor(idProfessor, dados):
    vazio = verificar_campo_null(dados)
    if vazio:
        return vazio, 400
        
    professor = next((professor for professor in dici["professor"] if professor["id"] == idProfessor), None)
    if not professor:
        return jsonify({"error": "Professor não encontrado"}), 404
        
    duplicacao = verificar_duplicacao(dados['id'], dici["professor"], "Professor")
    if duplicacao:
        return duplicacao
    
    professor = professor_porID(idProfessor)
    if professor:
        professor.update(dados)
        return professor
    
    return False

#DELETE

def deleteProfessor(idProfessor):
    professor = professor_porID(idProfessor)
    if professor:
        dici['professor'].remove(professor)
        return True
    
    return False
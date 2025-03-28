from app import verificar_campo_null, verificar_duplicacao

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

#CREATE

def createProfessores(dados):
   
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
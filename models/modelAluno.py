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

# Create
def createAluno(dados):    
    dici['alunos'].append(dados)
    return True

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
    aluno = alunoPorID(idAluno)
    if aluno:
        aluno.update(dados)
        return aluno
    
    return False

# Delete
def deleteAluno(idAluno):
    aluno = alunoPorID(idAluno)
    if aluno:
        dici['alunos'].remove(aluno)
        return True
    
    return False
    
            
    
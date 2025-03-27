from app import verificar_campo_null, verificar_duplicacao
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

def createAluno(dados):
        
    vazio = verificar_campo_null(dados)
    if vazio:
        return vazio, 400

        
    turma_existente = next((turma for turma in dici["turma"] if turma["id"] == dados["turma_id"]), None)
    if not turma_existente:
        return ({"error": "Turma não encontrada."}), 404 

    duplicacao = verificar_duplicacao(dados['id'], dici["alunos"], "Aluno")
    if duplicacao:
        return duplicacao
    dici['alunos'].append(dados)
    return(dados), 201


def aluno_porID(id_aluno):
    return id_aluno


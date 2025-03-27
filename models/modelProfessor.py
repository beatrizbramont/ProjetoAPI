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

def createProfessores(dados):
    try:
       
        vazio = verificar_campo_null(dados)
        if vazio:
            return vazio, 400
        
        duplicacao = verificar_duplicacao(dados['id'], dici["professor"], "Professor")
        if duplicacao:
            return duplicacao
        
        dici['professor'].append(dados)
        return (dados), 201
    
    except Exception as e:
        return ({"error": str(e)}), 500
    

def professor_porID(id_professor):
    return id_professor

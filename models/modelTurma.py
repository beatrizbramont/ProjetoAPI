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


def turma_porID(id_turma):
    return id_turma

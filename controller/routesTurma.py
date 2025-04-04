from flask import Blueprint, request, jsonify
from models import modelTurma

turma_bp = Blueprint('turma', __name__) #Criando uma instância

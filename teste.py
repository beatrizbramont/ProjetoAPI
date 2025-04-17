import os
from config import db, app
from sqlalchemy import inspect

with app.app_context():
    inspector = inspect(db.engine)

    # Listar todas as tabelas
    tabelas = inspector.get_table_names()
    print("Tabelas:", tabelas)

    # Ver colunas de uma tabela específica
    colunas = inspector.get_columns('turma')
    for coluna in colunas:
        print(f"Coluna: {coluna['name']}, Tipo: {coluna['type']}")



# Criar uma função decodificação jwt - validação nas rotas - JWT
# 3° Arrumar os testes
# 2° JTW
# 1° Docker (configuração)
# 4° Deploy 
# --------------------
# - Passar para o MYSQL (Baixar e configurar)
# - Mexer com o Docker
# - Deploy
#Tem que criar um método para calcular idade (aluno) dentro da classe
#relação many populations 


'''--------------------------------------------------------------'''
# docker build -t saladeaula . - cria imagem (imagem é uma receita para o container)
# docker run -p 8001:8001 saladeaula professor - cria container
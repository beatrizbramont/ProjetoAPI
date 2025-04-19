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



# Criar testes de integração com o banco
# Swagger
# Relatório
# 3° Arrumar os testes
# 4° Deploy 
# --------------------
# - Passar para o MYSQL (Baixar e configurar)
# Criar uma função decodificação jwt - validação nas rotas - JWT
# 2° JTW
# - Mexer com o Docker
# - Deploy
#Tem que criar um método para calcular idade (aluno) dentro da classe
#relação many populations 


'''--------------------------------------------------------------'''
# docker build -t saladeaula . - cria imagem (imagem é uma receita para o container)
# docker run -p 8001:8001 saladeaula professor - cria container

# duplicacao = verificar_duplicacao(dados['id'])
    # if duplicacao:
    #     return duplicacao

    # def verificar_duplicacao(id):
#     if Turma.query.get(id):
#         return jsonify({"error": f"Turma com id {id} já existe."}), 400
#     return None


# def setUp(self):
#     self.app = app.test_client()
#     self.app_context = app.app_context()
#     self.app_context.push()
    
#     # Limpa as tabelas manualmente
#     from models.modelAluno import Aluno
#     from models.modelProfessor import Professor
#     from models.modelTurma import Turma

#     db.session.query(Aluno).delete()
#     db.session.query(Turma).delete()
#     db.session.query(Professor).delete()
#     db.session.commit()


#BANCO MYSQL

''' 1° - CONEXÃO - OK
2° - TESTES DE INTEGRAÇÃO - FAZER
3° - DOCKER COMPOSER'''
# --------------------
# - Passar para o MYSQL (Baixar e configurar)
# Criar uma função decodificação jwt - validação nas rotas - JWT
# 2° JTW
# - Mexer com o Docker
# - Deploy
 


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


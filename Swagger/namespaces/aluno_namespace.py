from flask_restx import Namespace, Resource, fields
from models.modelAluno import createAluno, todosAlunos, alunoPorID, updateAluno, deleteAluno

aluno_ns = Namespace("aluno", description="Operações relacionadas aos aluno")

aluno_model = aluno_ns.model("Aluno", {
    "nome": fields.String(required=True, description="Nome do aluno"),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (YYYY-MM-DD)"),
    "nota_primeiro_semestre": fields.Float(required=True, description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(required=True, description="Nota do segundo semestre"),
    "turma_id": fields.Integer(required=True, description="ID da turma associada"),
})

aluno_output_model = aluno_ns.model("AlunoOutput", {
    "id": fields.Integer(description="ID do aluno"),
    "nome": fields.String(description="Nome do aluno"),
    "idade": fields.Integer(description="Idade do aluno"),
    "data_nascimento": fields.String(description="Data de nascimento (YYYY-MM-DD)"),
    "nota_primeiro_semestre": fields.Float(description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(description="Nota do segundo semestre"),
    "media_final": fields.Float(description="Média final do aluno"),
    "turma_id": fields.Integer(description="ID da turma associada"),
})

@aluno_ns.route("/")
class alunoResource(Resource):
    @aluno_ns.marshal_list_with(aluno_output_model)
    def get(self):
        """Lista todos os alunos"""
        return todosAlunos()

    @aluno_ns.expect(aluno_model)
    def post(self):
        """Cria um novo aluno"""
        data = aluno_ns.payload
        response, status_code = createAluno(data)
        return response, status_code

@aluno_ns.route("/<int:idAluno>")
class AlunoIdResource(Resource):
    @aluno_ns.marshal_with(aluno_output_model)
    def get(self, idAluno):
        """Obtém um aluno pelo ID"""
        return alunoPorID(idAluno)

    @aluno_ns.expect(aluno_model)
    def put(self, idAluno):
        """Atualiza um aluno pelo ID"""
        data = aluno_ns.payload
        updateAluno(idAluno, data)
        return data, 200

    def delete(self, idAluno):
        """Exclui um aluno pelo ID"""
        deleteAluno(idAluno)
        return {"message": "Aluno excluído com sucesso"}, 200
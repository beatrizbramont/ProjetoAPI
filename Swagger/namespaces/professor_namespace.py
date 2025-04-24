from flask_restx import Namespace, Resource, fields
from models.modelProfessor import createProfessor, todosProfessores, professorPorID, updateProfessor, deleteProfessor

professor_ns = Namespace("professor", description="Operações relacionadas ao professor")

professor_model = professor_ns.model("professor", {
    "nome": fields.String(required=True, description="Nome do professor"),
    "idade": fields.String(required=True, description="Idade"),
    "materia": fields.Float(required=True, description="Matéria que leciona"),
    "observacoes": fields.Float(required=True, description="Observações"),
})

professor_output_model = professor_ns.model("professorOutput", {
    "nome": fields.String(description="Nome do professor"),
    "idade": fields.String(description="Idade"),
    "materia": fields.Float(description="Matéria que leciona"),
    "observacoes": fields.Float(description="Observações"),
})

@professor_ns.route("/")
class professorResource(Resource):
    @professor_ns.marshal_list_with(professor_output_model)
    def get(self):
        """Lista todos os professores"""
        return todosProfessores()

    @professor_ns.expect(professor_model)
    def post(self):
        """Cria um novo professor"""
        data = professor_ns.payload
        response, status_code = createProfessor(data)
        return response, status_code

@professor_ns.route("/<int:idProfessor>")
class professorIdResource(Resource):
    @professor_ns.marshal_with(professor_output_model)
    def get(self, idProfessor):
        """Obtém um professor pelo ID"""
        return professorPorID(idProfessor)

    @professor_ns.expect(professor_model)
    def put(self, idProfessor):
        """Atualiza um professor pelo ID"""
        data = professor_ns.payload
        updateProfessor(idProfessor, data)
        return data, 200

    def delete(self, idProfessor):
        """Exclui um professor pelo ID"""
        deleteProfessor(idProfessor)
        return {"message": "professor excluído com sucesso"}, 200
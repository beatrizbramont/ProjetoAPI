import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import app, db
import unittest
from models.modelAluno import Aluno
from models.modelProfessor import Professor
from models.modelTurma import Turma
from datetime import date
from flask import Flask

class TestIntegracaoGeral(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    # def tearDown(self):
    #     db.session.rollback()
    #     db.drop_all()
    #     self.app_context.pop()

    def test_criacao_professor_completo(self):
        professor = Professor(nome="Carla", idade=35, materia="História", observacoes="Experiente")
        db.session.add(professor)
        db.session.commit()

        professor_do_banco = Professor.query.filter_by(nome="Carla").first()
        self.assertIsNotNone(professor_do_banco)
        self.assertEqual(professor_do_banco.nome, "Carla")
        self.assertEqual(professor_do_banco.materia, "História")
        self.assertEqual(professor_do_banco.idade, 35)

    def test_criacao_turma_completo(self):
        # Primeiro, criar o professor
        professor = Professor(nome="Ana", idade=45, materia="Biologia", observacoes="Mestre em Genética")
        db.session.add(professor)
        db.session.commit()

        # Agora, criar a turma
        turma = Turma(descricao="Bio 101", professor_id=professor.id, ativo="Sim")
        db.session.add(turma)
        db.session.commit()

        turma_do_banco = Turma.query.filter_by(descricao="Bio 101").first()
        self.assertIsNotNone(turma_do_banco)
        self.assertEqual(turma_do_banco.descricao, "Bio 101")
        self.assertEqual(turma_do_banco.professor_id, professor.id)
        self.assertEqual(turma_do_banco.ativo, "Sim")

    def test_criacao_aluno_completo(self):
        # Criar professor
        professor = Professor(nome="Rogério", idade=40, materia="Matemática", observacoes="N/A")
        db.session.add(professor)
        db.session.commit()

        # Criar turma
        turma = Turma(descricao="RPA", professor_id=professor.id, ativo="Sim")
        db.session.add(turma)
        db.session.commit()

        # Criar aluno
        aluno = Aluno(
            nome="Rubens",
            data_nascimento=date(2005,5,10),
            nota_primeiro_semestre=8.5,
            nota_segundo_semestre=7.5,
            turma_id=turma.id
        )
        db.session.add(aluno)
        db.session.commit()

        # Buscar e verificar aluno
        aluno_do_banco = Aluno.query.filter_by(nome="Rubens").first()
        self.assertIsNotNone(aluno_do_banco)
        self.assertEqual(aluno_do_banco.nome, "Rubens")
        self.assertEqual(aluno_do_banco.media_final, 8.0)
        self.assertEqual(aluno_do_banco.turma_id, turma.id)

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestIntegracaoGeral)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()

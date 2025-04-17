import unittest
from datetime import date, datetime
from models.modelAluno import Aluno  # Substitua 'your_model_file' pelo nome do seu arquivo .py que contém a classe Aluno

class TestAlunoIdade(unittest.TestCase):

    def test_calcular_idade(self):
        # Suponha que hoje seja 2025-04-17
        data_nascimento = date(2000, 4, 17)  # Exatamente 25 anos atrás
        aluno = Aluno(
            nome="Beatriz",
            data_nascimento=data_nascimento,
            nota_primeiro_semestre=8.0,
            nota_segundo_semestre=7.5,
            media_final=7.75,
            turma_id=1
        )

        idade_calculada = aluno.calcular_idade()
        idade_esperada = datetime.today().year - 2000  # Vai ser 25 se hoje for após ou no aniversário

        if (datetime.today().month, datetime.today().day) < (4, 17):
            idade_esperada -= 1

        self.assertEqual(idade_calculada, idade_esperada)

if __name__ == '__main__':
    unittest.main()

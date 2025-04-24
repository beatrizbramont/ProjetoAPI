import unittest 
import requests
from datetime import datetime

class AlunoTestStringMethods(unittest.TestCase):

    def test_criar_aluno(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'nome': 'José',
            'data_nascimento': "13/05/2005",
            'nota_primeiro_semestre': 9,
            'nota_segundo_semestre': 8,
            'turma_id': 1
        })
        if r.status_code != 200:
            self.fail(f"Erro ao criar aluno José. Status Code: {r.status_code}")

        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'nome': 'Letícia',
            'data_nascimento': "22/02/2004",
            'nota_primeiro_semestre': 10,
            'nota_segundo_semestre': 8,
            'turma_id': 1
        })
        if r.status_code != 200:
            self.fail(f"Erro ao criar aluna Letícia. Status Code: {r.status_code}")
            
        r_lista = requests.get('http://127.0.0.1:8001/alunos')
        if r_lista.status_code != 200:
            self.fail(f"Erro ao obter a lista de alunos. Status Code: {r_lista.status_code}")
            
        lista_retornada = r_lista.json()
        achei_jose = False
        achei_leticia = False
        for aluno in lista_retornada:
            if aluno['nome'] == 'José':
                achei_jose = True
            if aluno['nome'] == 'Letícia':
                achei_leticia = True
        
        if not achei_jose:
            self.fail('Aluno José não apareceu na lista de alunos')
        if not achei_leticia:
            self.fail('Aluna Letícia não apareceu na lista de alunos')

    def test_update_aluno_sucesso(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={ 
            "nome": "Joao",
            "data_nascimento": "01/02/2005",
            "nota_primeiro_semestre": 8.0,
            "nota_segundo_semestre": 9.0,
            "turma_id": 1
        })
        
        assert r.status_code == 200

        aluno_criado = r.json()
        aluno_id = aluno_criado['id']

        updated_r = {
            "id": aluno_id,
            "nome": "Joao Silva",
            "data_nascimento": "01/12/2004",
            "nota_primeiro_semestre": 8.5,
            "nota_segundo_semestre": 9.2,
            "turma_id": 1
        }

        
        response = requests.put(f'http://127.0.0.1:8001/alunos/{aluno_id}', json=updated_r, headers={"Content-Type": "application/json"})
        assert response.status_code == 200

        updated_aluno = response.json()
        assert updated_aluno['nome'] == "Joao Silva"
        
        get_response = requests.get('http://127.0.0.1:8001/alunos')
       
        assert get_response.status_code == 200


    def test_delete_aluno(self): 
        requests.delete('http://127.0.0.1:8001/alunos/6')
    
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'nome': "Matheus",
            'data_nascimento': "13/05/2005",
            'nota_primeiro_semestre': 9,
            'nota_segundo_semestre': 8,
            'turma_id': 1
        })
        if r.status_code != 200:
            self.fail(f"Erro ao criar aluno Matheus. Status Code: {r.status_code}")
        
        aluno_criado = r.json()
        aluno_id = aluno_criado['id']
        r = requests.delete(f'http://127.0.0.1:8001/alunos/{aluno_id}')
        self.assertEqual(r.status_code, 200)
        self.assertIn('Aluno deletado com sucesso', r.json()['message'])

        r_lista = requests.get('http://127.0.0.1:8001/alunos')
        self.assertEqual(r_lista.status_code, 200)
        lista_retornada = r_lista.json()

        achei_matheus = False
        for aluno in lista_retornada:
            if aluno['nome'] == 'Matheus':
                achei_matheus = True

        self.assertFalse(achei_matheus, "O aluno Matheus ainda está na lista de alunos.")
    
    def test_retorna_lista_alunos(self):
        r = requests.get('http://127.0.0.1:8001/alunos')
        if r.status_code == 404:
            return self.fail("Voce nao definiu a pagina '/alunos' no seu server")
            
        try:
            obj_retornado = r.json()
        except:
            self.fail("Era esperado um objeto JSON")
        
        self.assertEqual(type(obj_retornado),type([]))
    
    def test_calculo_idade(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'nome': "Kelvin",
            'data_nascimento': "23/04/2005",
            'nota_primeiro_semestre': 5,
            'nota_segundo_semestre': 8,
            'turma_id': 1
        })
        assert r.status_code == 200

        aluno_criado = r.json()
        aluno_id = aluno_criado['id']

        updated_r = {
            "id": aluno_id,
            "nome": "Kelvin",
            "data_nascimento": "24/04/2004",
            "nota_primeiro_semestre": 5,
            "nota_segundo_semestre": 8,
            "turma_id": 1
        }
        response = requests.put(f'http://127.0.0.1:8001/alunos/{aluno_id}', json=updated_r, headers={"Content-Type": "application/json"})
        assert response.status_code == 200

        updated_aluno = response.json()
        data_retornada = datetime.strptime(updated_aluno['data_nascimento'], "%a, %d %b %Y %H:%M:%S %Z").date()
        data_esperada = datetime.strptime("24/04/2004", "%d/%m/%Y").date()
        assert data_retornada == data_esperada
        
        get_response = requests.get('http://127.0.0.1:8001/alunos')
        assert get_response.status_code == 200

#Testes de integração
    def test_campo_aluno_nome_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'nome': None,
            'data_nascimento': '01/01/2000',
            'nota_primeiro_semestre': 8.0,
            'nota_segundo_semestre': 9.0,
            'turma_id': 1
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo nome informado é obrigatório.', r.json()['error'])

    def test_campo_aluno_datanasc_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'nome': 'Angelina',
            'data_nascimento': None,
            'nota_primeiro_semestre': 8.0,
            'nota_segundo_semestre': 9.0,
            'turma_id': 1
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo data_nascimento informado é obrigatório.', r.json()['error'])

    def test_campo_aluno_nota_primeiro_semestre_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'nome': 'Beatriz',
            'data_nascimento': '03/10/2005',
            'nota_primeiro_semestre': None,
            'nota_segundo_semestre': 9.0,
            'turma_id': 1
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo nota_primeiro_semestre informado é obrigatório.', r.json()['error'])

    def test_campo_aluno_nota_segundo_semestre_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'nome': 'Bianca',
            'data_nascimento': '03/10/2005',
            'nota_primeiro_semestre': 10.0,
            'nota_segundo_semestre': None,
            'turma_id': 1
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo nota_segundo_semestre informado é obrigatório.', r.json()['error'])
    
    def test_campo_aluno_turma_id_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'nome': 'Beatriz',
            'data_nascimento': '03/10/2005',
            'nota_primeiro_semestre': 5.0,
            'nota_segundo_semestre': 9.0,
            'turma_id': None
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo turma_id informado é obrigatório.', r.json()['error'])
    
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(AlunoTestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()
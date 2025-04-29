import unittest
from TDD.reseTestes import resetar_banco
from TDD.testeAluno import AlunoTestStringMethods
from TDD.testeProfessor import ProfessorTestStringMethods
from TDD.testeTurma import TurmaTestStringMethods
from TDD.testIntegracao import TestIntegracaoGeral

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestIntegracaoGeral))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ProfessorTestStringMethods))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TurmaTestStringMethods))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(AlunoTestStringMethods))

    return suite


if __name__ == '__main__':
    resetar_banco()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())


 

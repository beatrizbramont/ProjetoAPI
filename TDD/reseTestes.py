from config import app, db
from sqlalchemy import text

def resetar_banco():
    try:
        with app.app_context():
            with db.engine.connect() as connection:
                connection.execute(text("PRAGMA foreign_keys = OFF;"))
                connection.execute(text("DELETE FROM Aluno;"))
                connection.execute(text("DELETE FROM Turma;"))
                connection.execute(text("DELETE FROM Professor;"))
                connection.execute(text("PRAGMA foreign_keys = ON;"))
                connection.commit()
            print("Banco resetado com sucesso.")
    except Exception as e:
        print(f"Erro ao resetar o banco: {e}")
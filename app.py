import os
from config import app

from controller.routesAlunos import alunos_bp
from controller.routesProfessor import professor_bp
from controller.routesTurma import turma_bp

# Registrar os blueprints
app.register_blueprint(alunos_bp)
app.register_blueprint(professor_bp)
app.register_blueprint(turma_bp)

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'])


import os
from flask import Flask

app = Flask(__name__)

app.config['HOST'] = '0.0.0.0'
app.config['PORT']= 8001 
#Deixamos como 8001, pois na porta 8000 os testes não rodavam porque a rede tentava
#direcionar para uma porta mais segura
app.config['DEBUG'] = True

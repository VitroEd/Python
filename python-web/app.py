from flask import Flask
from controllers import routs
from models.database import db
import os

#__name__ é o nome padrão a ser definido
#template_folder é pra definir onde esta a pasta views
app = Flask(__name__, template_folder="views" )
#

#função para inicializar as rotas
routs.init_app(app)
#

#permite ler um path ( caminho do sistema operacional )
basedir = os.path.abspath(os.path.dirname(__file__))
#

#é o path do banco
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'models/estudantes.sqlite3')
#

#codigo abaixo para abrir a pagina, debug = True serve pra verificar erros de sintaxe 

if __name__ == "__main__":
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)
from flask import Flask, render_template
from models.database import db, Estudante

#app.route("/") é pra definir a rota para a pagina html
# def [nome]() é como se define uma função
#return render_template("[nome]")

# def init_app é uma função q ja foi definida no app.py

def init_app(app):
    @app.route("/")
    def index():
        estudantes = Estudante.query.all()
        return render_template("index.html", 
                               pEstudantes = estudantes
                               )

    @app.route("/crud")
    def crud():
        return render_template("crud.html")
    
    @app.route("/teste")
    def teste():
        return render_template("teste.html")
    




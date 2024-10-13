from flask import Flask
# Importo flask

def create_app(): #Definisce una funzione chiamata create_app() serve a creare una istanza di Flask, che si crea proprio con Flask(__name__)
    app = Flask(__name__) #__name__ è una variabile speciale che rappresenta il nome del modulo corrente, passandolo a Flask, l'app è in grado capire il percorso relativo delle risorse (template e file statici)
    app.config.from_pyfile('../config.py') # Carica la configurazione da questo file
    from .routes import main # Flask usa i Blueprint per gestire le rotte e modulare l'app, i Blueprint non sono altro che gruppi di rotte registrate su un'istanza dell'app, utile per organizzare l'app in parti logiche
    app.register_blueprint(main) # Registra il Blueprint (rotta) nel Flask
    
    return app # Restituisce l'istanza dell'app configurata    
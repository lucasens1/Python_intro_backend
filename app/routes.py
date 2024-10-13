from flask import Blueprint # L'intera app come detto in init si serve dei Blueprint per creare dei gruppi di rotte quindi nel file delle routes, importiamo e stanziamo le nostre rotte

main = Blueprint('main', __name__) # è il nome del Blueprint usato come riferimeto a questo gruppo di rotte, Blueprint('main', __name__) indica a Flask dove trovare questo modulo e caricare le risorse relative

@main.route('/') #Definisco qui la prima rotta @main.route('/') è un decoratore che associa la funzione home() all'URL '/'
def home():
    return 'Home'
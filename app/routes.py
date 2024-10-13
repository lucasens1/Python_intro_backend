from flask import Blueprint # L'intera app come detto in init si serve dei Blueprint per creare dei gruppi di rotte quindi nel file delle routes, importiamo e stanziamo le nostre rotte
from flask import render_template # Questa importazione permette di renderizzare alla rotta corrispondente un file html

main = Blueprint('main', __name__) # è il nome del Blueprint usato come riferimeto a questo gruppo di rotte, Blueprint('main', __name__) indica a Flask dove trovare questo modulo e caricare le risorse relative

@main.route('/') #Definisco qui la prima rotta @main.route('/') è un decoratore che associa la funzione home() all'URL '/'
def home():
    return render_template('home.html') #renderizza come da nome del metodo il template che va a prendere in automatio dalla cartella templates

@main.route('/about')
def about():
    return render_template('about.html')
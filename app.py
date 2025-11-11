from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = "clave_super_segura"
API = "https://pokeapi.co/api/v2/pokemon/"

@app.route('/search', methods=['POST'])
def busca_pokemon():
    pokemon_name = request.get('pokemon_name','').strip().lower()

    if not pokemon_name:
        flash('Por favor, ingresa un nombre de un pokemon')
        return redirect(url_for('index'))
    
@app.route("/")
def home():
    return redirect(url_for("inicio")) 










if __name__ == "__main__":
    app.run(debug=True)
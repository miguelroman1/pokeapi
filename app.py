
from flask import Flask, render_template, request, redirect, url_for, flash
import requests  

app = Flask(__name__)
app.secret_key = '12345'

API_URL = "https://pokeapi.co/api/v2/pokemon/"

@app.route('/')
def base():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_pokemon():
    pokemon_name = request.form.get('pokemon_name', '').lower().strip()

    if not pokemon_name:
        flash('Por favor ingresa un nombre de Pokémon.')
        return redirect(url_for('base'))


    response = requests.get(API_URL + pokemon_name)
    if response.status_code == 200:
        data = response.json()
        pokemon_info = {
            'name': data['name'].capitalize(),
            'id': data['id'],
            'height': data ['height'] / 10,
            'weight': data ['weight'] / 10,
            'sprite': data['sprites']['front_default'],
            'types' : [t['type']['name'].title()for t in data['types']],
            'abilities': [a['ability']['name'] for a in data['abilities']],
        }
        return render_template('pokemon.html', pokemon=pokemon_info)
    else:
        flash('Pokémon no encontrado.')
        return redirect(url_for('base'))


if __name__ == '__main__':
    app.run(debug=True)

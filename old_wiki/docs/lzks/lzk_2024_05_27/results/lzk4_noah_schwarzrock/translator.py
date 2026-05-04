from flask import Flask, render_template, jsonify
from provided_translator import translate_to_eng

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/translate/<pokemon>')
def translate_pokemon_name(pokemon):
    translated_pokemon = translate_to_eng(pokemon)
    return jsonify(translated_pokemon)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

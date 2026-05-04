from flask import Flask, render_template
from provided_translator import translate_to_eng

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/translate/<pokemonName>', methods=['GET'])
def translate(pokemonName):
    return translate_to_eng(pokemonName)
    


if __name__ == '__main__':
    app.run(debug=True, port=5000)

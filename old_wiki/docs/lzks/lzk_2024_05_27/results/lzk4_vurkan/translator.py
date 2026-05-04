from flask import Flask, render_template,jsonify
from provided_translator import translate_to_eng


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/translate/<pokemon_name>', methods=['GET'])
def translate(pokemon_name):
    translated_name = translate_to_eng(pokemon_name)
    return jsonify({"translated_name": translated_name}), 200




if __name__ == '__main__':
    app.run(debug=True, port=5500)

from flask import Flask, render_template, jsonify, request
from sqlalchemy_translator import translate_to_eng,orm_translate_to_eng
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/translate/<pokemon_name>')
def translate2eng(pokemon_name:str):
    print(f"{pokemon_name}")
    englichername = orm_translate_to_eng(pokemon_name)
    return englichername




if __name__ == '__main__':
    app.run(debug=True, port=5000)

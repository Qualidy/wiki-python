from flask import Flask, render_template, jsonify
# from provided_translator import translate_to_eng
from sqlalchemy_translator import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/translate/<name>', methods=['GET'])
def translate(name):
    name_in_eng = translate_to_eng(name)
    if name_in_eng:
        return jsonify({'name': name_in_eng}), 200
    return jsonify({'error': 'can not find pokemon'}), 400



if __name__ == '__main__':
    app.run(debug=True, port=5000)

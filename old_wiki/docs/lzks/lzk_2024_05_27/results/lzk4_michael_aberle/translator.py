from flask import Flask, render_template, jsonify
from sqlalchemy_translator import translate_to_eng


app = Flask(__name__)


@app.route("/translate/<pokename>")
def translate(pokename):
    
    return jsonify(translate_to_eng(pokename).lower())


@app.route("/")
def home():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)

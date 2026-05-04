from flask import Flask, render_template, jsonify
from provided_translator import translate_to_eng
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/translate/<name>', methods =["GET"])
def translate(name):
    translate = translate_to_eng(name)
    return jsonify(translate)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

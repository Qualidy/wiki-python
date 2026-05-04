from flask import Flask, render_template, jsonify
import provided_translator as pt
import sqlalchemy_translator as sqlt

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/translate/<name>')
def translate(name):
    return jsonify(sqlt.translate_to_eng(name))


if __name__ == '__main__':
    app.run(debug=True, port=5000)

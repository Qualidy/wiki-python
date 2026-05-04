from flask import Flask, render_template, jsonify
#from provided_translator import translate_to_eng
from sqlalchemy_translator import translate_to_eng

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.get('/translate/<name>')
def translate(name: str):
    trans_name = translate_to_eng(name)
    return jsonify({'name': trans_name, 'success': bool(trans_name)})


if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Flask, render_template, jsonify
from provided_translator import translate_to_eng

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/translate/<string:name>', methods=['GET'])
def translate(name):
    # print(translate_to_eng(name))
    eng_name = translate_to_eng(name)
    return jsonify({'name': name, 'eng_name': eng_name})

if __name__ == '__main__':

    app.run(debug=True, port=5000)


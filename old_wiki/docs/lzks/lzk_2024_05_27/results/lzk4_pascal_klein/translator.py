from flask import Flask, render_template, request, jsonify
from provided_translator import translate_to_eng

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/translate/<string:name>')
def translate(name):
    english_name = translate_to_eng(name)
    if english_name:
        return jsonify({"english_name": english_name})
    else:
        return jsonify({"error": "Pokemon not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)
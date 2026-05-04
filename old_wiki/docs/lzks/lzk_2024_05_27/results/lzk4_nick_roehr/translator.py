from flask import Flask, render_template,jsonify
from flask_cors import CORS
from provided_translator import translate_to_eng

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/translate/<pokemon>',methods=['GET'])
def translate(pokemon):
    p = translate_to_eng(pokemon)
    return jsonify(p)
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)

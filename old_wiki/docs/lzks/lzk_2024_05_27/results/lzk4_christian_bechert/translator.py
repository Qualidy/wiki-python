from flask import Flask, render_template, request, jsonify
from provided_translator import translate_to_eng
# from sqlalchemy_translator import translate_to_eng as sql_translator

app = Flask(__name__)


@app.route('/', methods= ['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('main.html')
        
        
        

@app.route('/translate/<pokemon>', methods=['GET','POST'])
def translate(pokemon):
    if request.method == 'GET':
        return translate_to_eng(pokemon.capitalize())


if __name__ == '__main__':
    app.run(debug=True, port=5000)

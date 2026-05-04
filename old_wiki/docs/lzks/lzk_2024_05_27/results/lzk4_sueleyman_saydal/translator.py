
from flask import Flask, render_template
from provided_translator import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/translate', methods=['GET'])
def translate_name():
    return "Test"

if __name__ == '__main__':
    app.run(debug=True, port=5000)


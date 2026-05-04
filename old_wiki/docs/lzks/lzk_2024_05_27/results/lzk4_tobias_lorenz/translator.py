from flask import Flask, render_template
import provided_translator

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/translate')
def translate_to_eng():
    return provided_translator.translate_to_eng("main.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)

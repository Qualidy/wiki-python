from flask import Flask, render_template, redirect, url_for, request
import provided_translator

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.get("/translate/<name>")
def translate(name):
    return provided_translator.translate_to_eng(name)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

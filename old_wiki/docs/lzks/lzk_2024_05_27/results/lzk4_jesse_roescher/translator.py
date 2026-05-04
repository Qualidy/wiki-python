from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.get("/translate/<name>")
def translate_to_eng(name):
    pass
    




if __name__ == '__main__':
    app.run(debug=True, port=5001)

from flask import Flask, render_template, request, jsonify
from sqlalchemy_translator import translate_to_eng

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/translate')
def translate():
    poke_name = request.args.get("name")
    print(poke_name)
    eng_name = translate_to_eng(poke_name).lower()
    return jsonify({"eng_name": eng_name}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)

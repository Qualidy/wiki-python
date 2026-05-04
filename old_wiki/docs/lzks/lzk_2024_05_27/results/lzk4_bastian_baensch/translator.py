from flask import Flask, render_template, jsonify
from sqlalchemy_translator import translate_to_eng

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main.html")

@app.get("/translate/<name>")
def translate(name):
    english_name = translate_to_eng(name)
    if english_name:
        return jsonify({"english_name": english_name}), 200
    else:
        return jsonify({"error": "Pokemon nicht gefunden."}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5001)

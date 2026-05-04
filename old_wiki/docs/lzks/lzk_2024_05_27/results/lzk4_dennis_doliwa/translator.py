from flask import Flask, render_template , jsonify, redirect, request, url_for, provided

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')




@app.get("/get_pokemon_by_name/<name>")
def get_pokemon(name):
    pokemon = provided_translator.get_pokemon_by_name(name)
    return jsonify({
            'name': pokemon.name,
        })




if __name__ == '__main__':
    app.run(debug=True, port=5000)

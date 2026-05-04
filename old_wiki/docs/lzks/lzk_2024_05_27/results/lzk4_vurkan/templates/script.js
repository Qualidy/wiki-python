async function getPokemon() {
    let char_name = document.getElementById("char_name").value.trim().toLowerCase();
    let translatedName = await translatePokemonName(char_name);

    let get_url = `https://pokeapi.co/api/v2/pokemon/${translatedName}`;
    let response = await fetch(get_url);
    let data = await response.json();
    displayData(data);
}

async function translatePokemonName(name) {
    let response = await fetch(`http://127.0.0.1:5500/translate/${name}`);
    let data = await response.json();
    return data.translated_name;
}

function displayData(data) {
    let textfeld = document.getElementById("textfeld");
    let htmlContent = ``;
    textfeld.innerHTML = htmlContent;
    document.getElementById("pokemon_bild").src = data.sprites.front_default;
}
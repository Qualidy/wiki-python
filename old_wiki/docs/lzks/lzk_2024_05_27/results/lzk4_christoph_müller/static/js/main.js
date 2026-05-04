let loadedPokemon = null

async function loadPokemon (name) {
    let response = await fetch(`https://pokeapi.co/api/v2/pokemon/${name}`)
    loadPokemon = await response.json()

    document.querySelector("#pokemon_img").innerHTML = loadedPerson.name


}
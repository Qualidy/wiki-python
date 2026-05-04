"use strict";

const btn = document.getElementById("pkmn_button");
const img_prev = document.getElementById("pkmn_previewer");
const pkmn_input_name = document.getElementById("input_name");

btn.addEventListener("click", () => {
    let pkmn_name = pkmn_input_name.value;
    if (pkmn_name != "") {
        fetch(`http://127.0.0.1:5000/translate/${pkmn_name}`)
        .then(response => {return response.json()})
        .then(data => {
            if (data.success) {
                img_prev.alt = data.name;
                fetch(`https://pokeapi.co/api/v2/pokemon/${data.name.toLowerCase()}`)
                .then(response => response.json())
                .then(data => {
                    let img_url = data.sprites.front_default;
                    console.log(img_url);
                    img_prev.src = img_url;
                });

            } else {
                alert("this name doesn't exist!");
            }
        });
    } else {
        alert("You need to input a pokemon name first!");
    }
    
});
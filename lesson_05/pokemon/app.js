document.querySelector('button').addEventListener('click', getFetch)
fetch('https://pokeapi.co/api/v2/pokemon/')
    .then(res => res.json())
    .then(data => {
        console.log(data)
    })


async function getFetch() {
    const choice = document.querySelector('input').value
    const url = 'https://pokeapi.co/api/v2/pokemon/'+choice

    try {
        let data = await fetch(url);
        let pokemonInfo = await data.json();
    
        let pic = pokemonInfo.sprites.front_default;
    
        if(document.querySelector('#shinyBox').checked){
            pic = pokemonInfo.sprites.front_shiny;
        }
    
        console.log(pokemonInfo);
        document.querySelector('h2').innerHTML = pokemonInfo.species.name;
        document.querySelector('img').src = pic;
        document.querySelector('h3').innerHTML = pokemonInfo.types[0].type.name;
    } catch (error){
        document.querySelector('h2').innerHTML = 'Pokemon not found, check spelling'
        console.error(error)
    }
}
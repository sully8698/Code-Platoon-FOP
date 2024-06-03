document.querySelector('button').addEventListener('click', getFetch);
const url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY';

fetch('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
    .then(res => res.json())
    .then(data => {
        console.log(data)
    })

async function getFetch() {
    const dateChoice = document.querySelector('input').value;
    const data = await fetch(url+`&date=${dateChoice}`);
    const info = await data.json();
    console.log(info)
    document.querySelector('img').src = info.url
}  
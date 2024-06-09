document.querySelector('button').addEventListener('click', getFetch);
const url = 'https://api.nasa.gov/planetary/apod?api_key=yF5P7muYQuWPROCRclCcJdtGk65LCjY7sV3SR7LB';
// api key yF5P7muYQuWPROCRclCcJdtGk65LCjY7sV3SR7LB
fetch('https://api.nasa.gov/planetary/apod?api_key=yF5P7muYQuWPROCRclCcJdtGk65LCjY7sV3SR7LB')
    .then(res => res.json())
    .then(data => {
        console.log(data)
    })

async function getFetch() {
    const dateChoice = document.querySelector('input').value;
    const data = await fetch(url+`&date=${dateChoice}`);
    const info = await data.json();
    console.log(info);
    if (info.media_type === "image"){
        document.querySelector('img').src = info.url;
    } else {
        document.querySelector('h2').innerHTML = "image type is a video, third party cookies may have been blocked";
        document.querySelector('img').alt = info.url;
        document.querySelector('img').src = info.url;
    }
}  
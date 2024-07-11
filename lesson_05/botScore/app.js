localStorage.getItem('count', 0)

let getStr = localStorage.getItem('count')

document.querySelector('h4').innerHTML = getStr
console.log(getStr)

document.querySelector('#addOne').addEventListener('click', addOne)
document.querySelector('#minusOne').addEventListener('click', minusOne)
document.querySelector('#zero').addEventListener('click', zero)
function addOne() {
    localStorage.count++;
    document.querySelector('h4').innerHTML = localStorage.count;
}

function minusOne() {
    localStorage.count--;
    document.querySelector('h4').innerHTML = localStorage.count;
}

function zero (){
    localStorage.count = 0;
    document.querySelector('h4').innerHTML = localStorage.count;
}
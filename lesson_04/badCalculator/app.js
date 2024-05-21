let total = '';

// all the buttons that listen for a click
document.querySelector('#clear').addEventListener('click', clear);
document.querySelector('#zero').addEventListener('click', zero);
document.querySelector('#one').addEventListener('click', one);
document.querySelector('#two').addEventListener('click', two);
document.querySelector('#three').addEventListener('click', three);
document.querySelector('#four').addEventListener('click', four);
document.querySelector('#five').addEventListener('click', five);
document.querySelector('#six').addEventListener('click', six);
document.querySelector('#seven').addEventListener('click', seven);
document.querySelector('#eight').addEventListener('click', eight);
document.querySelector('#nine').addEventListener('click', nine);
document.querySelector('#plus').addEventListener('click', plus);
document.querySelector('#minus').addEventListener('click', minus);
document.querySelector('#multiply').addEventListener('click', multiply);
document.querySelector('#divide').addEventListener('click', divide);
document.querySelector('#equal').addEventListener('click', equal);

// button functions
function clear() {
  total = '0';
  document.querySelector('#result').innerText = total;
}
function zero(){
  total += '0'
  document.querySelector('#result').innerHTML = total
}
function one(){
  total += '1'
  document.querySelector('#result').innerHTML = total
}
function two(){
  total +='2'
  document.querySelector('#result').innerHTML = total
}
function three(){
  total += '3'
  document.querySelector('#result').innerHTML = total
}
function four(){
  total += '4'
  document.querySelector('#result').innerHTML = total
}
function five(){
  total += '5'
  document.querySelector('#result').innerHTML = total
}
function six(){
  total += '6'
  document.querySelector('#result').innerHTML = total
}
function seven(){
  total += 7
  document.querySelector('#result').innerHTML = total
}
function eight(){
  total += '8'
  document.querySelector('#result').innerHTML = total
}
function nine(){
  total += '9'
  document.querySelector('#result').innerHTML = total
}
function plus(){
  total += ' + ';
  document.querySelector('#result').innerHTML = total;
}
function minus(){
  total += ' - ';
  document.querySelector('#result').innerHTML = total;
}
function multiply(){
  total += ' * ';
  document.querySelector('#result').innerHTML = total;
}
function divide(){
  total += ' / ';
  document.querySelector('#result').innerHTML = total;
}

function equal(){
  let totalArr = total.split(" ");
  let answer = Number(totalArr[0]);
  for (let i = 1; i < totalArr.length; i+=2){
    console.log(answer)
    if (totalArr[i] === "+"){
      answer += Number(totalArr[i+1])
    } else if (totalArr[i] === "-"){
      answer -= Number(totalArr[i+1])
    } else if (totalArr[i] === "*"){
      answer *= Number(totalArr[i+1])
    } else if (totalArr[i] === "/"){
      answer /= Number(totalArr[i+1])
    }
  }
  console.log(answer)
  total = answer;
  document.querySelector('#result').innerText = total;

}







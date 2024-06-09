document.querySelector('button').addEventListener('click', addItem);
document.querySelector('#save').addEventListener('click', save);
const unorderedList = document.querySelector('ul');

let storageObj = {}

if ('currentList' in localStorage) {
    const storedObj = localStorage.getItem('currentList')
    storageObj = JSON.parse(storedObj)
    window.onload = showStoredList(storageObj)
}
  

function addItem() {
    let userInput = document.querySelector('input').value;
    let newTodo = document.createElement('li');

    let userInputObj = {listItem: userInput, class: "not-complete"};
    storageObj[userInput] = userInputObj;
    console.log(storageObj)

    newTodo.innerHTML = userInput;
    newTodo.classList.add('not-complete');

    let deleteButton = document.createElement('button');
    deleteButton.innerHTML = "DELETE";
    
    
    deleteButton.addEventListener('click', () => {
        delete storageObj[userInput]
        console.log(storageObj)
        let listItem = deleteButton.parentNode
        listItem.parentNode.removeChild(listItem)
    });

    newTodo.addEventListener('click', () => {
        if (newTodo.className === 'complete') {
            newTodo.classList = 'not-complete';
            storageObj[userInput].class = 'not-complete'
            console.log(storageObj)
        } else {
            newTodo.classList = 'complete'
            storageObj[userInput].class = 'complete' 
            console.log(storageObj)
        }  
    })
    

    newTodo.appendChild(deleteButton)
    unorderedList.appendChild(newTodo);
}


function showStoredList(arg){
    console.log(arg)
    for (const element in arg) {
        console.log(arg[element])
        let userInput = arg[element].listItem;
        let newTodo = document.createElement('li');

        newTodo.innerHTML = userInput;
        newTodo.classList.add(arg[element].class);

        let deleteButton = document.createElement('button');
        deleteButton.innerHTML = "DELETE";
        
        
        deleteButton.addEventListener('click', () => {
            delete storageObj[userInput]
            console.log(storageObj)
            let listItem = deleteButton.parentNode
            listItem.parentNode.removeChild(listItem)
        });

        newTodo.addEventListener('click', () => {
            if (newTodo.className === 'complete') {
                newTodo.classList = 'not-complete';
                storageObj[userInput].class = 'not-complete'
                console.log(storageObj)
            } else {
                newTodo.classList = 'complete'
                storageObj[userInput].class = 'complete' 
                console.log(storageObj)
            }  
    })
    

    newTodo.appendChild(deleteButton)
    unorderedList.appendChild(newTodo);
    };
}

function save() {
    let stringedObj = JSON.stringify(storageObj)
    localStorage.setItem('currentList', stringedObj)
}
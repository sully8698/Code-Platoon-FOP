

fetch('https://www.thecocktaildb.com/api/json/v1/1/search.php?s')
    .then(res => res.json()) // parse response as JSON
    .then(data => {
      console.log(data)
    })
    .catch(err => {
        console.log(`error ${err}`)
    });
  


function cocktailInfo() {
  let drinkSelect = document.querySelector("input").value;
  
  fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${drinkSelect}`)
      .then(res => res.json()) // parse response as JSON
      .then(data => {
        let drinkShow = {};
        const drinksArr = data.drinks;
        for (let i = 0; i < drinksArr.length; i++){
          if (drinkSelect.toLowerCase() === drinksArr[i].strDrink.toLowerCase()){
            drinkShow = drinksArr[i];
            console.log(drinkShow);
            break;
          } else { drinkShow = drinksArr[0]}
        }
        if (Object.keys(drinkShow).length > 1){
          document.querySelector('h2').innerHTML = drinkShow.strDrink;
          document.querySelector('img').src = drinkShow.strDrinkThumb;
          document.querySelector('h3').innerHTML = drinkShow.strInstructions;
        } else {
          document.querySelector('h2').innerHTML = "No Cocktail found, check spelling"
        }
       
        console.log(data)
      })
      .catch(err => {
          console.log(`error ${err}`)
      });
    }


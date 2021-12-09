// window.onload = function() {
// document.getElementById("search").addEventListener("click", search());
// }

function search() {
  let request = new XMLHttpRequest();
  let url =
    "https://www.thecocktaildb.com/api/json/v2/9973533/filter.php?a=non_alcoholic";
  // url = getURL();
  request.open("GET", url, true);
  request.onload = function() {
    let data = JSON.parse(this.response);
    let counter = 0;
    let row = 0;
    let drinks = [];
    let id = null;
    let list = document.getElementById("list");
    let request2 = new XMLHttpRequest();
    let url2 = "www.thecocktaildb.com/api/json/v1/1/lookup.php?i=" + id;

    data.drinks.forEach(drink => {
      if (counter % 4 == 0) {
        // % gets the remainder of current pokemon counter (not division)
        row = document.createElement("div");
        row.className = "row";
        list.appendChild(row);
      }
      //create new div of col-3 (to fit 4 in a row since 3x4 = 12)
      let poster = document.createElement("div");
      poster.className = "col-3 drink ";
      // display the pokemon name
      let img = document.createElement("img");
      img.src = data.drinks[counter].strDrinkThumb;
      let name = document.createElement("h3");
      name.innerHTML = data.drinks[counter].strDrink;
      let id = data.drinks[counter].idDrink;
      request2.open("GET",url2,true);
      let dataID = JSON.parse(this.response);
      
      //Append the name to the column div and column to the row
      //for (let i = 0; i < 15; i++){
      //if (data.drinks[counter].)
      poster.appendChild(img);
      poster.appendChild(name);
      row.appendChild(poster);

      counter++;
    });
//     let request2 = new XMLHttpRequest();
//     let url2 =
//       "www.thecocktaildb.com/api/json/v1/1/lookup.php?i=" + idFromArray;
//     for (let i = 0; i < drinks.length; i++) {
      
//     }
  };

  request.send();
}


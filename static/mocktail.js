// window.onload = function() {
// document.getElementById("search").addEventListener("click", search());
// }
function randomMock(){
  let request = new XMLHttpRequest();
  let url = "https://www.thecocktaildb.com/api/json/v2/9973533/filter.php?a=non_alcoholic";
  request.open("GET", url, true);
  request.onload = function() {
    let data = JSON.parse(this.response);
    let num = Math.floor(Math.random() * 5);
     let poster = document.createElement("div");
    poster.className = "randoDrink";
    let list = document.getElementById("randoList");
      
      console.log(num);
    console.log(data.drinks[num].strDrinkThumb);
      let img = document.createElement("img");
      img.src = data.drinks[num].strDrinkThumb;
      let name = document.createElement("h3");
      name.innerHTML = data.drinks[num].strDrink;
      const button = document.createElement("button");
      button.innerHTML = "Click for more info";
       
        
      list.append(poster);
      poster.appendChild(img);
      poster.appendChild(name);
      poster.appendChild(button);
    console.log("Yes");
  }
  request.send();
}
function search(drinks) {
  // let request = new XMLHttpRequest();
  // let url =
  //   "https://www.thecocktaildb.com/api/json/v2/9973533/filter.php?a=non_alcoholic";
  // // url = getURL();
  // request.open("GET", url, true);
  // request.onload = function() {
  //   let data = JSON.parse(this.response);
  //   let counter = 0;
  //   let row = 0;

  //   let list = document.getElementById("list");
  console.log("In")  
  console.log(drinks)

    drinks.forEach(drink => {
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
      const button = document.createElement("button");
      button.innerHTML = "Click for more info";
 
      row.appendChild(poster);
      poster.appendChild(img);
      poster.appendChild(name);
      poster.appendChild(button);
      
      

      counter++;
    });
  
  //};

  request.send();
}
// var non = 'nonalc.json';
//  console.log(non.hits[0].idDrink);

function clearPage() {
    let list = document.getElementById("list");
    list.innerHTML = "";
}


let place = document.getElementById("content-data");
let openStatus = false
let SearchBar = document.getElementById("MySearch");


async function openPopup() {

  if (openStatus == false) {

    let getData = await fetch('http://127.0.0.1:8000/toilet');
    let data = await getData.json();
    data = data["data"]
    
    var index;
    for (index = 0; index < data.length; ++index) {
      let span = document.createElement('p');
      span.innerHTML = data[index]["title"] + " - " + data[index]["description"]
      place.appendChild(span)
    }

    document.getElementById("popup").style.display = "block";
    ;
    openStatus = true
  }
}
function closePopup() {
  openStatus = false

  place.innerHTML = ""
  document.getElementById("popup").style.display = "none";
}

function getSearchData() {
  console.log(SearchBar.value)
  
  
  




}
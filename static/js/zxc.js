let place = document.getElementById("content-data");
let openStatus = false
let SearchBar = document.getElementById("MySearch");



async function openPopup() {
  

  if (openStatus == false) {
    openStatus = true

    let getData = await fetch('http://127.0.0.1:8000/toilet');
    let data = await getData.json();
    data = data["data"]

    if (data.length == 0) {

      place.innerHTML = ""
      let el = document.createElement('h2');
      el.innerHTML = "По такому запросу ничего не найдено"
      place.appendChild(el)

    }

    else{

      var index;
      for (index = 0; index < data.length; ++index) {
      let span = document.createElement('p');
      span.className = "content-unitasis"
      span.innerHTML = data[index]["title"] + " - " + data[index]["description"]
      place.appendChild(span)
    }

    }


    
    

    document.getElementById("popup").style.display = "block";
    ;
    
  }
}
function closePopup() {
  openStatus = false

  place.innerHTML = ""
  document.getElementById("popup").style.display = "none";
}



async function getSearchData() {
    let GetData = await fetch("http://127.0.0.1:8000/toilet/search", {
    method: "POST",
    body: JSON.stringify({
      title : SearchBar.value
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  });

    let data = await GetData.json();

    


    if (data["count"] == 0) {
      place.innerHTML = ""
      let el = document.createElement('h2');
      el.innerHTML = "По такому запросу ничего не найдено"
      place.appendChild(el)

    }

    else{
      place.innerHTML = ""

      for (index = 0; index < data["data"].length; ++index) {
        
        let span = document.createElement('p');
        
        span.innerHTML = data["data"][index]["title"] + " - " + data["data"][index]["description"]
        span.className = "content-unitasis"
        place.appendChild(span)
      }

    }


  



    



}

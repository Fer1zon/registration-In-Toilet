let place = document.getElementById("content-data");


async function openPopup() {
    

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
    
  }
  
function closePopup() {
    place.innerHTML = ""
    document.getElementById("popup").style.display = "none";
}
let place = document.getElementById("content-data");


async function openPopup() {
  console.log("sda")

    let getData = await fetch('http://127.0.0.1:8000/toilet');
    let data = await getData.json();
    data = data["data"]

    
    let getData1 = await fetch("http://127.0.0.1:8000/toilet/search", {"title" : "Дешевый туалет"});
    let data1 = await getData1.json();

    
    
    
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
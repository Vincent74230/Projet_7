//The code below is responsible for retreiving user's question.
let button = document.getElementById("button");
let form = document.getElementById("form");
let text = document.getElementById("question");
var myString = '';
var googleMap = document.getElementById("googleMap");
var img = document.createElement("img");

form.addEventListener("submit", function(e){

    e.preventDefault();
    myString = text.value

    console.log(text.value);
    text.value = '';
});
/////////////////////////////////////////////////////////////////


//The code below is responsible for asking a map to google api and displaying it
//it takes 2 numbers : lontitude and latitude
////////////////////////////////////////////////////////////////////
// Creating the script tag, setting the appropriate attributes
var script = document.createElement("script");
script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyBvjVqsDCXUG3xGNdZai3lQBkekuMbUAfk&callback=initMap';
script.defer = true;
script.async = true;
// google maps api key = AIzaSyBvjVqsDCXUG3xGNdZai3lQBkekuMbUAfk
//attaching the callback function to the 'window' object
window.initMap = function() {
    map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -34.397, lng: 150.644},
          zoom: 8
});
}

// Append the 'script' element to 'head'
document.head.appendChild(script);
////////////////////////////////////////////////////////////////////

//The code below is responsible for retreiving user's question.
let form = document.getElementById("form");
let text = document.getElementById("question");



form.addEventListener("submit", function(e){

    e.preventDefault();

    let question = text.value
    console.log(question)
    let users_question = new FormData();
    users_question.append("question", question);
    console.log(users_question);
    let request = new XMLHttpRequest();
    request.open("POST", "/users_question");
    request.send(users_question);
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
          center: {lat:40.000 , lng:5.000},
          //annecy : center: {lat:45.889 , lng:6.129},
          zoom: 8
});
    console.log(script);
}
console.log(script);
// Append the 'script' element to 'head'
document.head.appendChild(script);
////////////////////////////////////////////////////////////////////
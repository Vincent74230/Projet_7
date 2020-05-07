
// google maps api key = AIzaSyBvjVqsDCXUG3xGNdZai3lQBkekuMbUAfk

let button = document.getElementById("button");
let form = document.getElementById("form");

let text = document.getElementById("question");

form.addEventListener("submit", function(e){
    var quest = text.value;
    console.log(e,quest);

    e.preventDefault();
});


var request = new XMLHttpRequest();
request.onreadystatechange = function(){
    if (this.readyState == XMLHttpRequest.DONE && this.status == 200){
        var response = request.response;

    }
}

request.open('get', "https://maps.googleapis.com/maps/api/staticmap?center=Berkeley,CA&zoom=14&size=400x400&key=AIzaSyBvjVqsDCXUG3xGNdZai3lQBkekuMbUAfk");
request.send();

console.log(request);
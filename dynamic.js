
// google maps api key = AIzaSyBvjVqsDCXUG3xGNdZai3lQBkekuMbUAfk
// api request example = "https://maps.googleapis.com/maps/api/staticmap?center=pyramide de gizeh&zoom=14&size=400x400&key=AIzaSyBvjVqsDCXUG3xGNdZai3lQBkekuMbUAfk"

let button = document.getElementById("button");
let form = document.getElementById("form");
let text = document.getElementById("question");
var myString = '';
var googleMap = document.getElementById("googleMap");
var img = document.createElement("img");

form.addEventListener("submit", function(e){

    e.preventDefault();
    var myString1 = "https://maps.googleapis.com/maps/api/staticmap?center=";
    var myString2 = "&zoom=14&size=400x400&key=AIzaSyBvjVqsDCXUG3xGNdZai3lQBkekuMbUAfk";
    myString = myString1+text.value+myString2;

    img.src = myString;
    googleMap.appendChild(img);
    text.value = '';
});

/*
var map;
var xhr = new XMLHttpRequest();
xhr.addEventListener('readystatechange', function(){
    if (xhr.readyState === 4 && xhr.status === 200){
        map = xhr;
    }
        
});

xhr.open('get', "https://maps.googleapis.com/maps/api/staticmap?center=Chicago&zoom=14&size=400x400&key=************************");
xhr.send();
*/



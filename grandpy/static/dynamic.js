let form = document.getElementById("form");
let text = document.getElementById("question");
let displayBox = document.getElementById("display");
let displayAddress = document.getElementById('address');

function googleMaps (lat,lng){
    var script = document.createElement("script");
    script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyBvjVqsDCXUG3xGNdZai3lQBkekuMbUAfk&callback=initMap';
    script.defer = true;
    script.async = true;
    //attaching the callback function to the 'window' object
    window.initMap = function() {
        map = new google.maps.Map(document.getElementById('map'), {
              center: {lat:lat, lng:lng},
              zoom: 12
    });
    }
    // Append the 'script' element to 'head'
    document.head.appendChild(script);
    }

function displayQuestion (text){
    displayBox.innerHTML += text+'<br>';
}

function speech_bubbles (users_question, grandpy_response){
    
}

form.addEventListener("submit", function(e){
    e.preventDefault();
    let question = text.value;
    let users_question = new FormData();
    users_question.append("question", question);
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            data=this.response;
            console.log(data);
            googleMaps(data.geoloc.position.lat, data.geoloc.position.lng);
            displayAddress.innerHTML = 'This is the address of this place:<br>'+data.geoloc.address+data.bla_bla;
        }
    }

    request.open("POST", "/users_question");
    request.responseType = "json";
    request.send(users_question);
    displayQuestion(question);
    
    text.value = '';
});

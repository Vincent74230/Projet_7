let form = document.getElementById("form");
let text = document.getElementById("question");
let speechBox = document.getElementById("speechBox");

function googleMaps (latitude,longitude){
    const coordinates = {lat:latitude, lng:longitude};
    const map = new google.maps.Map(document.getElementById("map"),{
        center: coordinates,
        zoom: 12
    });
    const marker = new google.maps.Marker({
        position: coordinates,
        map:map
    });
}

function speech_bubbles (users_question, grandpy_response){
    let newUserQuestionBox = document.createElement("div");
    newUserQuestionBox.classList.add("userSpeechBox");
    speechBox.appendChild(newUserQuestionBox);
    let newUserQuestion = document.createElement("p");
    newUserQuestion.classList.add("userQuestion");
    newUserQuestionBox.appendChild(newUserQuestion);
    newUserQuestion.innerHTML = users_question;

    let newGrandpyResponseBox = document.createElement("div");
    newGrandpyResponseBox.classList.add("grandPySpeechBox");
    speechBox.appendChild(newGrandpyResponseBox);
    let newGrandpyAnswer = document.createElement("p");
    newGrandpyAnswer.classList.add("grandPyAnswer");
    newGrandpyResponseBox.appendChild(newGrandpyAnswer);
    newGrandpyAnswer.innerHTML = grandpy_response;
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
            googleMaps(data.geoloc.position.lat, data.geoloc.position.lng);
            speech_bubbles(question,'hello youngster, the address of this place is:'+data.geoloc.address+data.bla_bla);
        }
    }

    request.open("POST", "/users_question");
    request.responseType = "json";
    request.send(users_question);
    
    text.value = '';
});

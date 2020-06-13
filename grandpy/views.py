'''Module that contains the flask app and the routes between back and front'''
import random
from flask import Flask, render_template, request
from .parser import parser
from .get_position import Get_position
from .get_wiki_summary import Get_wiki_summary

app = Flask(__name__)

def grandpy_answer():
    '''no arguments, returns a random sentence'''
    examples = ["Oh I've been there once, the address : ",
                "I went there long time ago, the location is : ",
                "I know exactly where it is..",
                "I've already been there, youngster, the address is : "]
    return random.choice(examples)

@app.route('/')
def home():
    '''leads to home page'''
    return render_template('index.html')

@app.route('/users_question', methods=['POST'])
def search():
    '''leads to user question'''
    position = Get_position()
    description = Get_wiki_summary()
    if request.method == 'POST':
        users_question = request.form['question']
        place_in_the_world = parser(users_question)
        if place_in_the_world:
            if position.send_request(place_in_the_world):
                if description.send_request(place_in_the_world):
                    return {'geoloc' : position.send_request(place_in_the_world), 
                            'bla_bla' : description.send_request(place_in_the_world), 
                            'grandpy_sentence' : grandpy_answer(), 'parser_answer':'ok'}
                else:
                    return {'geoloc' : position.send_request(place_in_the_world), 
                            'bla_bla' : "I know where it is but I can't remember any story about that..", 
                            'grandpy_sentence' : grandpy_answer(), 'parser_answer' : 'ok'}
            else:
                return {'geoloc' : 'not_ok', 
                        'bla_bla' : "Say it again son, I only have an Intel 486 as brain..", 
                        'parser_answer' : 'ok'}
        else:
            return {'grandpy_sentence' : "Ask me a question please, type it in the little window..", 
                    'parser_answer' : 'not_ok'}

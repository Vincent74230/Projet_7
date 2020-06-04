from flask import Flask, render_template, request
from parser import parser
from get_position import get_position
from get_wiki_summary import get_wiki_summary

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/users_question', methods= ['POST'])
def search():
    if request.method == 'POST':
        users_question = request.form['question']
        place_in_the_world = parser(users_question)
        return {'geoloc':get_position(place_in_the_world),'bla_bla':get_wiki_summary(place_in_the_world)}

if __name__ == '__main__':
    app.run(debug = True)

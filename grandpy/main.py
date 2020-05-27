from flask import Flask, render_template, request
from parser import parser
from get_position import get_position

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/users_question', methods= ['POST'])
def search():
    if request.method == 'POST':
        users_question = request.form['question']
        magic_word = parser(users_question)
        return get_position(magic_word)

if __name__ == '__main__':
    app.run(debug=True)

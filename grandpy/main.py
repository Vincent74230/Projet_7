from flask import Flask, render_template, request

app = Flask(__name__)


def f():# pytest trial
    return "Tout fonctionne"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/users_question', methods= ['POST'])
def search():
    if request.method == 'POST':
        users_question = request.form['question']
        print (users_question)
        return 'Ok'

"""
@app.route('/', methods=['GET','POST'])
def home():

    if request.method == 'POST':
        users_question = request.form['question']
        print (users_question)

    return render_template('index.html')

def parser():
    return users_question
"""

if __name__ == '__main__':
    app.run(debug=True)

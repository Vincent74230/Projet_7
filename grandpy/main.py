from flask import Flask, render_template, request

app = Flask(__name__)

users_question = ''


def f():
    return "Tout fonctionne"


@app.route('/', methods=['GET','POST'])
def home():

    if request.method == 'POST':
        users_question = request.form['question']
        print (users_question)

    return render_template('index.html')


def parser():
    return users_question

if __name__ == '__main__':
    app.run(debug=True)

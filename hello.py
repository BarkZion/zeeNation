from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello hello hello'


@app.route('/hello/')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/manager/')
def manager(name=None):
    return render_template('manager.html')


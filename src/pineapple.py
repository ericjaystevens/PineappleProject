from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/pineapple/')
@app.route('/pineapple/<int:amount>')
def pineapple(amount=None):
    return render_template('pineapple.html', amount=amount)
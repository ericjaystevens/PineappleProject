from flask import Flask
from flask import render_template
import requests
import json


app = Flask(__name__)

@app.route('/')
def welcome():
    msg = 'Welcome!' 
    msg += '</br> <a href=../pineapple> Pineapples </a>'
    msg += '</br> <a href=../pineapple/ready/1> When </a>'
    return msg

@app.route('/pineapple/')
@app.route('/pineapple/<int:amount>')
def pineapple(amount=None):
    return render_template('pineapple.html', amount=amount)

@app.route('/pineapple/ready/<int:smellStrength>')
def getDaysUntilReady(smellStrength):
    lookupUrl = "https://s3.us-east-2.amazonaws.com/pineapplecharts/readyLookup.json"

    lookUpTable = json.loads(requests.get(lookupUrl).text)

    for prediction in lookUpTable:
        if prediction["SmellStrength"] == smellStrength:
            days = prediction["daysFromBeingReady"]

    return render_template('readytoeat.html', days=days)

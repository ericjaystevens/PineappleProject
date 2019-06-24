from flask import Flask
from flask import render_template
import requests, json

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
    # Pass the amount and display it with Jinja2 template.
    return render_template('pineapple.html', amount=amount)

@app.route('/pineapple/ready/<int:smellStrength>')
def displayUntilReady(smellStrength):   
    lookUpTable = getLookupTable()
    days = getDaysUntilReady(smellStrength, lookUpTable)
    return render_template('readytoeat.html', days=days)

def getDaysUntilReady(smellStrength, lookUpTable):
    # Use the lookup table to determine days until ready
    for prediction in lookUpTable:
        if prediction["SmellStrength"] == smellStrength:
            days = prediction["daysFromBeingReady"]
    return days

def getLookupTable():
    # Download smell strength to ready lookup table
    lookupUrl = "https://s3.us-east-2.amazonaws.com/pineapplecharts/readyLookup.json"
    lookUpTable = json.loads(requests.get(lookupUrl).text)
    return lookUpTable


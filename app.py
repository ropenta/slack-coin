from flask import Flask, render_template, redirect, url_for, session, request, jsonify, abort
import requests
import json
import os

app = Flask(__name__)
build_notes = {
    0: 'learn flask and its API',
    1: 'build app.py, requirements.txt, runtime.txt, and Procfile',
    2: 'learn Heroku\'s HTTP server hosting, and get its url',
    3: 'connect server with Slack and get slash command \bitcoin to return link to webpage',
    4: 'work out details of retreiving currency data, possibly graphs, with app and bot.py',
    5: 'connect again with Slack and run \bitcoin to get useful info in the chatbox'
}

exampleworldcoinindex = {
    "Label": "ETH/BTC",
    "Name": "Ethereum",
    "Price_btc": 0.01948437,
    "Price_usd": 8.59941135,
    "Price_cny": 55.94140258,
    "Price_eur": 7.58939922,
    "Price_gbp": 6.10172873,
    "Price_rur": 544.17387808,
    "Volume_24h": 28680.92498425,
    "Timestamp": 1461221820
}
#https://www.worldcoinindex.com/coin/<coin_name>

exampleslackcommand = {
    "token": "gIkuvaNzQIHg97ATvDxqgjtO",
    "team_id": "T0001",
    "team_domain": "example",
    "enterprise_id": "E0001",
    "enterprise_name": "Globular%20Construct%20Inc",
    "channel_id": "C2147483705",
    "channel_name": "test",
    "user_id": "U2147483697",
    "user_name": "Steve",
    "command" : "/weather",
    "text": 94070,
    "response_url": "https://hooks.slack.com/commands/1234/5678"
}

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('home.html')

@app.route('/slash-command/', methods=['GET', 'POST'])
def command():
    # token = request.form.get('token', None)
    # command = request.form.get('command', None)
    # text = request.form.get('text', None)
    # print(text)
    r = requests.get('https://www.worldcoinindex.com/apiservice/json?key=BRCC0KMJDnZHfrGuaPL51giKV', auth=('user', 'pass'))
    print(r.status_code)
    return r.text
    
    # return jsonify({
    #     'text' : 
    #     'url' : 
    #     'token' : 
    #     "response_url": "https://mighty-eyrie-28651.herokuapp.com/slash-command"
    # }) #, name=name, volume=volume)

@app.route('/coin/', methods=['GET', 'POST'])
def coin():
    name = request.form['Name']    
    volume = request.form.get["Volume_24h"]
    return jsonify({

    })

if __name__ == ('__main__'):
    #app.secret_key='secret123'
    app.run(debug=True)


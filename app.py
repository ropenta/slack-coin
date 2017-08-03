from flask import Flask, render_template, flash, redirect, url_for, session, request, jsonify
import json

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

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('home.html')

@app.route('/coin/', methods=['GET', 'POST'])
def coin():
    #name = request.form['Name']    
    #volume = request.form["Volume_24h"]
    return render_template('coin.html') #, name=name, volume=volume)


if __name__ == ('__main__'):
    #app.secret_key='secret123'
    app.run(debug=True)


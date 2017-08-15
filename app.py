from flask import Flask, render_template, redirect, url_for, session, request, jsonify, abort, g
import pyscreenshot as ImageGrab
import requests
import json
import os
import sqlite3



app = Flask(__name__)
build_notes = {
    0: 'learn flask and its API',
    1: 'build app.py, requirements.txt, runtime.txt, and Procfile',
    2: 'learn Heroku\'s HTTP server hosting, and get its url',
    3: 'connect server with Slack and get slash command \bitcoin to return link to webpage',
    4: 'work out details of retreiving currency data, possibly graphs, with app and bot.py',
    5: 'connect again with Slack and run \bitcoin to get useful info in the chatbox'
}

# Database functions from sqlite3
DATABASE = '/path/to/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET'])
def index():
    cur = get_db().cursor()
    return render_template('home.html')


@app.route('/slash-command/', methods=['GET', 'POST'])
def handler():
    '''
        POST handler
        1. GET the relevant JSON data from WCI
        2. Format the Slack POST
    '''
    # 1. GET the relevant JSON data from WCI
    wci_url = 'https://www.worldcoinindex.com/apiservice/json?key=BRCC0KMJDnZHfrGuaPL51giKV'
    print(request.form.keys)

    r = requests.get(wci_url, auth=('user', 'pass'))
    print(r.status_code)
    data = r.json()
    meta = data[u'Markets']

    # session = requests.session()
    # r = requests.post(wci_url, data=payload)
    # print(r.text)

    # 2. Format the Slack POST
    slack_url = request.form.get('response_url', None)
    text = request.form.get('text', None)

    print(data.keys)
    print(slack_url)
    print(text)  #this has nothing in it unless a slack command is invoked

    if (text == 'btc' or text == 'bitcoin'):
        coin_type = meta[46]

    elif (text == 'eth' or text == 'ethereum'):
        coin_type = meta[173]
    else: #command == 'litecoin'
        coin_type = meta[276]



    # part of the screen
    # im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2
    # im.show()
    # fullscreen
    # screenshot=ImageGrab.grab()
    # screenshot.show()

    # # part of the screen
    # screenshot=pyscreenshot.grab(bbox=(10,10,500,500))
    # screenshot.show()

    # # save to file
    #ImageGrab.grab_to_file('screenshot.png')
    return jsonify(coin_type)


    
    

if __name__ == ('__main__'):
    #app.secret_key='secret123'
    app.run(debug=True)



'''
    JSON Formats
'''
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
    "command" : "/coin",
    "text": 94070,
    "response_url": "https://hooks.slack.com/commands/1234/5678"
}

examplereturnformat = {
    "text" : "some filler text foo bar",
    "attachments" : [
        {
            "fallback" : "fallback text",
            "text" : "more filler text"
        }
    ]
}
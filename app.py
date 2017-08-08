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

@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/slash-command/', methods=['GET', 'POST'])
def handler():
    wci_url = 'https://www.worldcoinindex.com/apiservice/json?key=BRCC0KMJDnZHfrGuaPL51giKV'
    print(request.form.keys)

    r = requests.get(wci_url, auth=('user', 'pass'))
    print(r.status_code)
    #r = requests.get('https://api.github.com/repos/requests/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
    data = r.json()
    meta = data[u'Markets']

    payload = {
        "token": "gIkuvaNzQIHg97ATvDxqgjtO",
        "team_id": "T0001",
        "team_domain": "example",
        "enterprise_id": "E0001",
        "enterprise_name": "Globular%20Construct%20Inc",
        "channel_id": "C2147483705",
        "channel_name": "test",
        "user_id": "U2147483697",
        "user_name": "Steve",
        "command" : "/bitcoin",
        "text": 94070,
        "response_url": "https://hooks.slack.com/commands/1234/5678"
    }
    # session = requests.session()
    # r = requests.post(wci_url, data=payload)
    # print(r.text)

    slack_url = request.form.get('response_url', None)
    text = request.form.get('text', None)

    print(data.keys)
    print(slack_url)
    print(text)  #this has nothing in it unless a slack command is invoked

    if (text == '/bitcoin' or text == 'bitcoin'):
        coin_type = meta[46]

    elif (text == '/ethereum' or text == 'ethereum'):
        coin_type = meta[173]
    else: #command == 'litecoin'
        coin_type = meta[276]

    # b = meta[46]
    # e = meta[173]
    # l = meta[276]
    #print(m['Label'])
    # i_num = 0
    # for i in meta:
    #     print(i_num, '\n', i, '\n')
    #     i_num = i_num + 1



    # i = 0
    # for each in meta[i]['Label']:
    #     print(each)
    #     i = i + 1
    # payload = dict(key1='val1', key2='value2')
    # r = requests.post(wci_url, data=payload)
    # print(r.request.headers)

    return jsonify(coin_type)
    #return redirect("https://www.worldcoinindex.com/coin/bitcoin")
    # return jsonify({
    #     "text" : "some filler text foo bar",
	#     "attachments" : [
    #         {
    #             "fallback" : "fallback text",
    #             "text" : "more filler text"
    #         }
    #    ]
    # })

    
    

if __name__ == ('__main__'):
    #app.secret_key='secret123'
    app.run(debug=True)






    # token = request.form.get('token', None)
    # command = request.form.get('command', None)
    # text = request.form.get('text', None)
    # print(text)

    # return jsonify({
    #     'text' : 
    #     'url' : 
    #     'token' : 
    #     "response_url": "https://mighty-eyrie-28651.herokuapp.com/slash-command"
    # }) #, name=name, volume=volume)


# @app.route('/coin/', methods=['GET', 'POST'])
# def coin():
#     name = request.form['Name']    
#     volume = request.form.get["Volume_24h"]
#     return jsonify({

#     })
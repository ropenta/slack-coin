from flask import request, url_for, Flask, Request
from flask_api import FlaskAPI, status, exceptions
# for whatever reason, this doesn't use Flask or Request
app = FlaskAPI(__name__)


notes = {
    0: 'learn the flask and its API',
    1: 'build app.py, requirements.txt, runtime.txt, and Procfile',
    2: 'learn Heroku\'s HTTP server hosting, and get its url',
    3: 'connect server with Slack and get slash command \bitcoin to return link to webpage',
    4: 'work out details of retreiving currency data, possibly graphs, with app and bot.py',
    5: 'connect again with Slack and run \bitcoin to get useful info in the chatbox'

}

def note_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('notes_detail', key=key),
        'text': notes[key]
    }


@app.route("/", methods=['GET', 'POST'])
def notes_list():
    """
    List or create notes.
    """
    if request.method == 'POST':
        note = str(request.data.get('text', ''))
        idx = max(notes.keys()) + 1
        notes[idx] = note
        return note_repr(idx), status.HTTP_201_CREATED
    else:
        # request.method == 'GET'
        return [note_repr(idx) for idx in sorted(notes.keys())]


@app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
def notes_detail(key):
    """
    Retrieve, update or delete note instances.
    """
    if request.method == 'PUT':
        note = str(request.data.get('text', ''))
        notes[key] = note
        return note_repr(key)

    elif request.method == 'DELETE':
        notes.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    if key not in notes:
        raise exceptions.NotFound()
    return note_repr(key)


if __name__ == "__main__":
    app.run(debug=True)
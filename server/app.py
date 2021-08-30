import datetime
from flask import Flask, jsonify, request
from flask.json import jsonify
from flask_cors import CORS
from datetime import datetime

#configuration
DEBUG=True

BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins':"*"}})


# sanity check route
@app.route('/ping', methods=["GET"])
def ping_pong():
    return jsonify(f"{datetime.now().isoformat(timespec='seconds')}: pong!")


# bad practice, bad - to mess logic within single method
@app.route('/books', methods=["GET", "POST"])
def get_all_books():
    response = {'status':'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response['message'] = 'Book added!'
    else:
        response['books'] = BOOKS
    return jsonify(response)

if __name__ == '__main__':
        app.run()

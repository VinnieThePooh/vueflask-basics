import datetime
from flask import Flask
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

@app.route('/books', methods=["GET"])
def get_all_books():
        return jsonify({'status': 'success', 'books': BOOKS})

if __name__ == '__main__':
        app.run()

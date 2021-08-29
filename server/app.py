import datetime
from flask import Flask
from flask.json import jsonify
from flask_cors import CORS
from datetime import datetime

#configuration
DEBUG=True


app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins':"*"}})


# sanity check route
@app.route('/ping', methods=["GET"])
def ping_pong():
    return jsonify(f"{datetime.now().isoformat(timespec='seconds')}: pong!")

if __name__ == '__main__':
        app.run()

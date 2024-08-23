from flask import Flask,jsonify
from database_connection import db

app = Flask(__name__)

db.connect()

@app.route('/', methods=['GET'])
def responseToTheHomeRoute():
    return jsonify("Added home route.")

if __name__ == '__main__':
    app.run()
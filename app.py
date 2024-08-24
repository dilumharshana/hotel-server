from flask import Flask, request, jsonify
from database_connection import db
from customersController import createCustomer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db.connect()


@app.route('/', methods=['GET'])
def responseToTheHomeRoute():
    return jsonify("Added home route.")


@app.route('/customer', methods=['POST'])
def handleCreateCustomer():
    return createCustomer(request.json)


if __name__ == '__main__':
    app.run()

from flask import Flask, request, jsonify
from database_connection import db
from customersController import createCustomer
from offersController import createOffer, getAllOffers
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


@app.route('/offer', methods=['POST'])
def handleCreateOffer():
    return createOffer(request.json)


@app.route('/offers', methods=['GET'])
def getOffers():
    return getAllOffers()


if __name__ == '__main__':
    app.run()

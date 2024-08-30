from flask import Flask, request, jsonify
from database_connection import db
from customersController import createCustomer
from offersController import createOffer, getAllOffers, updateOffer, activateOffer, deleteOffer
from serviceController import createService, getAllService, updateService, activateService, deleteService
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


@app.route('/offer', methods=['PUT'])
def handleUpdateOffer():
    return updateOffer(request.json)


@app.route('/activate-offer', methods=['PUT'])
def handleActivateOffer():
    return activateOffer(request.json)


@app.route('/offer/<int:id>', methods=['DELETE'])
def handleDeleteOffer(id):
    return deleteOffer(id)


@app.route('/offers', methods=['GET'])
def getOffers():
    return getAllOffers()


@app.route('/service', methods=['POST'])
def handleCreateService():
    return createService(request.json)


@app.route('/service', methods=['PUT'])
def handleUpdateService():
    return updateService(request.json)


@app.route('/activate-service', methods=['PUT'])
def handleActivateService():
    return activateService(request.json)


@app.route('/service/<int:id>', methods=['DELETE'])
def handleDeleteService(id):
    return deleteService(id)


@app.route('/services', methods=['GET'])
def getService():
    return getAllService()


if __name__ == '__main__':
    app.run()

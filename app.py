from flask import Flask, request, jsonify
from database_connection import db
from customersController import createCustomer
from offersController import createOffer, getAllOffers, updateOffer, activateOffer, deleteOffer
from serviceController import createService, getAllService, updateService, activateService, deleteService
from reservationController import create_reservation
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


# reservation routes

@app.route('/reservation', methods=['POST'])
def createReservation():
    return create_reservation(request.json)


# @app.route('/reservation/<int:reservation_id>', methods=['PUT'])
# def update_reservation(reservation_id):
#     data = request.json
#     return ReservationHandler().update_reservation(reservation_id, data)


# @app.route('/reservation/<int:reservation_id>', methods=['DELETE'])
# def delete_reservation(reservation_id):
#     return ReservationHandler().delete_reservation(reservation_id)


# @app.route('/available_rooms', methods=['GET'])
# def get_available_rooms():
#     start_date = request.args.get('start_date')
#     end_date = request.args.get('end_date')
#     return ReservationHandler().get_available_rooms(start_date, end_date)


# @app.route('/available_banquet_halls', methods=['GET'])
# def get_available_banquet_halls():
#     date = request.args.get('date')
#     return ReservationHandler().get_available_banquet_halls(date)

if __name__ == '__main__':
    app.run()

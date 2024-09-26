from flask import Flask, request, jsonify
from database_connection import db
from customersController import createCustomer, getCustomer
from offersController import createOffer, getAllOffers, updateOffer, activateOffer, deleteOffer
from serviceController import createService, getAllService, updateService, activateService, deleteService
from reservationController import create_reservation, get_reservations
from inquiryController import createInquiry, getAllInquiries, sendInquiryReply
from dashboardController import getDashboard
from emailService import send_email, mail
from login import login
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'dilum.harshana123@gmail.com'
app.config['MAIL_PASSWORD'] = 'ajwm ysbv tuob curt'
app.config['MAIL_DEFAULT_SENDER'] = 'dilum.harshana123@gmail.com'

mail.init_app(app)

db.connect()


@app.route('/', methods=['GET'])
def responseToTheHomeRoute():
    return jsonify("Added home route.")


@app.route('/customer', methods=['POST'])
def handleCreateCustomer():
    return createCustomer(request.json)


@app.route('/customer', methods=['GET'])
def handleGetCustomers():
    return getCustomer()


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


@app.route('/reservation', methods=['GET'])
def getReservations():
    return get_reservations()


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


# login routes
@app.route('/login', methods=['POST'])
def handleLogin():
    return login(request.json)


@app.route('/inquiry', methods=['POST'])
def handleCreateInquiry():
    return createInquiry(request.json)


@app.route('/inquiry', methods=['GET'])
def handleGetInquiries():
    return getAllInquiries()


@app.route('/reply-inquiry', methods=['POST'])
def handleSendInquiryReply():
    return sendInquiryReply(request.json)


@app.route('/dashboard', methods=['GET'])
def getDashboardData():
    return getDashboard()


@app.route('/email', methods=['POST'])
def sendMail():
    return send_email()


if __name__ == '__main__':
    app.run()

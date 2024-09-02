from reservationsModel import ReservationHandler

reservation = ReservationHandler()


def create_reservation(data):
    return reservation.create_reservation(data)

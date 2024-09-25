
import random
from flask import Flask, request, jsonify
from datetime import datetime
from abc import ABC, abstractmethod
from database_connection import db
from emailService import send_email
# Strategy Pattern for Reservation Types


class ReservationStrategy(ABC):
    @abstractmethod
    def create_reservation(self, cursor, data):
        pass

    @abstractmethod
    def check_availability(self, cursor, data):
        pass


class RoomReservationStrategy(ReservationStrategy):
    def create_reservation(self, cursor, data):
        # First, get all available rooms
        available_rooms = self.get_available_rooms(
            cursor, data['check_in_date'], data['check_out_date'])

        if not available_rooms:
            return None, "No rooms available for the specified dates."

        # Randomly select a room
        selected_room = random.choice(available_rooms)[1]

        print(data)

        print("selected_room ==>", selected_room)

        # Create the reservation
        query = """
        INSERT INTO reservations 
        (customer_name, customer_email, reservation_type, room_id, check_in_date, check_out_date, num_adults)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (data['customer_name'], data['customer_email'], 'room',
                  selected_room, data['check_in_date'], data['check_out_date'],
                  data['num_adults'])

        cursor.execute(query, values)
        return selected_room

    def check_availability(self, cursor, data):
        available_rooms = self.get_available_rooms(
            cursor, data['check_in_date'], data['check_out_date'])
        print(available_rooms)
        return len(available_rooms) > 0

    def get_available_rooms(self, cursor, check_in_date, check_out_date):
        connection = db.get_db_connection()
        cursor2 = connection.cursor()

        print(check_in_date)
        print(check_out_date)
        query = """
        SELECT r.id, r.room_number FROM rooms r
        WHERE r.id NOT IN (
            SELECT DISTINCT room_id FROM reservations
            WHERE reservation_type = 'room'
            AND ((check_in_date <= %s AND check_out_date >= %s)
            OR (check_in_date <= %s AND check_out_date >= %s)
            OR (check_in_date >= %s AND check_out_date <= %s))
        )
        """
        cursor2.execute(query, (check_in_date, check_in_date,
                                check_out_date, check_out_date, check_in_date, check_out_date))
        return cursor2.fetchall()


class ReservationHandler:
    def __init__(self):
        self.strategies = {
            'room': RoomReservationStrategy(),
        }

    def create_reservation(self, data):
        reservation_type = data.get('reservation_type')
        strategy = self.strategies.get(reservation_type)
        if not strategy:
            return jsonify({'error': 'Invalid reservation type'}), 400

        connection = db.get_db_connection()
        cursor = connection.cursor()

        try:
            if not strategy.check_availability(cursor, data):
                return jsonify({'error': 'Sorry! No rooms are available for the specified dates !'}), 200

            selected_room = strategy.create_reservation(cursor, data)
            connection.commit()
            message = "You have successfully booked your room at ABC Hotel. Your room number is:" + selected_room
            send_email(data['customer_email'], 'Room reservation', message)
            return jsonify({'message': 'Reservation created successfully', 'room_number': selected_room}), 200
        except Exception as err:
            return jsonify({'error: {err}'}), 500

    def get_all_reservations(self):
        connection = db.get_db_connection()
        cursor = connection.cursor(dictionary=True)

        try:

            cursor.execute('SELECT * FROM RESERVATIONS')
            reservations = cursor.fetchall()

            return jsonify({'reservations': reservations}), 200
        except Exception as err:
            return jsonify({'error: {err}'}), 500

    def update_reservation(self, reservation_id, data):
        connection = db.get_db_connection()
        cursor = connection.cursor()

        try:
            query = """
            UPDATE reservations
            SET customer_name = %s, customer_email = %s, check_in_date = %s, 
                check_out_date = %s, num_adults = %s, num_guests = %s
            WHERE id = %s
            """
            values = (data.get('customer_name'), data.get('customer_email'),
                      data.get('check_in_date'), data.get('check_out_date'),
                      data.get('num_adults'), data.get('num_guests'),
                      reservation_id)
            cursor.execute(query, values)

            if cursor.rowcount == 0:
                return jsonify({'error': 'Reservation not found'}), 404

            connection.commit()
            return jsonify({'message': 'Reservation updated successfully'}), 200
        except Exception as err:
            return jsonify({'error': f'Database error: {err}'}), 500

    def delete_reservation(self, reservation_id):
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        try:
            query = "DELETE FROM reservations WHERE id = %s"
            cursor.execute(query, (reservation_id,))

            if cursor.rowcount == 0:
                return jsonify({'error': 'Reservation not found'}), 404

            connection.commit()
            return jsonify({'message': 'Reservation deleted successfully'}), 200
        except Exception as err:
            return jsonify({'error': f'Database error: {err}'}), 500

    def get_available_rooms(self, start_date, end_date):
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        try:
            query = """
            SELECT r.* FROM rooms r
            WHERE r.id NOT IN (
                SELECT DISTINCT room_id FROM reservations
                WHERE reservation_type = 'room'
                AND ((check_in_date <= %s AND check_out_date >= %s)
                OR (check_in_date <= %s AND check_out_date >= %s)
                OR (check_in_date >= %s AND check_out_date <= %s))
            )
            """
            cursor.execute(query, (start_date, start_date,
                           end_date, end_date, start_date, end_date))
            available_rooms = cursor.fetchall()
            return jsonify(available_rooms), 200
        except Exception as err:
            return jsonify({'error': f'Database error: {err}'}), 500

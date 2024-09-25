from flask import jsonify
from database_connection import db


class Dashboard:

    def getDashboardData(self):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor(dictionary=True)

            query = 'SELECT * FROM OFFERS WHERE IS_ACTIVE=1;'

            cursor.execute(query, ())
            offerCount = cursor.fetchall()

            query = 'SELECT * FROM SERVICES WHERE IS_ACTIVE=1;'
            cursor.execute(query, ())
            serviceCount = cursor.fetchall()

            query = 'SELECT * FROM INQUIRES WHERE REPLY IS NULL;'
            cursor.execute(query, ())
            inquiryCount = cursor.fetchall()

            query = 'SELECT * FROM RESERVATIONS;'
            cursor.execute(query, ())
            reservationCount = cursor.fetchall()

            query = 'SELECT * FROM USERS WHERE ROLE = 4;'
            cursor.execute(query, ())
            customerCount = cursor.fetchall()

            connection.close()

            return jsonify({'offerCount': offerCount,
                            'serviceCount': serviceCount,
                            'inquiryCount': inquiryCount,
                            'reservationCount': reservationCount,
                            'customerCount': customerCount}
                           ), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

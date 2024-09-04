from flask import jsonify
from database_connection import db


class Inquiry:

    def createInquiry(self, data):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor()

            query = "INSERT INTO `hotel`.`inquires` (`customer_id`, `inquiry`, `contact_number`) VALUES (%s, %s, %s)"
            cursor.execute(
                query, (data['customer_id'], data['message'], data['contactNumber']))

            connection.commit()
            inquiryId = cursor.lastrowid

            cursor.close()
            return jsonify({'inquiryId': inquiryId}), 200

        except Exception as e:
            print(e)

    def getAllInquiries(self, ):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM INQURIES')
            inquiries = cursor.fetchall()

            cursor.close()
            return jsonify({'inquiries': inquiries}), 200

        except Exception as e:
            print(e)

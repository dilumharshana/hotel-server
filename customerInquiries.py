from flask import jsonify
from database_connection import db
from emailService import send_email


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

            return jsonify({'inquiryId': inquiryId}), 200

        except Exception as e:
            print(e)

    def getAllInquiries(self):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                'SELECT i.*, u.* FROM INQUIRES i INNER JOIN USERS u ON i.customer_id = u.ID WHERE i.REPLY is NULL ORDER BY i.created_at DESC;')
            inquiries = cursor.fetchall()

            return jsonify({'inquiries': inquiries}), 200

        except Exception as e:
            print(e)
            return jsonify("error on fetching data"), 500

    def sendInquiryReply(self, data):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor()

            cursor.execute(
                "UPDATE `hotel`.`inquires` SET `reply` = %s WHERE id = %s", (
                    data['reply'], data['inquiryId']))

            connection.commit()

            send_email(data['customerEmail'],
                       "ABC Restaurant - Inquiry reply", data['reply'] + " ABC Restaurant Admin")

            return jsonify({'status': 'success'}), 200

        except Exception as e:
            print(e)
            return jsonify("error on fetching data"), 500

from flask import jsonify
from database_connection import db


class Customer:

    def createCustomer(self, customerData):
        connection = db.get_db_connection()
        try:
            cursor = connection.cursor()
            query = 'INSERT INTO `hotel`.`users` (`NAME`, `EMAIL`, `CONTACT_NUMBER`, `ROLE`, `PASSWORD`, `IS_ACTIVE`) VALUES (%s, %s, %s, %s, %s, %s);'
            cursor.execute(query, (customerData['name'],
                                   customerData['email'], customerData['contactNumber'], 4, customerData['password'], 1))
            connection.commit()
            customerId = cursor.lastrowid
            print("customerId =>", customerId)
            return jsonify({'customerData': customerData, 'customerId': customerId}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def getCustomers(self):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM USERS where ROLE = 4')
            customers = cursor.fetchall()
            return jsonify({'customers': customers}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

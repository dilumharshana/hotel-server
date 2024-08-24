from flask import jsonify
from database_connection import db


class Customer:

    def createCustomer(self, customerData):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor()
            query = 'INSERT INTO `hotel`.`users` (`NAME`, `EMAIL`, `CONTACT_NUMBER`, `ROLE`, `PASSWORD`, `IS_ACTIVE`) VALUES (%s, %s, %s, %s, %s, %s);'
            cursor.execute(query, (customerData['name'],
                                   customerData['email'], customerData['contactNumber'], 1, customerData['password'], 1))
            connection.commit()
            customerId = cursor.lastrowid
            print("customerId =>", customerId)
            cursor.close()
            return jsonify({'customerData': customerData, 'customerId': customerId}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

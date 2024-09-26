from flask import jsonify
from database_connection import db


class Service:

    def createService(self, serviceData):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor()

            query = 'INSERT INTO `hotel`.`services` (`NAME`, `DESCRIPTION`, `IS_ACTIVE`) VALUES (%s, %s, %s);'
            cursor.execute(query, (serviceData['name'],
                                   serviceData['description'], serviceData['isActive']))
            connection.commit()
            serviceId = cursor.lastrowid
            print("serviceId =>", serviceId)
            return jsonify({'serviceId': serviceId}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def updateService(self, serviceData):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor()
            query = 'UPDATE `hotel`.`services` SET `NAME` = %s, `DESCRIPTION` = %s, `IS_ACTIVE` = %s WHERE (`ID` = %s);'
            cursor.execute(query, (serviceData['name'],
                                   serviceData['description'], serviceData['isActive'], serviceData['id']))
            connection.commit()
            rowCount = cursor.rowcount
            print("serviceId =>", rowCount)
            return jsonify({'serviceId': rowCount}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def handleActivateService(self, serviceData):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor()
            query = 'UPDATE `hotel`.`services` SET `IS_ACTIVE` = %s WHERE (`ID` = %s);'
            cursor.execute(
                query, (serviceData['activation'], serviceData['id']))
            connection.commit()
            rowCount = cursor.rowcount
            print("serviceId =>", rowCount)
            return jsonify({'serviceId': rowCount}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def deleteService(self, serviceId):
        cursor = None
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor()
            query = 'DELETE FROM `hotel`.`services` WHERE (`ID` = %s);'
            cursor.execute(query, (serviceId,))
            connection.commit()
            rowCount = cursor.rowcount
            print("serviceId =>", rowCount)
            return jsonify({'serviceId': rowCount}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def getAllServices(self):
        cursor = None
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM SERVICES')
            services = cursor.fetchall()
            return jsonify({'services': services}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

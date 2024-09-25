from flask import jsonify
from database_connection import db


class Offer:

    def createOffer(self, offerData):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor()
            query = 'INSERT INTO `hotel`.`offers` (`NAME`, `DESCRIPTION`, `IS_ACTIVE`, `THUMBNAIL`, `ENDING_DATE`) VALUES (%s, %s, %s, %s, %s);'
            cursor.execute(query, (offerData['name'],
                                   offerData['description'], offerData['isActive'], offerData['thumbnailUrl'], offerData['endingDate']))
            connection.commit()
            offerId = cursor.lastrowid
            print("offerId =>", offerId)
            return jsonify({'offerId': offerId}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            connection.close()

    def updateOffer(self, offerData):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor()
            query = 'UPDATE `hotel`.`offers` SET `NAME` = %s, `DESCRIPTION` = %s, `IS_ACTIVE` = %s, `THUMBNAIL` = %s, `ENDING_DATE` = %s WHERE (`ID` = %s);'
            cursor.execute(query, (offerData['name'],
                                   offerData['description'], offerData['isActive'], offerData['thumbnailUrl'], offerData['endingDate'], offerData['id']))
            connection.commit()
            rowCount = cursor.rowcount
            print("offerId =>", rowCount)
            return jsonify({'offerId': rowCount}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            connection.close()

    def handleActivateOffer(self, offerData):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor()
            query = 'UPDATE `hotel`.`offers` SET `IS_ACTIVE` = %s WHERE (`ID` = %s);'
            cursor.execute(query, (offerData['activation'], offerData['id']))
            connection.commit()
            rowCount = cursor.rowcount
            print("offerId =>", rowCount)
            return jsonify({'offerId': rowCount}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            connection.close()

    def deleteOffer(self, offerId):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor()
            query = 'DELETE FROM `hotel`.`offers` WHERE (`ID` = %s);'
            cursor.execute(query, (offerId,))
            connection.commit()
            rowCount = cursor.rowcount
            print("offerId =>", rowCount)
            return jsonify({'offerId': rowCount}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            connection.close()

    def getAllOffers(self):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM OFFERS')
            offers = cursor.fetchall()
            connection.close()
            return jsonify({'offers': offers}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

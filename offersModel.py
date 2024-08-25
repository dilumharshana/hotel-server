from flask import jsonify
from database_connection import db


class Offer:

    def createOffer(self, offerData):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor()
            query = 'INSERT INTO `hotel`.`offers` (`NAME`, `DESCRIPTION`, `IS_ACTIVE`, `THUBNAIL`, `ENDING_DATE`) VALUES (%s, %s, %s, %s, %s);'
            cursor.execute(query, (offerData['name'],
                                   offerData['description'], offerData['isActive'], offerData['thumbnailUrl'], offerData['endingDate']))
            connection.commit()
            offerId = cursor.lastrowid
            print("offerId =>", offerId)
            return jsonify({'offerData': offerData, 'offerId': offerId}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()

    def getAllOffers(self):
        try:
            connection = db.get_db_connection()
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM OFFERS')
            offers = cursor.fetchall()
            cursor.close()
            return jsonify({'offers': offers}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()

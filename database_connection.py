
import mysql.connector
from mysql.connector import Error


class DatabaseConnector:
    _instance = None
    _connection = None

    # _new_ method in python is responsible for handling instance creation of a class and this invokes before the
    # class constructor does and we can control the object creation of a particular class with this method

    # cls is class itself which is DatabaseConnector
    def _new_(cls):
        # with this code snippet it ensures that only one instance of the class is created
        if cls._instance is None:
            cls._instance = super(DatabaseConnector, cls)._new_(cls)
        return cls._instance

    def connect(self):
        if self._connection is None:
            try:
                self._connection = mysql.connector.connect(
                    host='localhost',
                    database='hotel',
                    user='root',
                    password='papapapa'
                )

                if self._connection.is_connected():
                    self._connection.cursor()
                    print("Connected to the database")
            except Error as e:
                print("Error : ", e)

    def get_db_connection(self):
        if self._connection is None:
            self.connect()
        return self._connection

    def close_db_connection(self):
        if self._connection and self._connection.is_connected():
            self._connection.close()
            print("Database disconnected !")


db = DatabaseConnector()

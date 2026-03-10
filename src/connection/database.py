import os

import mysql.connector


class __DatabaseConnection__:
    def __init__(self, host, port, user, password, database):
        self.__host__ = host
        self.__port__ = port
        self.__user__ = user
        self.__password__ = password
        self.__database__ = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.__host__,
                port=self.__port__,
                user=self.__user__,
                password=self.__password__,
                database=self.__database__
            )
            print("Connection to the database has been established!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection = None

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Connection to the database has been disconnected!")

    def execute_query(self, query, params=None):
        if not self.connection:
            raise Exception("No database connection established.")

        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
            self.connection.rollback()
            raise
        finally:
            cursor.close()

    def fetch_all(self, query, params=None, fetch_mode="tuple"):
        if not self.connection:
            raise Exception("No database connection established.")

        if fetch_mode == "dict":
            cursor = self.connection.cursor(dictionary=True)
        else:
            cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error fetching data: {err}")
            raise
        finally:
            cursor.close()

    def fetch_one(self, query, params=None, fetch_mode="tuple"):
        if not self.connection:
            raise Exception("No database connection established.")

        if fetch_mode == "dict":
            cursor = self.connection.cursor(dictionary=True)
        else:
            cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            return cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"Error fetching data: {err}")
            raise
        finally:
            cursor.close()


DatabaseConnection = __DatabaseConnection__(
    host=os.getenv("DATABASE_HOST"),
    port=os.getenv("DATABASE_PORT"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    database=os.getenv("DATABASE_NAME")
)

DatabaseConnection.connect()

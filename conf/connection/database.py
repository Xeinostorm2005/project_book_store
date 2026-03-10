import mysql.connector


class DatabaseConnection:
    def __init__(self, host, port, user, password):
        self.__host__ = host
        self.__port__ = port
        self.__user__ = user
        self.__password__ = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.__host__,
                port=self.__port__,
                user=self.__user__,
                password=self.__password__
            )
            print("Connection to the database has been established!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection = None

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Connection to the database has been disconnected!")

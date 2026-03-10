from src.connection.database import DatabaseConnection
from src.models.cart import cart
from random import randint


class Checkout:
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart
        self.db = DatabaseConnection

    def __order_details__(self, order_id, isbn, quantity, total_price):
        query = """
            INSERT INTO odetails (ono, isbn, qty, amount)
            VALUES (%s, %s, %s, %s)
        """
        self.db.execute_query(query, (order_id, isbn, quantity, total_price))

    def __create_order__(self, order_id, user_id, address, city, zip):
        query = """
            INSERT INTO orders (ono, userid, shipAddress, shipCity, shipZip)
            VALUES (%s, %s, %s, %s, %s)
        """
        self.db.execute_query(query, (order_id, user_id, address, city, zip))

    def __generate_order_id__(self):
        return randint(10000000, 99999999)

    def process_checkout(self):
        order_id = self.__generate_order_id__()

        self.__create_order__(
            order_id,
            self.user['userid'],
            self.user['address'],
            self.user['city'],
            self.user['zip']
        )

        for item in self.cart:
            total_price = item['price'] * item['qty']
            self.__order_details__(
                order_id,
                item['isbn'],
                item['qty'],
                total_price
            )

        cart.clear_cart(self.user['userid'])
        return order_id

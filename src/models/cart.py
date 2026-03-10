from src.connection.database import DatabaseConnection


class Cart:
    def __init__(self):
        self.db = DatabaseConnection

    def add_to_cart(self, user_id, isbn, quantity=1):
        query = "INSERT INTO cart (userid, isbn, qty) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE qty = qty + %s"
        self.db.execute_query(query, (user_id, isbn, quantity, quantity))

    def view_cart(self, user_id):
        query = """
            SELECT cart.isbn, books.title, books.price, cart.qty FROM cart
            JOIN books ON cart.isbn = books.isbn
            WHERE cart.userid = %s
        """
        return self.db.fetch_all(query, (user_id,), fetch_mode="dict")

    def clear_cart(self, user_id):
        query = "DELETE FROM cart WHERE userid = %s"
        self.db.execute_query(query, (user_id,))


cart = Cart()

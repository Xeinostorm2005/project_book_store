from src.connection.database import DatabaseConnection


class __Book__:
    def __init__(self):
        self.db = DatabaseConnection

    def fetch_book(self, isbn):
        query = "SELECT * FROM books WHERE isbn = %s"
        result = self.db.fetch_one(query, (isbn,), fetch_mode="dict")
        return result if result else None

    def fetch_books(self, subject, start, limit):
        query = "SELECT * FROM books WHERE subject = %s ORDER BY title ASC LIMIT %s OFFSET %s"
        result = self.db.fetch_all(query, (subject, limit, start), fetch_mode="dict")
        return result if result else None


Book = __Book__()

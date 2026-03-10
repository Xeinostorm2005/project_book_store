from src.connection.database import DatabaseConnection
import bcrypt


class User:
    def __init__(
        self,
        email=None,
        password=None,
        fname=None,
        lname=None,
        address=None,
        city=None,
        post_code=None,
        phone_number=None
    ):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.city = city
        self.post_code = post_code
        self.phone_number = phone_number
        self.email = email
        self.password = password
        self.db = DatabaseConnection

    def email_exists(self):
        query = "SELECT email FROM members WHERE email = %s"
        result = self.db.fetch_all(query, (self.email,))
        return bool(result)

    def add_user(self):
        query = """
        INSERT INTO members (fname, lname, address, city, zip, phone, email, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            self.fname, self.lname,
            self.address, self.city,
            self.post_code, self.phone_number,
            self.email, self.hash_password(self.password)
        )
        self.db.execute_query(query, values)

    def get_user_by_email(self, data_format="tuple"):
        query = "SELECT * FROM members WHERE email = %s"
        result = self.db.fetch_one(query, (self.email,), fetch_mode=data_format)
        return result if result else None

    def hash_password(self, password):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed.decode('utf-8')

    def password_matches(self):
        query = "SELECT password FROM members WHERE email = %s"
        result = self.db.fetch_all(query, (self.email,))

        if result:
            stored_password = result[0][0]
            return bcrypt.checkpw(
                self.password.encode('utf-8'),
                stored_password.encode('utf-8')
            )

        return False

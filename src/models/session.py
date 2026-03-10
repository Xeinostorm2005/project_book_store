
class Session:
    def __init__(self):
        self.loggedIn = False
        self.createdAccount = False
        self.user = None
        self.cart = []

    def login(self, user):
        self.loggedIn = True
        self.user = user

    def logout(self):
        self.loggedIn = False
        self.user = None
        self.cart = []


session = Session()

from getpass import getpass
from src.utils.logo import logo
from src.utils.color import color
from src.models.user import User
from src.models.session import session


def user_login():
    user_data = dict()
    phase = {
        "email": False,
        "password": False
    }
    logo()
    print(color("Login to your account", "250;200;0"))
    print("Please enter your email and password to login to your account.")

    while True:

        # Loops until all phases are complete
        while not all(phase.values()):

            # Asks for the user's email
            if not phase["email"]:
                email = input("Enter your email: ")
                if not email or "@" not in email or "." not in email:
                    print("You must enter a valid email!")
                    continue
                phase["email"] = True
                user_data["email"] = email

            # Asks for the user's password
            if not phase["password"]:
                password = getpass("Enter your password: ")
                if not password:
                    print("You must enter your password!")
                    continue
                phase["password"] = True
                user_data["password"] = password

        user = User(**user_data)

        if not user.email_exists():
            print("No account with this email exists! Please try again.")
            phase["email"] = False
            phase["password"] = False
            continue

        if not user.password_matches():
            print("Incorrect password! Please try again.")
            phase["password"] = False
            continue

        session.loggedIn = True
        session.user = user.get_user_by_email(data_format="dict")
        print(f"Successfully logged in as {session.user['fname']} {session.user['lname']}")
        break

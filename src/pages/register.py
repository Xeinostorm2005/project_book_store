from src.utils.color import color
from src.models.user import User
from src.utils.logo import logo


def user_register():
    user_data = dict()
    phase = {
        "fname": False,
        "lname": False,
        "address": False,
        "city": False,
        "post_code": False,
        "phone_number": False,
        "email": False,
        "password": False
    }
    logo()
    print(color("Create an account", "250;200;0"))
    print("Please enter the following data to create an account.")

    while True:

        # Loops until all phases are complete
        while not all(phase.values()):

            # Asks for the user's first name
            if not phase["fname"]:
                fname = input("Enter your first name: ")
                if not fname.isalpha():
                    print("Your first name must only have alphabets")
                    continue
                phase["fname"] = True
                user_data["fname"] = fname

            # Asks for the user's last name
            if not phase["lname"]:
                lname = input("Enter your last name: ")
                if not lname.isalpha():
                    print("Your last name must only have alphabets")
                    continue
                phase["lname"] = True
                user_data["lname"] = lname

            # Asks for the user's address
            if not phase["address"]:
                address = input("Enter your address: ")
                if not address:
                    print("You must enter ur address!")
                    continue
                phase["address"] = True
                user_data["address"] = address

            # Asks for the user's city
            if not phase["city"]:
                city = input("Enter your city:")
                if not city.isalpha():
                    print("City name must only have alphabets")
                    continue
                phase["city"] = True
                user_data["city"] = city

            # Asks for the user's post code
            if not phase["post_code"]:
                post_code = input("Enter your post code: ")
                if not post_code.isdigit():
                    print("Post code must only have numbers")
                    continue
                phase["post_code"] = True
                user_data["post_code"] = post_code

            # Asks for the user's phone number
            if not phase["phone_number"]:
                phone_number = input("Enter your phone number: ")
                if not phone_number.isdigit():
                    print("Phone number must only have numbers")
                    continue
                phase["phone_number"] = True
                user_data["phone_number"] = phone_number

            # Asks for the user's email
            if not phase["email"]:
                email = input("Enter your email: ")
                if "@" not in email or "." not in email:
                    print("Invalid email format")
                    continue
                phase["email"] = True
                user_data["email"] = email

            # Asks for the user's password
            if not phase["password"]:
                password = input("Enter your password: ")
                if len(password) < 6:
                    print("Password must be at least 6 characters long")
                    continue
                phase["password"] = True
                user_data["password"] = password

        user = User(**user_data)

        if user.email_exists():
            print("An account with this email already exists. Please try again.")
            phase["email"] = False
            user_data["email"] = ""
            continue

        try:
            user.add_user()
            print(color("Account created successfully!", "0;255;0"))
            break
        except Exception as e:
            print(color("An error occurred while creating your account.", "255;0;0"))
            print("please try again later. if the problem persists, contact support.")
            print(f"Error details: {e}")
            break

from src.utils.logo import logo
from src.utils.color import color
from src.pages.register import user_register
from src.pages.login import user_login
from src.models.session import session
from src.pages.loggedIn import main as loggedIn_main


def application():

    while True:
        if session.loggedIn:
            loggedIn_main()
        logo()
        print("Choose an option from the following:")
        register_opt = "2. Create a new account\n"
        if session.createdAccount:
            register_opt = "\033[9m2. Create a new account\033[29m (Already created an account)\n"
        options = (
            "1. Login to an account\n"
            f"{register_opt}"
            "3. Exit"
        )
        print(color(options, "44;44;44"), end="\n\n")

        while True:
            choice = input(color("~> ", "255;140;0"))

            match int(choice):
                case 1:
                    print("You have chosen to login to an account.")
                    user_login()
                    input("Press Enter to continue...")
                    break
                case 2:
                    if session.createdAccount:
                        print("You have already created an account. Please choose another option.")
                        input("Press Enter to continue...")
                        continue
                    print("You have chosen to create an account.")
                    user_register()
                    session.createdAccount = True
                    input("Press Enter to continue...")
                    break
                case 3:
                    print("Thank you for visiting our book store. Good Bye!")
                    exit()
                case _:
                    print(
                        "Invalid option has been chosen! Please try again...",
                        end="\n\n"
                    )

        if session.createdAccount or session.loggedIn:
            continue

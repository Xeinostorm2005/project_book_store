from src.utils.color import color
from src.utils.logo import logo
from src.models.session import session
from src.pages.browse import main as browse_main


def main():
    while True:
        if not session.loggedIn:
            break
        logo()
        print(f"You are logged in as {session.user['fname']} {session.user['lname']}", end="\n\n")
        print(color("Book Store", "250;200;0"))
        print("Please choose an option from the following:")
        options = (
            "1. Browse for books\n"
            "2. View cart\n"
            "3. Logout"
        )
        print(color(options, "44;44;44"), end="\n\n")

        while True:
            choice = input(color("~> ", "255;140;0"))

            match int(choice):
                case 1:
                    print("You have chosen to browse for books.")
                    browse_main()
                    break
                case 2:
                    print("You have chosen to view your cart.")
                    input("Press Enter to continue...")
                    break
                case 3:
                    print("You have chosen to logout.")
                    session.loggedIn = False
                    session.user = None
                    input("Press Enter to continue...")
                    break
                case _:
                    print(
                        "Invalid option has been chosen! Please try again...",
                        end="\n\n"
                    )

from conf.main import main as setup_database
from src.main import application
from src.utils.clear_console import clear_console


def main():
    clear_console()
    print("Welcome to the book store!")
    print("Select an option:")
    print("1. Setup the database")
    print("2. Run the application")
    print("3. Exit", end="\n\n")
    print("Enter your choice (1, 2, or 3):")

    while True:
        try:

            choice = input("~> ")

            match choice:
                case '1':
                    print("Running the database configurator...")
                    setup_database()
                    break
                case '2':
                    print("Running the application...")
                    application()
                    break
                case '3':
                    print("Exiting the program. Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter 1, 2, or 3.")


# Runs the application
try:
    main()
except KeyboardInterrupt:
    print("Thank you for visiting our book store. Good Bye!")
    exit()

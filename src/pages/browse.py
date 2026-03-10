from src.utils.logo import logo
from src.utils.color import color
from src.pages.books import main as books_main

subjects = {
    1: "Action & Adventure",
    2: "Arts, Film & Photography",
    3: "Biographies, Diaries & True Account",
    4: "Comics & Mangas",
    5: "Computing, Internet & Digital Media",
    6: "Crime, Thriller & Mystery",
    7: "Humour",
    8: "Language, Lingustics & Writing",
    9: "Romance",
    10: "Sport"
}


def main():
    while True:
        logo()
        print(color("Browse the Book Store", "250;200;0"))
        print("Please choose one of the following subjects to browse through:")
        options = (
            "1. Action & Adventure\n"
            "2. Arts, Film & Photography\n"
            "3. Biographies, Diaries & True Account\n"
            "4. Comics & Mangas\n"
            "5. Computing, Internet & Digital Media\n"
            "6. Crime, Thriller & Mystery\n"
            "7. Humour\n"
            "8. Language, Lingustics & Writing\n"
            "9. Romance\n"
            "10. Sport\n"
            "11. Return to main menu"
        )
        print(color(options, "44;44;44"), end="\n\n")

        while True:
            try:
                choice = input(color("~> ", "255;140;0"))

                if not choice.isdigit() or int(choice) < 1 or int(choice) > 11:
                    raise ValueError

                if int(choice) == 11:
                    return

                subject = subjects[int(choice)]

                books_main(subject)
                break
            except ValueError:
                print(
                    "Invalid option has been chosen! Please try again...",
                    end="\n\n"
                )

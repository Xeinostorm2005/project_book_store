from src.utils.logo import logo
from src.utils.color import color
from src.models.book import Book


def main(subject):
    start = 0

    while True:
        books = Book.fetch_books(subject, start, 2)
        logo()
        print(color(f" 🚀 EXPLORING: {subject.upper()} ".center(60, "—"), "250;200;0"))
        print()

        for book in books:
            print(f"  {color('ID:', '100;100;100')} {book['isbn']}")
            print(f"  {color('TITLE:', '255;255;255'):<18} {book['title']}")
            print(f"  {color('AUTHOR:', '255;255;255'):<18} {book['author']}")
            print(f"  {color('PRICE:', '0;255;100'):<18} ${book['price']:,.2f}")
            print(f"  {color('—' * 45, '60;60;60')}")

        print("\n" + color("—" * 60, "100;100;100"))
        print(f" {color('[NEXT]', '0;255;255')} Next Page  | {color('[BACK]', '0;255;255')} Previous  | {color('[EXIT]', '255;50;50')} Main Menu")
        print(color("—" * 60, "100;100;100"))

        print("\n🛒 Enter an " + color("ISBN", "255;140;0") + " to add to cart, or use a command:")

        while True:
            choice = input(color("~> ", "255;140;0")).strip().upper()

            if choice.upper() == "NEXT":
                start += 2
                break
            elif choice.upper() == "BACK":
                if start > 2:
                    start -= 2
                    break
                else:
                    print("You are already on the first page!")
            elif choice.upper() == "EXIT":
                return
            else:
                print(
                    "Invalid option has been chosen! Please try again...",
                    end="\n\n"
                )

from src.utils.logo import logo
from src.utils.color import color
from src.models.session import session
from src.models.cart import cart


def main():
    cart_items = cart.view_cart(session.user['userid'])
    logo()
    print(color(f" 🛒 DIN KASSA (YOUR CART) ".center(80, "—"), "250;200;0"))
    print(f"Logged in as: {session.user['fname']} {session.user['lname']}\n")

    header = f"{'ISBN':<15} | {'Title':<30} | {'Price':<12} | {'Qty':<8} | {'Total':<15}"

    print(color("—" * 85, "60;60;60"))
    print(color(header, "150;150;150"))
    print(color("—" * 85, "60;60;60"))

    total_price = 0
    if not cart_items:
        print(f"{'Your cart is currently empty.':^85}")
    else:
        for item in cart_items:
            line_total = item['price'] * item['qty']
            total_price += line_total

            # Formatting the row
            print(f"{item['isbn']:<15} | "
                  f"{item['title'][:27] + '...' if len(item['title']) > 27 else item['title']:<30} | "
                  f"${item['price']:^12.2f} | "
                  f"{item['qty']:^8} | "
                  f"{color(f'${line_total:^15.2f}', '0;255;100')}")

    print(color("—" * 85, "60;60;60"))

    print(color(f"Total: ${total_price:,.2f}", "250;200;0"), end="\n\n")

    print("What would you like to do?")
    options = (
        "1. Proceed to checkout\n"
        "2. Return to main menu"
    )
    print(color(options, "44;44;44"), end="\n\n")

    while True:
        choice = input(color("~> ", "255;140;0"))

        match int(choice):
            case 1:
                print("You have chosen to proceed to checkout.")
                input("Press Enter to continue...")
                break
            case 2:
                print("You have chosen to return to the main menu.")
                return
            case _:
                print(
                    "Invalid option has been chosen! Please try again...",
                    end="\n\n"
                )
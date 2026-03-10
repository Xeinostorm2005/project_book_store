from src.utils.logo import logo
from src.utils.color import color
from src.models.session import session


def main(order, cart_items):
    order_id = order.process_checkout()
    logo()
    print(color(" RECEIPT ".center(80, "—"), "250;200;0"))
    print(f"Logged in as: {session.user['fname']} {session.user['lname']}\n")
    print(f"Order ID: {order_id}")
    print(f"Address: {session.user['address']}, {session.user['city']} {session.user['zip']}\n")

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

            print(f"{item['isbn']:<15} | "
                  f"{item['title'][:27] + '...' if len(item['title']) > 27 else item['title']:<30} | "
                  f"${item['price']:^12.2f} | "
                  f"{item['qty']:^8} | "
                  f"{color(f'${line_total:^15.2f}', '0;255;100')}")

    print(color("—" * 85, "60;60;60"))

    print(color(f"Total: ${total_price:,.2f}", "250;200;0"), end="\n\n")

    input(color("Press Enter to return to the main menu...", "255;140;0"))
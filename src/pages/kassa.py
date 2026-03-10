from src.utils.logo import logo
from src.utils.color import color
from src.models.session import session
from src.models.cart import cart


def main():
    cart_items = cart.view_cart(session.user['userid'])
    logo()
    print(color("Kassa", "250;200;0"))
    print("Your kassa:", end="\n\n")

    print("-"*100, end="\n\n")
    print(f"{'ISBN':<15} {'Title':<40} {'Price':<30} {'Quantity':<10} {'Total':<10}", end="\n\n")
    print("-"*100, end="\n\n")
    total_price = 0
    for items in cart_items:
        total = items['price'] * items['qty']
        print(f"{items['isbn']:<15} {items['title']:<40} {items['price']:<30} {items['quantity']:<10} {total:<10}", end="\n\n")
        print("-"*100, end="\n\n")
        total_price += total
    print(color(f"Total: ${total_price:,.2f}", "250;200;0"), end="\n\n")


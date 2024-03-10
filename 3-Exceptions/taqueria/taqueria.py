menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def display_menu(menu):
    print("menu:")
    for item, price in menu.items():
        print(f"{item}, ${price:.2f}")


order_total = 0
display_menu(menu)

while True:
    try:
        item = input("what would you like").title()
        if item in menu:
            order_total += menu[item]
        else:
            print("not in menu")
            continue
        print(f"total cost is ${order_total:.2f}")
    except EOFError:
        break
    except KeyboardInterrupt:
        print("\nOrder interrupted. Exiting...")
        break


print(f"final cost is ${order_total:.2f}")

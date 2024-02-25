def main():
    amount_paid = 0
    coke_price = 50

    while amount_paid < coke_price:
        coin = int(input("insert coin"))
        if coin in [25, 10, 5]:
            amount_paid += coin
            remaining_left = coke_price - amount_paid
            print("amount due {} cents".format(remaining_left))
        else:
            print("only 25, 10 or 5 cent")

    change = amount_paid - coke_price
    print("your change is {}".format(change))

    if amount_paid == coke_price:
        print("here is your coke")


if __name__ == "__main__":
    main()

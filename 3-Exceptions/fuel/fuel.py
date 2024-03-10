def get_fuel_percent():
    while True:
        try:
            fraction = input("can i have a fraction ")
            x, y = map(int, fraction.split("/"))

            if y == 0:
                print("denomenator cant be 0")
                continue

            percentage = (x / y) * 100

            if percentage <= 1:
                print("e")
            elif percentage >= 99:
                print("f")
            else:
                print(round(percentage), "% full")

            break
        except ValueError:
            print("invalid input please give values as fraction.")
        except ZeroDivisionError:
            print("y cannot be divided by zero")


get_fuel_percent()

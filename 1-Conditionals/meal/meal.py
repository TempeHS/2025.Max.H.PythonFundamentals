def convert(time: str):
    hours, minutes = time.split(":")
    x = float(minutes) / 60
    y = float(hours) + x
    return y


def main():
    time = input("whats the time: ")
    print(convert(time))


if "7.0" <= y <= "8.0":
    print("it is Breakfast")
elif "12.0" <= y <= "13.0" or "1.00":
    print("its lunch")
elif ""


if __name__ == "__main__":
    main()

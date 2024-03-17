def bid_adieu(names):
    if len(names) == 1:
        print("Adieu, adieu, to", names[0])
    elif len(names) == 2:
        print("Adieu, adieu, to", names[0], "and", names[1])
    else:
        farewell = "Adieu, adieu, to " + ", ".join(names[:-1]) + ", and " + names[-1]
        print(farewell)


def main():
    print("give names (press ctrl d to stop):")
    names = []
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    bid_adieu(names)


if __name__ == "__main__":
    main()

import emoji


def main():
    input_text = input("give me coded emoji ")
    emojized_text = emoji.emojize(input_text)
    print("emoji now:", emojized_text)


if __name__ == "__main__":
    main()

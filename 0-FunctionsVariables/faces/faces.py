def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str


def main():
    user_text = input("hi ")
    modified_text = convert(user_text)
    print(modified_text)


if __name__ == "__main__":

    main()

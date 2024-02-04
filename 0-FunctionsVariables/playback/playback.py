def replace_space_with_period(str):
    return str.replace(" ", "...")


def main():
    original_text = input("Enter the text: ")
    modified_text = replace_space_with_period(original_text)
    print("Modified text:", modified_text)


if __name__ == "__main__":

    main()

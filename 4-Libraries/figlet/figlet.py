import sys
from pyfiglet import Figlet


def print_usage():
    print("Usage: python figlet.py [-f FONT_NAME]")
    sys.exit(1)


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-f":
        print_usage()
    elif len(sys.argv) == 3 and sys.argv[1] == "-f":
        font_name = sys.argv[2]
    elif len(sys.argv) != 1:
        print_usage()

    figlet = Figlet(font=font_name) if len(sys.argv) == 3 else Figlet()

    text = input("give text: ")

    print(figlet.renderText(text))


if __name__ == "__main__":
    main()

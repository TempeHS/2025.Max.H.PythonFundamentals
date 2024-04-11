import sys


if len(sys.argv) < 2:
    print("too few arguments")
    sys.exit

elif len(sys.argv) > 2:
    print("too many arguments")
    sys.exit

elif not sys.argv[1].endswith(".py"):
    print("invalid input")
    sys.exit

else:
    try:
        lines = 0
        with open(sys.argv[1]) as file:
            for line in file:
                line.strip
                if not line or line.startswith("#"):
                    continue
                lines += 1
            print(lines)
    except FileNotFoundError:
        print("no file found")

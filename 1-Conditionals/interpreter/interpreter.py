def calculator(expression):
    x, y, z = expression.split()
    x = float(x)
    z = float(z)
    if y == ("+"):
        return = x + z
    elif y == ("-"):
        return = x - z
    elif y == ("*"):
        return = x * z
    elif y == ("/"):
        return = x / z

def main():
    expression = input("enter a math question: ")
    result = calculator(expression)
    print ("result", format(result, ".1f"))



if __name__ == "__main__":
    main()


main()

def calculate_expression(expression):
    x, operator, y = expression.split()
    x = float(x)
    y = float(y)
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        return x / y


def main():
    user_input = input("Enter an arithmetic expression (e.g., 1 + 1): ")
    result = calculate_expression(user_input)
    print("Result:", format(result, ".1f"))


if __name__ == "__main__":
    main()

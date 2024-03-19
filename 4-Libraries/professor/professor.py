import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        tries = 0

        while tries < 3:
            answer = input(f"what is {x} + {y}? ")
            try:
                answer = int(answer)
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"the correct answer is {correct_answer}")

    print(f"your score is {score}/10")


def get_level():
    while True:
        level = input("choose a level (1, 2, or 3): ")
        if level in ["1", "2", "3"]:
            return int(level)
        else:
            print("invalid input choose 1, 2, or 3.")


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("invalid level")


if __name__ == "__main__":
    main()

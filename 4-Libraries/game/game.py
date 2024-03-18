import random


def get_level():
    while True:
        try:
            level = int(input("Enter level: "))
            if level <= 0:
                raise ValueError
            return level
        except ValueError:
            print("enter a positive integer")


def get_guess():
    while True:
        try:
            guess = int(input("your guess: "))
            if guess <= 0:
                raise ValueError
            return guess
        except ValueError:
            print("enter a positive integer")


def game():
    level = get_level()
    target = random.randint(1, level)

    while True:
        guess = get_guess()

        if guess > target:
            print("Too big")
        elif guess < target:
            print("Too small")
        else:
            print("Just right")
            break


if __name__ == "__main__":
    game()

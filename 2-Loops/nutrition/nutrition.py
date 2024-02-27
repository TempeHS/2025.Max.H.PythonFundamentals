def get_fruit_calories(fruit):
    fruit_calories = {
        "apple": 95,
        "banana": 105,
        "grape": 62,
        "orange": 62,
        "avocado": 49,
        "sweet cherries": 100,
    }

    fruit_lower = fruit.lower()
    if fruit_lower in fruit_calories:
        return fruit_calories[fruit_lower]
    else:
        return None


def main():
    fruit = input("Enter a fruit: ")
    calories = get_fruit_calories(fruit)
    if calories is not None:
        print(f"One portion of {fruit.capitalize()} contains {calories} calories.")
    else:
        print("Sorry, we don't have information about the calories for that fruit.")


if __name__ == "__main__":
    main()

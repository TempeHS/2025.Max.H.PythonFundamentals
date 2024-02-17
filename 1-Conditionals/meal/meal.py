def main():
    time = input("whats the time: ")
    meal = check_meal_time(time)
    if meal:
        print("It's", meal, "time.")
    else:
        print("dont eat")


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60


def check_meal_time(time):
    hours = convert(time)
    if 7 <= hours < 8:
        return "breakfast"
    elif 12 <= hours < 13:
        return "lunch"
    elif 18 <= hours < 19:
        return "dinner"
    else:
        return None


if __name__ == "__main__":
    main()

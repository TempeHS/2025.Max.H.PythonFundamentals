def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not starts_with_2_letters(s):
        return False
    if not six_char(s):
        return False
    if not num_mid_plate(s):
        return False
    if not first_not_zero(s):
        return False
    if not all_is_alnum(s):
        return False
    return True


def all_is_alnum(s):
    return s[0:6].isalnum()


def first_not_zero(s):
    return s[0] != "0"


def six_char(s):
    return len(s) >= 2 and len(s) <= 6


def num_mid_plate(s):
    return not (s[2].isnumeric() and s[3].isnumeric() and s[4].isnumeric())


def starts_with_2_letters(s):
    return s[:2].isalpha()


main()

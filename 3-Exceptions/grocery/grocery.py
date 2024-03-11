grocery_list = {}

while True:
    try:
        item = input("What do you want: ").strip().lower()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    except EOFError:
        print("\n")
        for key in sorted(grocery_list):
            print(grocery_list[key], key.upper())
        break

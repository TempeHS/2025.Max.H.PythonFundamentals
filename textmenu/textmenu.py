def choice():
    print("choose an option")
    print("option 1: ", "option 2: ", "option 3: ", "option 4 exit: ", sep="\n")
    user_choice = input("what u pick:")
    while True:
        if user_choice.startswith("1"):
            print("choice 1")
        if user_choice.startswith("2"):
            print("choice 2")
        if user_choice.startswith("3"):
            print("choice 3")
        if user_choice.startswith("4"):
            print("goodbye")
            break


choice()

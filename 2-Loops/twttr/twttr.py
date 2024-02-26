def main():
    vowel = ("a", "e", "i", "o", "u")
    userinput = input("say stuff ")
    userinputstripped = "".join(char for char in userinput if char.lower() not in vowel)
    print(userinputstripped)


main()

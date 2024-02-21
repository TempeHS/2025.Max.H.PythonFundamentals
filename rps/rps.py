def main():
    player_Choice = input("Rock, Paper, or Scissors? ").lower()
    computer_Choice = "rock"
    if player_Choice == "rock" and computer_Choice == "rock":
        print("Tie")
    elif player_Choice == "paper" and computer_Choice == "rock":
        print("Win")
    elif player_Choice == "scissors" and computer_Choice == "rock":
        print("Loss")
    else:
        print("Invalid input")


main()

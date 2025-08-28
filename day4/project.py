import random

candidate_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper of 2 for Scissors."))
computer_selection = random.randint(0, 2)

selection = ["Rock", "Paper", "Scissors"]
print(f"You chose {selection[candidate_selection]} and computer chose {selection[computer_selection]}.")

if candidate_selection >= 3 or candidate_selection <0:
    print("You typed an invalid number. You lose!")
elif candidate_selection == 0 and computer_selection == 2:
    print("You win!")
elif candidate_selection < computer_selection:
    print("You lose!")
elif candidate_selection == computer_selection:
    print("It's a draw!")
elif computer_selection == 0 and candidate_selection ==2:
    print("You win!")

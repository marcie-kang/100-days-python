print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
choice1 = input('       Type "left" or "right"\n').lower()

if choice1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice2 = input('       Type "wait" ot wait of a boat. Type "swim" to swim across.\n').lower()

    if choice2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        choice3 = input('       One red, one yellow and one blue. Which colour do you choose?\n').lower()

        if choice3 == "red":
            print("Burned by fire. Game over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game over.")
        elif choice3 == "yellow":
            print("You found a treasure. You win!")
        else:
            print("You type a wrong answer.")

    elif choice2 == "swim":
        print("Attacked by trout. Game over.")
    else:
        print("You type a wrong answer.")

else:
    print("Fall into a hole. Game Over.")
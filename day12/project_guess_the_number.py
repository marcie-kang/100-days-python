import random
import art


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(answer, guess, attempts):
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        return attempts
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    elif guess > answer:
        print("Too high.")
        return attempts - 1


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard'!: ").lower()

    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


print(art.logo)
print("Welcome to the Number Guessing Game!")

def game():
    print("I'm thinking of a number between 1 and 100.")
    selected_number = random.randint(1, 100)
    life = set_difficulty()
    print(f"You have {life} attempts remaining to guess the number.")

    while life > 0:
        user_guess = int(input("Make a guess: "))
        life = check_answer(selected_number, user_guess, life)
        
        if user_guess == selected_number:
            break

        if life == 0:
            print("You've run out of guesses. Refresh the page to run again.")
        else:
            print(f"Guess again.\nYou have {life} attempts remaining to guess the number.")

game()

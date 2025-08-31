import random
word_list = ["aardvark", "baboon", "camel"]

#Todo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = "_" * len(chosen_word)
print(placeholder)
list_placeholder = list(placeholder)
guessed_char = []

life = 6
game_over = False

# Todo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lower case.

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_char:
        print("You've already guessed.")
    else:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                list_placeholder[i] = guess
            elif guess not in chosen_word:
                life -= 1
                print(f"You guessed {guess}, that's not in the word. You lose a life. {life} lives left.")
                break
        
        final = ''.join(list_placeholder)
        print(final)
        
        if "_" not in final:
            game_over = True
            print("Yon win.")
        elif life == 0:
            game_over = True
            print("Game over.")
    
    guessed_char.append(guess)

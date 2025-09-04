import random

card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def add_card(card_list, final_value):
    random_card = random.choice(card_deck)
    
    if final_value >= 10 and random_card == 11:
        card_list.append(1)
        final_value += 1
    elif final_value < 10 and random_card == 11:
        card_list.append(11)
        final_value += 11
    else:
        card_list.append(random_card)
        final_value += random_card
    
    return final_value

def print_result(user_card, computer_card, user_value, computer_value):
    print(f"     Your final hand: {user_card}, final score: {user_value}")
    print(f"     Computer's final hand: {computer_card}, final score: {computer_value}")

def blackjack():
    user_card = []
    computer_card = []
    user_value = 0
    computer_value = 0
    is_continue = False
    is_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
    user_value = add_card(user_card, user_value)
    computer_value = add_card(computer_card, computer_value)

    if is_start == 'y':
        is_continue = True
    
    while is_continue:
        user_value = add_card(user_card, user_value)
        computer_value = add_card(computer_card, computer_value)
        
        print(f"Your cards: {user_card}, current score: {user_value}.\nComputer's first card: {computer_card[0]}")
        
        if user_value > 21:
            is_continue == False
            print("You went over. You lose :(")
            print_result(user_card, computer_card, user_value, computer_value)
            
            blackjack()
            break
        
        should_add = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        
        while computer_value < 17 and computer_Value:
            computer_value = add_card(computer_card, computer_value)

        if should_add == 'n' and user_value <= 21:
            is_continue = False
            print_result(user_card, computer_card, user_value, computer_value)
            
            if computer_value > 21:
                print("Computer went over. You win :)")
            elif user_value > computer_value:
                print("You win :)!")
            elif user_value < computer_value:
                print("You lose :(!")
            elif user_value == computer_value:
                print("You draw!")
            
            blackjack()

blackjack()


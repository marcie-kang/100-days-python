import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def add_card(card_list, final_value):
    random_card = random.choice(cards)
    
    if final_value >= 10 and random_card == 11:
        card_list.append(1)
    elif final_value < 10 and random_card == 11:
        card_list.append(11)
    else:
        card_list.append(random_card)
        
def card_value(cards):
    return sum(cards)

def calculating(u_card_value, c_card_value):
    if u_card_value == c_card_value1:
        return "You draw."
    elif u_card_value > 21:
        return "You went over. You lose."
    elif c_card_value > 21:
        return "Computer went over. You win."
    elif u_card_value > c_card_value:
        return "You win!"
    elif c_card_value > u_card_value:
        return "You lose!"
    
user_card = []
computer_card = []
user_value = 0
computer_value = 0
is_game_over = False

for i in range(2):
    add_card(user_card, user_value)
    add_card(computer_card, computer_value)

print(user_card, computer_card)

# while not is_game_over:
#     is_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
# 
#     if is_start == 'y':
#         user_value = card_value(user_card)
#         computer_value = card_value(computer_card)
#         
#         print(f"Your cards: {user_card}, current score: {user_value}.\nComputer's first card: {computer_card[0]}")
#         
#         if user_value > 21:
#             is_continue == False
#             print("You went over. You lose :(")
#             print_result(user_card, computer_card, user_value, computer_value)
#             
#             blackjack()
#             break
#         
#         should_add = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#         
#         while computer_value < 17 and computer_Value:
#             computer_value = add_card(computer_card, computer_value)
# 
#         if should_add == 'n' and user_value <= 21:
#             is_continue = False
#             print_result(user_card, computer_card, user_value, computer_value)
#             

            

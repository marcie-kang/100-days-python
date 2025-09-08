import random
from art import logo, vs
from game_data import data

is_game_over = False
current_score = 0

print(logo)
random_A = random.randint(0,49)

def compare_follower(rand_A, rand_B, score):
    if data[rand_A]['follower_count'] > data[rand_B]['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}.")
        return score
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        return "end"

while not is_game_over:
    print(f"Compare A: {data[random_A]['name']}, {data[random_A]['description']}, from {data[random_A]['country']}.")

    random_B = random.randint(1, 50)

    while random_A == random_B:
        random_B = random.randint(1,50)

    print(vs)
    print(f"Against B: {data[random_B]['name']}, {data[random_B]['description']}, from {data[random_B]['country']}.")

    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    if answer == "A":
        result = compare_follower(random_A, random_B, current_score)
        current_score = result
    else:
        result = compare_follower(random_B, random_A, current_score)
        current_score = result

    if result == "end":
        is_game_over = True
    else:
        random_A = random_B

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

enemies = 1

def increase_enemies(enemy):
    return enemy + 1

enemies = increase_enemies(enemies)
print(enemies)


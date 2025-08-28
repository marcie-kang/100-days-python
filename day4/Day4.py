import random
# import my_module

random_integer = random.randint(0, 1)
# print(random_integer)
# print(my_module.my_favourite_number)

# random_number_0_to_1 = random.random() * 10
# # print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

# if random_integer == 0:
#     print("Heads")
# else:
#     print("Tails")

friends = ["Alice", "Bob", "Marcie", "Joy", "Chloe"]

random_index = random.randint(0, len(friends)-1)
print(friends[random_index])


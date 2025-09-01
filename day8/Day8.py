# def greet():
#     print("Hi")
#     print("Hello")
#     print("World")
# 
# greet()

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# 
# greet_with("Angela", "LA")
# greet_with(location = "California", name = "Bob")

# def calculate_love_score(name1, name2):
#     final_name1 = name1.upper()
#     final_name2 = name2.upper()
#     true = 0
#     love = 0
# 
#     for char in final_name1:
#         if char == "E":
#             true += 1
#             love += 1
#         elif char == "T" or char == "R" or char == "U":
#             true += 1
#         elif char == "L" or char == "O" or char == "V":
#             love += 1
#     
#     for char in final_name2:
#         if char == "E":
#             true += 1
#             love += 1
#         elif char == "T" or char == "R" or char == "U":
#             true += 1
#         elif char == "L" or char == "O" or char == "V":
#             love += 1
#     
#     print(str(true) + str(love))

def calculate_love_score(name1, name2):
    combined_name = (name1 + name2).upper()
    true = sum(combined_name.count(char) for char in "TRUE")
    love = sum(combined_name.count(char) for char in "LOVE")
    
    print(str(true) + str(love))
    
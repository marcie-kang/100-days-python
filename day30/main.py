
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sdfsf"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} key does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file was closed.")

# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError
#
# bmi = weight / height ** 2
# print(bmi)

fruits = ["Apple", "Pear", "Orange"]

try:
    def make_pie(index):
        fruit = fruits[index]
        print(fruit + " pie")

except IndexError:
    print("Fruit pie")

make_pie(4)
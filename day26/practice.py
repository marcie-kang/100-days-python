# old_list = [1, 2, 3]
# new_list = [n+1 for n in old_list]

# name = "Angela"
# new_list = [chr.upper() for chr in name]
#
# new_numbers = [num * 2 for num in range(1,5)]
#
# names = ["Angela", "Tom", "Eleanor", "Jimmy", "jin", "Marcie", "Joy", "Dave", "Chloe", "Jay", "Hanna", "Han"]
# long_names = [name.upper() for name in names if len(name) > 5]
#
# print(long_names)
# import random
#
# names = ["Angela", "Tom", "Eleanor", "Jimmy", "jin", "Marcie", "Joy", "Dave", "Chloe", "Jay", "Hanna", "Han"]
#
# students_scores = {student:random.randint(1,100) for student in names}
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
#
# print(passed_students)

# student_dict = {
#     "student": ["Angela", "Jin", "Tom"],
#     "score": [56, 66, 78]
# }

# for (key, value) in student_dict.items():
#     print(key)

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

# import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# for (index, row) in student_data_frame.iterrows():
#     if row.student == "Angela":
#         print(row.score)

#TODO 1. Creat a dictionary in this format:
#{"A": "Alpha", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

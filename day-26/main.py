# List comprehension

# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# range_list = [n * 2 for n in range(1, 5)]
# print(range_list)

# Conditional List comprehension

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
# print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# Dictionary comprehension

import random

# new_dict = { new_key: new_value for item in list }
# new_dict = { new_key: new_value for (key, value) in dict.items() }
# new_dict = { new_key: new_value for (key, value) in dict.items() if test }

# new_dict = { new_key: new_value for item in list }
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score = {student: random.randint(1, 100) for student in names}
print(students_score)

# new_dict = { new_key: new_value for (key, value) in dict.items() }
passed_students = {
    student: score for (student, score) in students_score.items() if score >= 60
}
print(passed_students)

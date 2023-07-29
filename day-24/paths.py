# Reading a file
# Absolute path
# with open("/Users/rich1986/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Relative path
with open("../../../my_file.txt") as file:
    contents = file.read()
    print(contents)

# Write to file - 'w' => write - 'a' => append
# Create new file
# relative path
# with open("new_file.txt", mode="w") as file:
#     file.write("\nNew text.")

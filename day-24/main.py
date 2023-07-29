# Reading a file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Write to file - 'w' => write - 'a' => append
# Create new file
with open("new_file.txt", mode="w") as file:
    file.write("\nNew text.")

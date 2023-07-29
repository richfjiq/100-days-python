# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    for name in names:
        filename = f"letter_for_{name.strip()}.txt"
        letter_edited = letter.replace("[name]", f"{name.strip()}")
        with open(f"./Output/ReadyToSend/{filename}", mode="w") as file:
            file.write(f"{letter_edited}")

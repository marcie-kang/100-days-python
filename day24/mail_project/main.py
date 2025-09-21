PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

with open ("Input/Names/invited_names.txt", mode="r") as name_file:
    names = name_file.readlines()

for name in names:
    trimmed_name = name.strip()
    with open (f"Output/ReadyToSend/{name}.txt", mode="w") as final_letter:
        final_letter.write(letter.replace(PLACEHOLDER, trimmed_name))

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        personalized_letter = letter_content.replace("[name]", stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as output_file:
            output_file.write(personalized_letter)

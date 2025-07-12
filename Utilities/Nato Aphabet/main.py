import pandas as pd

dt = pd.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in dt.iterrows()}

def generate_phonetic():
    word_to_convert = input("Enter a word: ").upper()
    try:
        phonetic_list = [new_dict[letter] for letter in word_to_convert]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()
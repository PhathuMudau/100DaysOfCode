import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}:

data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# print(data_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

succeed = False

while not succeed:

    user_input = input("Enter a word: ").upper()
    try:
        nato_code = [data_dict[letter] for letter in user_input]
    except KeyError:
        succeed = False
        print("Sorry. Only letters in the alphabet please!")
    else:
        succeed = True
        print(nato_code)

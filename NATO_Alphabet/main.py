import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dataframe = pd.DataFrame(nato_data)

nato_dictionary = {row["letter"]:row["code"] for index,row in nato_alphabet_dataframe.iterrows()}  
# print(nato_dictionary)

user_input = input("Enter a word: ")
result = [nato_dictionary[letter.upper()] for letter in user_input]
print(result)
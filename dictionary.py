import json
from datetime import datetime
from difflib import get_close_matches

def create_dict(path):
    return json.load(open(path))

def does_value_exist(word, dict):
    if word in dict.keys():
        return True
    else:
        return False

def find_value(word, dict):
    return dict[word]

data_set_alpha = create_dict('data.json')

word = input("Enter word to find meaning: ").lower()

if does_value_exist(word, data_set_alpha):
    for meaning in find_value(word, data_set_alpha):
        print(meaning)
elif get_close_matches(word, data_set_alpha.keys(), 1):
    new_words = get_close_matches(word, data_set_alpha.keys(), 1)[0]
    correct_word = input("Did you mean %s? yes or no[y/n]: " %new_words)
    if correct_word == 'yes' or correct_word == 'y':
        for meaning in find_value(get_close_matches(word, data_set_alpha.keys(), 1)[0], data_set_alpha):
            print(meaning)
    else:
        print("not there")

else:
    print("not there")

import json
from difflib import get_close_matches

# Read JSON File
data = json.load(open("DictionaryApp/cdata.json"))

# Get JSON File
def readJson(data, key):
    if key in data:
        value = data[key]
        return (len(value), value)
    elif key.title() in data:
        value = data[key.title()]
        return (len(value), value)
    elif key.upper() in data:
        value = data[key.upper()]
        return (len(value), value)
    recommended = get_close_matches(key, data.keys())[0]
    question = input("Do you mean %s, Yes or No: " % (recommended)).lower()
    answered = False
    while (len(get_close_matches(key, data.keys())) > 0) and (answered == False):
        if question == "yes":
            value = data[recommended]
            return (len(value), value)

        elif question == "no":
            return "Word does not exist, please double check"

        else:
            question = input("Wrong input!\nDo you mean %s, Yes or No: " % (recommended)).lower()

    else:
        return (-1, -1)


# Print the derived word
def printDef(tupWord):
    if isinstance(tupWord, tuple):
        if tupWord[0] == 1:
            print("{} - {}".format(1, tupWord[1][0]))
        elif tupWord[0] > 1:
            for i in range(tupWord[0]):
                print("{} - {}".format(i+1, tupWord[1][i]))
        else:
            print("Word does not exist, please double check.")
    elif isinstance(tupWord, str):
        print(tupWord)

# Main execution
while True:
    word = input("Enter a word: ").lower()
    if word != "exitp":
        meaning = readJson(data, word)
        printDef(meaning)
    else:
        break
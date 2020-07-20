import json
import difflib
from difflib import SequenceMatcher

# Read JSON File
data = json.load(open("data.json"))

# Get JSON File
def readJson(data, key):
    if key in data:
        value = data[key]
        return (len(value), value)

    else:
        return (-1, -1)


# Print the derived word
def printDef(tupWord):
    if tupWord[0] == 1:
        print("{} - {}".format(1, tupWord[1][0]))
    elif tupWord[0] > 1:
        for i in range(tupWord[0]):
            print("{} - {}".format(i+1, tupWord[1][i]))
    else:
        print("Word does not exist, please double check.")

# Main execution
while True:
    word = input("Enter a word: ").lower()
    if word != "exitp":
        meaning = readJson(data, word)
        printDef(meaning)
    else:
        break
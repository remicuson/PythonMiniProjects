import pandas
import os
import time

def makerSentence(inp):
    questions = ("Why", "How", "What", "Where", "Is")
    inp = inp.capitalize()
    if inp.startswith(questions):
        word = inp + "?" + " "
    else:
        word = inp + "." + " "
    return word

# word = ""
# while True:
#     inp = input("Say Something: ")
#     if inp == "\end":
#         print(word)
#         break
#     else:
#         word = word + makerSentence(inp)

while True:
    if os.path.exists("temps_today.csv"):
        data = pandas.read_csv("temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exist")

    time.sleep(10)



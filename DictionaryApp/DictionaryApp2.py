import mysql.connector
from difflib import get_close_matches

# This application differs from the first one because we are querying from the database in this application

def databaseQuery(key, cursor):
    search = key[0] + "%"
    cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % key)
    data = cursor.fetchall()

    if len(data) > 0:
        count = 0
        for definition in data:
            print("{} - {}".format(count+1, definition[1]))
            count += 1

    cursor.execute("SELECT * FROM Dictionary WHERE Expression LIKE '%s' " % search)
    possibleMatches = cursor.fetchall()
    candidate = get_close_matches(key, dict(possibleMatches))[0]
    if candidate:
        while True:
            answer = input("Do you mean %s? Enter Yes or No" % candidate)
            if answer == "Yes":
                cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % candidate)
                data = cursor.fetchall()
                count = 0
                for definition in data:
                    print("{} - {}".format(count + 1, definition[1]))
                    count += 1
                break

            elif answer == "No":
                print("Word does not exist")
                break

            else:
                print("Wrong Input!\n")
    else:
        print("Word does not exist")

con = mysql.connector.connect(
    user =  "ardit700_student",
    password = "ardit700_student",
    host="108.167.140.122",
    database= "ardit700_pm1database"
)

cursor = con.cursor()
while True:
    key = input("Enter a word: ").lower()
    if key != "exitp":
        databaseQuery(key, cursor)
    else:
        break






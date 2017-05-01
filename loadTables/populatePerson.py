#!/usr/bin/python
# assemble person tables, login tables

import sys
import hashlib
import random

print( 'Number of arguments:', len(sys.argv), 'arguments.')
print( 'Argument List:', str(sys.argv))

print(len(sys.argv))
if len(sys.argv) < 2:
    print("Bad number of args")
    exit()




# Use the following syntax, dilineated by commas.
# Quotes are removed. 
#
# Number,
# Gender,
# GivenName,
# MiddleInitial,
# Surname,
# StreetAddress,
# City,
# State,
# CountryFull,
# Username,
# Password,
# Birthday,
# EmailAddress,
# TelephoneNumber

fileHandler1 = open(sys.argv[1], "r")
splitLines = []
for line in fileHandler1:
    for char in line:
        if char in "\"":
            line = line.replace(char,'')
    splitLine = line.split(",")
    splitLines.append(splitLine)

# insert into TABLE values(01,'varchar1','varchar2' );

# for element in splitLines:
#     print( element)
#     print()

fileHandler2 = open("persons.txt", "w")
fileHandler3 = open("logins.txt", "w")

salt = "secretstring"

for element in splitLines:
    queryString = ""
    queryString = queryString + "INSERT INTO Person "
    queryString = queryString + "VALUES ( "

    queryString = queryString + "\"" + element[2] + "\"" + ", "
    queryString = queryString + "\"" + element[4] + "\"" + ", "


    usernameToInsert = element[9] + str(random.randint(0,9999))
    queryString = queryString + "\"" + usernameToInsert + "\"" + ", "






    # gender
    queryString = queryString + "\"" + element[1][0] + "\"" + ", "


    # mdy -> ymd
    monthDayAndYear = element[11].split("/")
    dateToInsert = monthDayAndYear[2] + "-" + monthDayAndYear[0] + "-" + monthDayAndYear[1]

    queryString = queryString + "\"" + dateToInsert + "\"" + ", "

    queryString = queryString + "\"" + element[5] + "\"" + ", "
    queryString = queryString + "\"" + element[6] + "\"" + ", "
    queryString = queryString + "\"" + element[7] + "\"" + ", "

    queryString = queryString + "\"" + element[13][:-1] + "\"" + ", "   #strip ending \n from telephone number
    queryString = queryString + "\"" + element[12] + "\"" + " "
    queryString = queryString + ");\n"

    # print(queryString)
    # WRITE OUT TO PERSON TABLE
    fileHandler2.write(queryString)





    # NEXT WE DO LOGINS
    queryString = ""
    queryString = queryString + "INSERT INTO Login "
    queryString = queryString + "VALUES ( "
    queryString = queryString + "\"" + usernameToInsert + "\"" + ", "



    # password
    password = element[10]
    passwordAndSalt = password + salt

    m = hashlib.sha256()
    m.update((password + salt).encode('utf-8'))
    hashedPassword = m.hexdigest()

    queryString = queryString + "\"" + hashedPassword + "\"" + " "
    queryString = queryString + ");\n"

    # print(queryString)
    fileHandler3.write(queryString)
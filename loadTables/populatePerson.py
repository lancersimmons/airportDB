#!/usr/bin/python
# assemble person tables, login tables

import sys

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


for element in splitLines:
    queryString = ""
    queryString = queryString + "INSERT INTO Person "
    queryString = queryString + "VALUES ( "

    queryString = queryString + "\"" + element[2] + "\"" + ", "
    queryString = queryString + "\"" + element[4] + "\"" + ", "
    queryString = queryString + "\"" + element[9] + "\"" + ", "
    queryString = queryString + "\"" + element[10] + "\"" + ", "
    queryString = queryString + "\"" + element[1][0] + "\"" + ", "
    queryString = queryString + "\"" + element[11] + "\"" + ", "
    queryString = queryString + "0" + ", "              # age
    queryString = queryString + "\"" + element[5] + "\"" + ", "
    queryString = queryString + "\"" + element[6] + "\"" + ", "
    queryString = queryString + "\"" + element[7] + "\"" + ", "
    queryString = queryString + "\"" + element[8] + "\"" + ", "
    queryString = queryString + "\"" + element[13][:-1] + "\"" + ", "   #strip ending \n from telephone number
    queryString = queryString + "\"" + element[12] + "\"" + " "
    queryString = queryString + ");\n"

    # print(queryString)
    fileHandler2.write(queryString)
    # exit()

fileHandler2.close()
fileHandler2 = open("logins.txt", "w")

for element in splitLines:
    queryString = ""
    queryString = queryString + "INSERT INTO Login "
    queryString = queryString + "VALUES ( "
    queryString = queryString + "\"" + element[9] + "\"" + ", "
    queryString = queryString + "\"" + element[10] + "\"" + " "
    queryString = queryString + ");\n"

    # print(queryString)
    fileHandler2.write(queryString)
    # exit()




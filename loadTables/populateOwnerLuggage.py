#!/usr/bin/python
# assemble owner, luggage tables

import sys
import random
import uuid

print( 'Number of arguments:', len(sys.argv), 'arguments.')
print( 'Argument List:', str(sys.argv))

print(len(sys.argv))
if len(sys.argv) != 1:
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

# Pass in the roles.txt file
fileHandler1 = open("roles.txt", "r")
splitLines = []
for line in fileHandler1:
    splitLine = line.split()
    splitLines.append(splitLine)



fileHandler2 = open("ownerAndLuggage.txt", "w")


for element in splitLines:

    if element[2] == "Customer":
        numberOfBags = random.randint(0,1) + random.randint(0,2)
        usernameToInsert = element[5]
        for char in usernameToInsert:
            if char in "\",":
                usernameToInsert = usernameToInsert.replace(char,'')
            
        # print(usernameToInsert)
        # print(numberOfBags)
        # print()

        for bag in range(0,numberOfBags):

            # Write to luggage table
            thisBagId = str(uuid.uuid4())
            thisBagWeight = str(random.randint(15,25) + random.randint(0,25))
            thisOwnershipId = str(uuid.uuid4())
            # print(thisBagId)
            # print(thisBagWeight)

            queryString = ""
            queryString = queryString + "INSERT INTO Luggage "
            queryString = queryString + "VALUES ( "

            queryString = queryString + "\"" + thisBagId + "\"" + ", "
            queryString = queryString + "\"" + thisBagWeight + "\"" + " "
            queryString = queryString + ");\n"

            fileHandler2.write(queryString)


            # Write to owner table

            queryString = ""
            queryString = queryString + "INSERT INTO Owner "
            queryString = queryString + "VALUES ( "

            queryString = queryString + "\"" + thisOwnershipId + "\"" + ", "
            queryString = queryString + "\"" + usernameToInsert + "\"" + ", "
            queryString = queryString + "\"" + thisBagId + "\"" + " "
            queryString = queryString + ");\n"

            fileHandler2.write(queryString)

        exit()
    else:
        pass
        # do nothing for employees

fileHandler2.close()

exit()


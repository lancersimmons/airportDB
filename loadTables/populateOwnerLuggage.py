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
            
        print(usernameToInsert)
        print(numberOfBags)
        print()

        for bag in range(0,numberOfBags):
            print("Hey!")
            print(uuid.uuid4())
            print(len(str(uuid.uuid4())))

            # queryString = ""
            # queryString = queryString + "INSERT INTO Luggage "
            # queryString = queryString + "VALUES ( "

            # queryString = queryString + "\"" + usernameToInsert + "\"" + ", "
            # queryString = queryString + "\"" + thisJob + "\"" + ", "
            # queryString = queryString + "\"" + str(thisSalary) + "\"" + " "
            # queryString = queryString + ");\n"


    else:
        pass
        # do nothing for employees

    print(element)
    # exit()


    # # randomly determine who are employees or customers
    # role = ""
    # thisJob = ""
    # thisSalary = 0
    # frequentFlyer = 0
    # if random.randint(0,19) == 0:
    #     role = "employee"        
    #     randomJobInt = random.randint(0,6)
    #     thisJob = jobs[randomJobInt]
    #     thisSalary = salaries[randomJobInt]
    #     thisSalary = thisSalary + (random.randint(-8,16) * 500)
    # else:
    #     role = "customer"
    #     if random.randint(0,7) == 0:
    #         frequentFlyer = 1


    # # Strip " and , chars from usernames
    # usernameToInsert = element[7]
    # for char in usernameToInsert:
    #     if char in "\",":
    #         usernameToInsert = usernameToInsert.replace(char,'')

    # # print(usernameToInsert)
    # # print(thisJob)
    # # print(thisSalary)

    # if role == "employee":
    #     queryString = ""
    #     queryString = queryString + "INSERT INTO Employee "
    #     queryString = queryString + "VALUES ( "

    #     queryString = queryString + "\"" + usernameToInsert + "\"" + ", "
    #     queryString = queryString + "\"" + thisJob + "\"" + ", "
    #     queryString = queryString + "\"" + str(thisSalary) + "\"" + " "
    #     queryString = queryString + ");\n"

    # else:
    #     queryString = ""
    #     queryString = queryString + "INSERT INTO Customer "
    #     queryString = queryString + "VALUES ( "

    #     queryString = queryString + "\"" + usernameToInsert + "\"" + ", "
    #     queryString = queryString + "\"" + str(frequentFlyer) + "\"" + " "
    #     queryString = queryString + ");\n"

    # print(queryString)
    # fileHandler2.write(queryString)
    # exit()

fileHandler2.close()

exit()


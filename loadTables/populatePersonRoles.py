#!/usr/bin/python
# assemble person tables, login tables

import sys
import random

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

# Pass in the persons.txt file
fileHandler1 = open("persons.txt", "r")
splitLines = []
for line in fileHandler1:
    splitLine = line.split()
    splitLines.append(splitLine)



# insert into TABLE values(01,'varchar1','varchar2' );

# for element in splitLines:
#     print( element[7], element[8])
#     print()


fileHandler2 = open("roles.txt", "w")


jobs = ["Senior_Pilot", "Junior_Pilot", "Janitor", "Customer_Service", "Security_Guard", "TSA_Agent", "Booking_Agent", "Steward"]
salaries = [140000, 110000, 30000, 30000, 32000, 30000, 36000, 34000]
for element in splitLines:

    # randomly determine who are employees or customers
    role = ""
    thisJob = ""
    thisSalary = 0
    frequentFlyer = 0
    if random.randint(0,19) == 0:
        role = "employee"        
        randomJobInt = random.randint(0,6)
        thisJob = jobs[randomJobInt]
        thisSalary = salaries[randomJobInt]
        thisSalary = thisSalary + (random.randint(-8,16) * 500)
    else:
        role = "customer"
        if random.randint(0,7) == 0:
            frequentFlyer = 1


    # Strip " and , chars from usernames
    usernameToInsert = element[7]
    for char in usernameToInsert:
        if char in "\",":
            usernameToInsert = usernameToInsert.replace(char,'')

    # print(usernameToInsert)
    # print(thisJob)
    # print(thisSalary)

    if role == "employee":
        queryString = ""
        queryString = queryString + "INSERT INTO Employee "
        queryString = queryString + "VALUES ( "

        queryString = queryString + "\"" + usernameToInsert + "\"" + ", "
        queryString = queryString + "\"" + thisJob + "\"" + ", "
        queryString = queryString + "\"" + str(thisSalary) + "\"" + " "
        queryString = queryString + ");\n"

    else:
        queryString = ""
        queryString = queryString + "INSERT INTO Customer "
        queryString = queryString + "VALUES ( "

        queryString = queryString + "\"" + usernameToInsert + "\"" + ", "
        queryString = queryString + "\"" + str(frequentFlyer) + "\"" + " "
        queryString = queryString + ");\n"

    # print(queryString)
    fileHandler2.write(queryString)
    # exit()

fileHandler2.close()

exit()


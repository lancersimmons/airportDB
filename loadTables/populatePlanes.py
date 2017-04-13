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


fileHandler2 = open("simplePlanes.txt", "w")


airlineCompanies = ["United", "Southwest", "Delta", "JetBlue"]
models = [1,2,3,4,5]

for x in range(0,25):

    # Write to luggage table
    thisPlaneId = str(uuid.uuid4())
    thisModelNo = str(models[random.randint(0,len(models) - 1)])
    thisAirline = str(airlineCompanies[random.randint(0,len(airlineCompanies) - 1)])

    # print(thisBagId)
    # print(thisBagWeight)

    queryString = ""
    queryString = queryString + "INSERT INTO Plane "
    queryString = queryString + "VALUES ( "

    queryString = queryString + "\"" + thisPlaneId + "\"" + ", "
    queryString = queryString + "\"" + thisModelNo + "\"" + ", "
    queryString = queryString + "\"" + thisAirline + "\"" + " "
    queryString = queryString + ");\n"

    fileHandler2.write(queryString)


fileHandler2.close()

exit()


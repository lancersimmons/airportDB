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
users = []
freqers = []
splitLines = []
for line in fileHandler1:
    splitLine = line.split()

    if splitLine[2] == "Employee":
        continue
    
    # print(splitLine[5][1:-2])
    users.append(splitLine[5][1:-2])
    
    # print(splitLine[6][1:-1])
    freqers.append(str(splitLine[6][1:-1]))

fileHandler2 = open("simpleFlights.txt", "r")

flights = []
for line in fileHandler2:
    splitLine = line.split()
    flights.append(splitLine[5][1:-2])


fileHandler3 = open("bookingsAndLuggage.txt", "w")

for userIndex in range(0, len(users) - 1):
    
    numberFlights = 0
    if (freqers[userIndex] == "1"):
        numberFlights = random.randint(9,20)
    else:
        numberFlights = random.randint(1,8)

    thisDudesFlights = []
    while( len(thisDudesFlights) < numberFlights):
        flightToTake = flights[random.randint(0, len(flights) - 1)]
        if flightToTake not in thisDudesFlights:
            thisDudesFlights.append(flightToTake)
        else:
            continue

    # print(thisDudesFlights)
    

    for flightId in thisDudesFlights:
        thisBookingId = str(uuid.uuid4())
        firstClass = random.randint(-8,1)
        if firstClass < 0:
            firstClass = 0
        firstClass = str(firstClass)

        queryString = ""
        queryString = queryString + "INSERT INTO Booking "
        queryString = queryString + "VALUES ( "

        queryString = queryString + "\"" + thisBookingId + "\"" + ", "
        queryString = queryString + "\"" + users[userIndex] + "\"" + ", "
        queryString = queryString + "\"" + flightId + "\"" + ", "
        queryString = queryString + "\"" + firstClass + "\"" + " "
        queryString = queryString + ");\n"


        # print(queryString)
        fileHandler3.write(queryString)
        


        numberOfBags = random.randint(0,1) + random.randint(0,2)

        for bag in range(0,numberOfBags):

            # Write to owner table
            thisLuggageId = str(uuid.uuid4()) 
            thisBagWeight = str(random.randint(15,25) + random.randint(0,25))

            queryString = ""
            queryString = queryString + "INSERT INTO Owner "
            queryString = queryString + "VALUES ( "

            queryString = queryString + "\"" + str(uuid.uuid4()) + "\"" + ", "
            queryString = queryString + "\"" + users[userIndex] + "\"" + ", "
            queryString = queryString + "\"" + thisBookingId + "\"" + ", "
            queryString = queryString + "\"" + thisBagWeight + "\"" + " "
            queryString = queryString + ");\n"


            # print(queryString)
            fileHandler3.write(queryString)




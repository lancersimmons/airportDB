#!/usr/bin/python
# assemble owner, luggage tables

import sys
import random
import uuid
import datetime
import faker
fake = faker.Faker()

print( 'Number of arguments:', len(sys.argv), 'arguments.')
print( 'Argument List:', str(sys.argv))

print(len(sys.argv))
if len(sys.argv) != 1:
    print("Bad number of args")
    exit()



# Pass in the roles.txt file
fileHandler1 = open("simplePlanes.txt", "r")
planeLines = []
for line in fileHandler1:
    splitLine = line.split("\"")
    planeLines.append(splitLine)
    # print(splitLine)
fileHandler1.close()


# keep track of possible destinations
destinations = []

fileHandler1 = open("simpleAirports.txt", "r")
airportLines = []
for line in fileHandler1:
    splitLine = line.split("\"")
    airportLines.append(splitLine)

    if splitLine[1] not in destinations:
        destinations.append(splitLine[1])

    # print(splitLine)
fileHandler1.close()


fileHandler2 = open("simpleFlights.txt", "w")



for planeIterator in planeLines:

    print(planeIterator)
    print()
    planeId = planeIterator[1]
    print(planeId)
    # exit()


    flightId = str(uuid.uuid4())
    
    thisSource = "err"
    thisDestination = "err"
    while (thisSource == thisDestination):
        thisSource = destinations[random.randint(0,len(destinations)-1)]
        thisDestination = destinations[random.randint(0,len(destinations)-1)]
    departureTime =  fake.date_time_between(start_date="now", end_date="+1d", tzinfo=None)
    departureTime = str(departureTime)[:-3]

    departureTime = datetime.datetime.strptime(departureTime, "%Y-%m-%d %H:%M")

    delta = datetime.timedelta(hours=random.randint(1,6))
    delta = delta + datetime.timedelta(minutes=(random.randint(0,11)*5))

    arrivalTime = departureTime + delta

    # print(thisSource)
    # print(thisDestination)

    # print(departureTime)
    # print(arrivalTime)


    queryString = ""
    queryString = queryString + "INSERT INTO Flight "
    queryString = queryString + "VALUES ( "

    queryString = queryString + "\"" + flightId + "\"" + ", "
    queryString = queryString + "\"" + planeId + "\"" + ", "

    queryString = queryString + "\"" + thisSource + "\"" + ", "
    queryString = queryString + "\"" + thisDestination + "\"" + ", "

    queryString = queryString + "\"" + str(departureTime) + "\"" + ", "

    queryString = queryString + "\"" + str(arrivalTime) + "\"" + " "
    queryString = queryString + ");\n"

    # print(queryString)
    fileHandler2.write(queryString)



    for x in range(0,500):

        flightId = str(uuid.uuid4())

        thisSource = thisDestination
        while (thisSource == thisDestination):
            thisDestination = destinations[random.randint(0,len(destinations)-1)]
        

        departureTime =  fake.date_time_between(start_date="now", end_date="+1y", tzinfo=None)
        departureTime = str(departureTime)[:-3]

        delta = datetime.timedelta(hours=random.randint(1,6))
        delta = delta + datetime.timedelta(minutes=(random.randint(0,11)*5))

        departureTime = arrivalTime + delta

        delta = datetime.timedelta(hours=random.randint(1,6))
        delta = delta + datetime.timedelta(minutes=(random.randint(0,11)*5))

        arrivalTime = departureTime + delta

        # print(thisSource)
        # print(thisDestination)

        # print(departureTime)
        # print(arrivalTime)


        queryString = ""
        queryString = queryString + "INSERT INTO Flight "
        queryString = queryString + "VALUES ( "

        queryString = queryString + "\"" + flightId + "\"" + ", "
        queryString = queryString + "\"" + planeId + "\"" + ", "

        queryString = queryString + "\"" + thisSource + "\"" + ", "
        queryString = queryString + "\"" + thisDestination + "\"" + ", "

        queryString = queryString + "\"" + str(departureTime) + "\"" + ", "

        queryString = queryString + "\"" + str(arrivalTime) + "\"" + " "
        queryString = queryString + ");\n"

        # print(queryString)
        fileHandler2.write(queryString)



fileHandler2.close()

exit()


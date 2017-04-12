#!/usr/bin/python
# assemble person tables

import sys



print( 'Number of arguments:', len(sys.argv), 'arguments.')
print( 'Argument List:', str(sys.argv))

print(len(sys.argv))
if len(sys.argv < 2):
	print("Bad number of args")
	exit()

print(sys.argv[1])



# Use the following syntax, dilineated by commas.
# Quotes are removed. 
#
# Number,Gender,GivenName,MiddleInitial,Surname,
# StreetAddress,City,State,CountryFull,
# Username,Password,Birthday,EmailAddress,TelephoneNumber

fileHandler1 = open(sys.argv[1], "r")
splitLines = []
for line in fileHandler1:
    for char in line:
        if char in "\"":
            line = line.replace(char,'')
    splitLine = line.split(",")
    splitLines.append(splitLine)

# insert into TABLE values(01,'varchar1','varchar2' );

for element in splitLines:
    print( element)










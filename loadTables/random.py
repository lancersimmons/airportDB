#!/usr/bin/python
# assemble person tables

import sys



print( 'Number of arguments:', len(sys.argv), 'arguments.')
print( 'Argument List:', str(sys.argv))

print(sys.argv[1])



# Use the following syntax, dilineated by commas.
# Quotes are removed. 
#
# Number,Gender,GivenName,MiddleInitial,Surname,
# StreetAddress,City,State,CountryFull,
# Username,Password,Birthday,EmailAddress,TelephoneNumber

# fileHandler = open("filename", "r")
# for line in 
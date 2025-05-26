#!/usr/bin/python3

"""
Multiplication Table: a python script that will ask the user to enter a number,
                      then use a for loop to print the multiplication table for that number from 1 to 10.
"""

number = int(input("Enter a number to see its multiplication table: "))
multiplier = 1

for x in range(1,11):
    print("{0} * {1} = {2}".format(number, multiplier, number * multiplier))
    multiplier = multiplier + 1

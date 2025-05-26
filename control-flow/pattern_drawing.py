#!/usr/bin/python3

"""
Pattern Drawing: a script will prompt the user to enter a positive integer, then use nested
                 loops to print a square pattern of that size made of asterisks (*).
"""

size = int(input("Enter the size of the pattern: "))
column = 0

if size < 0:
    print("ERROR: size should be greater than 0")
    quit()

while column != size:
    for x in range(0, size):
        print("*", end="")
    print("\n", end="")
    column = column + 1

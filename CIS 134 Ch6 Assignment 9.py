"""
Project: CIS 134 Ch6 Assignment 9.py
Author: Nicola Ward
Date: 3/22/2024

The purpose of this program is to compute and print the average of numbers from a text file input by
the user. It uses a mapping higher-order function to read and add each number into a list. It then computes
the average by using a reduce higher-order function and an anonymous lambda function, returning the
average. It then outputs said average in the form of a concatenated string.
"""
from functools import reduce
import os

# Functions
def readFromFile(): # Mapping Higher-Order Function

    while True:

        filename = (input("Please enter the file name and extension: ")) # Prompt user to input file name and extension

        numbers = [] # Initialize list

        if os.path.exists(filename): # If file exists

            numbers = [] # Initialize list

            f = open(filename, 'r') # Open file

            for line in f:
                line = line.strip()
                if line == "":
                    break
                    
                number = list(map(int, line.split()))
                numbers.extend(number)
            
            return numbers

        else: # If file doesn't exist
            print("Error. File not found.")


def average(numbers): # Reduce Higher-Order Function

    if numbers: # Check list not empty

        # Calculate average
        total = reduce(lambda x, y: x + y, numbers) # Sum of numbers

        average = total / len(numbers) # Average calc
        
        return average

    else:
        return 0

# Program / Main
def main():

    numbersList = readFromFile()
    avg = average(numbersList)

    # Output
    print("Average: " + str(avg))

if __name__ == "__main__":
    main()


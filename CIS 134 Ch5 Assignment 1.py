"""
Program: CIS 134 Ch5 Assignment 1.py (stats.py)
Author: Nicola Ward
Last Date Modified: 3/1/2024

The purpose of this program is to prompt the user to input a list of
numbers then calculate and display the median, mean and mode of said
input numbers. Each calculation is seperated into its own corresponding
function. The inputs consist of a list of integer numbers. The outputs
are formated to display a single digit number.
"""

# Functions
# Median Function
def median(numbers):
    if not numbers: # If empty, return 0
        return 0
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return (numbers[midpoint] + numbers[midpoint - 1]) / 2

# Mode Function
def mode(numbers):
    if not numbers: # If empty, return 0
        return 0
    else: # Dictionary
        dictionary = {}
        for number in numbers:
            count = dictionary.get(number, None)
            if count == None: # Number entered for the first time
                dictionary[number] = 1
            else: # Number already seen, increment count
                dictionary[number] = count + 1
                
    # Find the Mode
    maximum = max(dictionary.values())
    for key in dictionary:
        if dictionary[key] == maximum:
            mode = key
            return mode

# Mean Function
def mean(numbers):
    if not numbers: # If empty, return 0
        return 0
    
    theSum = 0 # Initialize sum
    
    for number in numbers:
        theSum += number
    return theSum / len(numbers)

# Main Function
def main():
    inputList = input("Enter a list of numbers separated by a space: ")
    numbers = [int(num) for num in inputList.split()]
    
    # Outputs, single digit format
    print("Median: %d" % median(numbers))
    print("Mode: %d" % mode(numbers))
    print("Mean: %d" % mean(numbers))

# Program
if __name__ == "__main__":
    main()

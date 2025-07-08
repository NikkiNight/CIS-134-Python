"""
Program: CIS 134 Ch4 Assignment 4b.py (decimalToOctal.py)
Author: Nicola Ward
Last Date Modified: 2/23/2024

The purpose of this program is to prompt the user to input a decimal
number which the program then converts into its octal's value.
The output displays the decimal's octal value in a string.
"""

#Input
decimal = int(input("Enter a decimal integer: "))

#Convert to Octal
octal = "" # Initialize string empty.

while decimal > 0:
    remainder = decimal % 8
    decimal //= 8
    octal = str(remainder) + octal
print("The Octal value is:", octal)

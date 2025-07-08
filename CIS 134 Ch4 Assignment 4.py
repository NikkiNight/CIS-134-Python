"""
Program: CIS 134 Ch4 Assignment 4.py (octalToDecimal.py)
Author: Nicola Ward
Last Date Modified: 2/23/2024

The purpose of this program is to prompt the user to input an octal
number which the program then converts into its decimal value.
The output displays the octal's decimal value in a string.
"""

#Input
octal = input("Enter an Octal number: ")

#Convert to Decimal
decimal = 0 # Initialize variable.

exponent = len(octal) - 1
for digit in octal:
    decimal += int(digit) * 8 ** exponent 
    exponent -= 1
print("The decimal value is:", str(decimal))

"""
Program: CIS 134 Ch5 Assignment 6.py
Author: Nicola Ward
Last Date Modified: 3/1/2024

The purpose of this program is to display an inputed number in a given base.
The user is prompted to enter a number and a base, and the program then displays
the input number in the specified base. Both inputs are integers. The
decimalToRep function uses a lookup table to convert the input number to the
specified base, returning the result as a string. Additionally, the main
function displays examples of numbers represented in different bases,
as requested by the assignment. These are three distinct numbers which are
shown in three different bases.
"""

def decimalToRep(decimal, base):
    
    # Lookup Table
    lookupTable = {2: '01', # Binary
                   8: '01234567', # Octal
                   16: '0123456789ABCDEF' # Hexadecimal
                   }
    
    # Calculations
    if decimal == 0: # If 0, print 0
        return '0'

    result = '' # Initialize result
    
    while decimal > 0:
        remainder = decimal % base
        result = lookupTable[base][remainder] + result
        decimal //= base        

    return str(result)

def main():    
    # Inputs
    decimal = int(input("Enter a number to represent: "))
    base = int(input("Enter a base: "))

    # Output
    if base == 2:
        baseName = "Binary"
    elif base == 8:
        baseName = "Octal"
    else:
        baseName = "Hexadecimal"
        
    print(baseName + " representation:", decimalToRep(decimal, base)) # Display result

    # Test numbers in multiple bases
    print(end="\n") # New line/space
    print("Additional numbers:\n" + "Binary representation of 42:", decimalToRep(42, 2)) # Binary rep of 42
    print("Octal representation of 10:", decimalToRep(10, 8))
    print("Hexadecimal representation of 72:", decimalToRep(72, 16))

if __name__ == "__main__":
    main()

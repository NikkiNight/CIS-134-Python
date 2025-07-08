"""
Program: CIS 134 Ch4 Assignment 6.py
Author: Nicola Ward
Last Date Modified: DATE

The purpose of this program is to prompt the user to input a decimal
number which the program then converts into its octal's value.
The output displays the decimals octal value in a string.
"""
#ENCRYPT

#Input
message = input("Enter a message to encrypt: ")

#Calc
encryptedString = ""
for char in message:
    # Add 1 to each character's numeric ASCII value
    ordValue = ord(char) + 1

    # Convert to bit string and shift one place to the left
    bitString = ""
    while ordValue > 0:
        remainder = ordValue % 2
        ordValue //= 2
        bitString = str(remainder) + bitString

    # Bit Shift
    shiftedBits = bitString[1:] + bitString[0]

    encryptedString += shiftedBits + " "

#Display the result
print("Encrypted Message:", encryptedString.strip())



#DECRYPT. CHANGE VARIABLE NAMES. REREAD CHAPTER.

# Input
message = input("Enter a message to decrypt: ")

# Decryption without functions
decryptedString = ""
for bits in message.split():
    # Reverse bit shift operation
    bit_string = bits[-1] + bits[:-1]

    # Convert bit string to decimal
    decimal_value = 0
    for i, bit in enumerate(bit_string[::-1]):
        decimal_value += int(bit) * (2 ** i)

    # Subtract 1 to get the original ASCII value
    original_ord = decimal_value - 1

    # Convert ASCII value to character
    decrypted_char = chr(original_ord)

    decryptedString += decrypted_char

# Display the decrypted result
print("Decrypted Message:", decryptedString)


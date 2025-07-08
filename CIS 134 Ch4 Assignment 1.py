"""
Program: CIS 134 Ch4 Assignment 1.py
Author: Nicola Ward
Last Date Modified: 2/23/2024

The purpose of this program is to prompt the user to enter a plaintext input,
then input a distance value for the encryption. The program encrypts the plaintext
using the Caesar cipher and displays the encrypted text back to the user.
"""

# Input
text = input("Enter some text: ")
distance = int(input("Enter a distance value: "))

# Caesar Cipher encryption
code = ""  # Initialize code variable

for ch in text:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - (ord('z') - ordvalue + 1)

    code += chr(cipherValue)

# Output
print("Encrypted text:", code)

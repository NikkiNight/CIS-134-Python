"""
Author: Nicola Ward
File: CIS 134 Ch11 Assignment 3.py
Last Date Modified: 27/4/2024

The purpose of this program is to calculate the exponentiation of a
number to a given power, then display the result.
"""
# expo Function
def expo(number, exponent):
   result = 1 # Any Non-Zero Number Raised To 0 = 1

   for i in range(exponent):
      result *= number # Number * Itself, Exponent Amount Of Times
   print(result)
   
"""
Computation complexity of expo function is O(n), n being
the amount input into the exponent as it will execute
that amount of times.
"""

# Input
number = int(input("Please enter a number: ")) # Number Prompt

while True:
   exponent = int(input("Please enter exponent value: ")) # Exponent Prompt
   
   if exponent < 0: # Error If Negative Exponent
      print("Error. Exponent cannot be a negative number.")
      continue
   else: # Call Function
      expo(number, exponent)
      break

"""
Program: CIS 134 Ch3 Assignment 2.py
Author: Nicola Ward
Last Date Modified: 2/16/2024

The purpose of this program is to prompt the user to input the length
of three different sides of a triangle, determine if said triangle
is a right triangle and then display the result. The inputs are floats
which represent the sides of the triangle. The output is generated based on
the statement of if one side of the triangle squared equals the sum of other
two sides squared. The output, if true, is that it is a right triangle, else,
not a right triangle.
"""

# Inputs
sideA = float(input("Enter the length of side A: "))
sideB = float(input("Enter the length of side B: "))
sideC = float(input("Enter the length of side C: "))

# Calculation & Outputs
if (sideA ** 2 == sideB ** 2 + sideC ** 2) or (sideB ** 2 == sideA ** 2 + sideC ** 2) or (sideC ** 2 == sideA ** 2 + sideB ** 2): # Pythagorean theorem
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")

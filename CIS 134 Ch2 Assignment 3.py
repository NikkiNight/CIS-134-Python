"""
Program: CIS 134 Ch2 Assignment 3.py
Author: Nicola Ward
Last Date Modified: 2/9/2024

The purpose of this program is to prompt the user for input on the
number of new and old rented videos, calculate, then display the total
amount due. The input is an integer representing the number of each
video types rented. The output is a string representing the total amount
due.
"""

#Declarations
newVideos = 3 # Price of new videos
oldVideos = 2 # Price of oldies

#Inputs
new = int(input("Enter amount of new videos: "))
old = int(input("Enter amount of oldies: "))

#Calculations
total = (new * newVideos) + (old * oldVideos)

#Output
print("Total due: $" + str(total))

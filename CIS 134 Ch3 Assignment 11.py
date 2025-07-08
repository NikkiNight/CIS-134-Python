"""
Program: CIS 134 Ch3 Assignment 11.py
Author: Nicola Ward
Last Date Modified: 2/16/2024

The purpose of this program is to prompt the user to input the amount
of money they want to put into the pot, roll two random numbers and if
they sum 7, win $4, if not, lose $1. The input is a float which represents
the amount of money the player puts into the pot. One output displays the
amount of rolls taken until the player reaches $0 in the pot and another
displays the max amount of money that was ever in the pot.
"""

import random

# Declarations
counterRolls = 0

# Inputs
playerPot = float(input("Enter amount of money you want to put into the pot: $"))
maxPot = playerPot # Initialize max pot.

# Calculations
while playerPot != 0:  # While player still has money, roll the dice.
    rollA = random.randint(1, 6)  # Roll a random number. Dice 1.
    rollB = random.randint(1, 6)  # Roll a random number. Dice 2.
    print(rollA, rollB)

    counterRolls += 1  # Add rolls to counter

    if rollA + rollB == 7:  # If the sum of two dice equals 7, player wins $4.
        print("Won $4!") # Output won.
        playerPot += 4 # Add money to playerPot.
        print("Balance: $%0.2f" % playerPot, "\n") # Output remaining balance.
    else:  # If the sum of two dice doesn't equal 7, player loses $1.
        print("Lose $1!") # Output lose.
        playerPot -= 1 # Take money from playerPot.
        print("Balance: $%0.2f" % playerPot, "\n") # Output remaining balance.

    maxPot = max(maxPot, playerPot) # Calc max amount of money ever in the pot.

#Outputs
    if playerPot == 0:        
        print("Amount of rolls taken:", counterRolls) # Display amount of rolls taken.
        print("Maximum amount of money in the pot: $%0.2f" % maxPot) # Display highest amount of money ever in the pot.

"""
Project: CIS 134 Ch6 Assignment 1.py
Author: Nicola Ward
Date: 3/22/2024

The purpose of this program is to prompt the user to input a value, the
program evaluates to see if the input is empty, then it checks to see if the
value entered is 0 or less. If 0 or less, it throws an error and reprompts
the user for input again. If the value entered is a positive number, it
converts the value to a float and calls the newton function that contains
Newton's square root approximation formula. It outputs the estimated square
root and then reprompts the user for input again. If the value entered is
empty, the program exits.
"""

# Function
def newton(number):

    # Declarations
    tolerance = 0.000001
    estimate = 1.0

    # Newton's sqr root approx formula
    while True:
        estimate = (estimate + number / estimate) / 2
        difference = abs(number - estimate ** 2)
        if difference <= tolerance:
            break        
    return estimate


def main():

        number = input("Enter a positive number, or press enter/return to exit: ") # Prompt & Input

        while number != "": # While not empty, run program

            if number.isdigit():            

                number = float(number)

                if number == 0 or number < 0: # If number is 0 or less than 0, error
                    print("Cannot enter 0 or a negative number.")

                    number = input("Enter a positive number, or press enter/return to exit: ") # Reprompt & Input

                else:
                    
                    estimate = newton(number) # call function that returns estimate
                    
                    print("Estimate: " + str(estimate)) # Output/Display estimate

                    number = input("Enter a positive number, or press enter/return to exit: ") # Reprompt & Input

            else: # Error, not digit
                number = input("Please input a positive number, or press enter/return to exit: ") # Reprompt & Input
                

if __name__ == "__main__":
        main()


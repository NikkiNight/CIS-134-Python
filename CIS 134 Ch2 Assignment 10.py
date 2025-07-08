"""
Program: CIS 134 Ch2 Assignment 10.py
Author: Nicola Ward
Last Date Modified: 2/9/2024

The purpose of this program is to prompt the user to input their
hourly wage, total amount of regular hours worked and total overtime
hours worked. Then calculate the total weekly pay and display it.
The inputs are of type float representing hourly wage and hours worked.
The output is a string representing total weekly pay.
"""

#Inputs
hourlyWage = float(input("Enter hourly wage: "))
totalRegularHours = float(input("Enter regular hours: "))
totalOvertimeHours = float(input("Enter overtime hours: "))

#Calculations
overtimePay = totalOvertimeHours * (hourlyWage * 1.5)
totalWeeklyPay = hourlyWage * totalRegularHours + overtimePay

#Output
print("Total weekly pay: $" + str(totalWeeklyPay))

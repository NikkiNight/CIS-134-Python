"""
Program: CIS 134 Ch7 Assignment 1.py
Author: Nicola Ward
Last Date Modified: 3/29/2024

The purpose of this program is to draw a circle using the Turtle class and
its methods. The function drawCircle takes the turtle object, the circle's
center point and the circle's radius as augments. The algorithm draws the
circle's circumference by turning 3 degrees and moving a given distance
120 times.
"""

from math import pi
from turtle import Turtle

# Create Turtle Object
t = Turtle()

# Declarations
centerPoint = (50, 50)
radius = 50

# Function
def drawCircle(t, centerPoint, radius):
    degrees = 3

    t.up()
    t.goto(centerPoint)
    t.setheading(degrees)
    t.down()
    
    for count in range(120):
        # Calculate Distance Moved
        distanceMoved = 2.0 * pi * radius / 120.0
        
        t.forward(distanceMoved)
        t.left(degrees)

# Call Function
drawCircle(t, centerPoint, radius)

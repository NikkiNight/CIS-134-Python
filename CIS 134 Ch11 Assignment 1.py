"""
Author: Nicola Ward
File: CIS 134 Ch11 Assignment 1.py
Last Date Modified: 27/4/2024

Modified sequential search to halt after the target is found.
Returns the position of the target if found, if not, returns -1.
"""
# Test Lists
#lyst = [1, 2, 3, 5, 4, 6] # Average Case, O(n + 1) / 2
#lyst = [5, 1, 2, 3, 4, 6] # Best Case, O(1)
lyst = [1, 2, 3, 4, 6, 7] # Worst Case, O(n)
target = 5

# Sequential Search Function
def sequentialSearch(target, lyst):
    position = 0
    found = False # Not Found

    while position < len(lyst) and not found:
        if lyst[position] == target:
            found = True # Target Found
            return position
        else:
            position += 1
    return -1 # Not Found

# Big-O Notation
"""
Worst Case: O(n) Item isnt in the list.

Average Case: (n + 1)/2 Sum each iteration required at each posible position
and divide the sum by 2.

Best Case: O(1) Item is found in the first position.
"""

result = sequentialSearch(target, lyst)
print(result) # Print Target Position Or -1 If Not Found

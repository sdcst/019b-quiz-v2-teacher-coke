#!python3
"""
Fix this program.
It should ask the user to enter in 10 numbers and see
if the number is positive or negative
"""
for i in range(10):
    n = float(input("Enter in a number: "))
    if n > 0:
        print('that is a positive number')
    elif n < 0:
        print('that is a negative number')

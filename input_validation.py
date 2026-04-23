"""
Ogechukwu Okereke
CSMCS 111
Week 11 assignment4
"""
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print("You entered:", number)
except ValueError:
    print("Invalid input. Please enter a valid number.")
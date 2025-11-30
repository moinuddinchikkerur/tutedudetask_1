# Task 1: Perform Basic Mathematical Operations
# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# 3.  Displays the results of each operation on the screen.

input1 = float(input("Enter the first number: "))
input2 = float(input("Enter the second number: "))
addition = input1 + input2
subtraction = input1 - input2
multiplication = input1 * input2
division = input1 / input2 if input2 != 0 else "Undefined (cannot divide by zero)"
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")




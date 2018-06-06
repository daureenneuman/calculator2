"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    user_input = input("> ")
    if user_input == "q":
        break

    numbers = user_input.split(" ")
    func = numbers[0]
    num1 = float(numbers[1])

    if func != "square" and func != "cube":
            num2 = float(numbers[2])

    if func == "+":
        print(add(num1, num2))
    elif func == "-":
        print(subtract(num1, num2))
    elif func == "*":
        print(multiply(num1, num2))
    elif func == "/":
        print(divide(num1, num2))
    elif func == "square":
        print(square(num1))
    elif func == "cube":
        print(cube(num1))
    elif func == "pow":
        print(power(num1, num2))
    elif func == "mod":
        print(mod(num1, num2))


# Your code goes here

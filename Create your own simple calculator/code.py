from art import calc_logo
from math import sqrt
def add(n1, n2):
    return n1 + n2
def subtract (n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operation = {"+": add, "-": subtract, "*": multiply, "/" : divide}


def calculator():
    print(calc_logo)
    num1 = float(input("What is the first number?"))
    wish_to_continue = True
    while wish_to_continue:
        for sign in operation:
            print(sign)
        operation_symbol = input("Pick out a operation you want to perform from the line above: ")

        num2 = float(input("What is the next number?"))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"The result of {num1} {operation_symbol} {num2}  = {answer}")
        proceed = input("Do you wish to continue? Type 'y' or 'n' or 's' to start a new calc").lower()
        if proceed not in ['y', 'n', 's']:
            print("Please provide a valid response")
            proceed = input("Do you wish to continue? Type 'y' or 'n' or 's' to start a new calc").lower()
        
        if proceed == 'y':
            num1 = answer
        elif proceed == 'n':
            wish_to_continue = False
        elif proceed == 's':
            wish_to_continue = False
            calculator()
calculator()

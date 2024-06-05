# 1. The Calculator App
# Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation, with parameters for two numbers to be used in the operation. 

def addition (num1,num2):
    return num1 + num2

def subtraction (num1,num2):
    return num1 - num2

def multiplication (num1,num2):
    return num1 * num2

def division (num1,num2):
    if num2 == 2:
        return "Error: Cannot divide by zero."
    return num1 / num2

# Task 2: Implement user input to receive numbers and an operation choice, their response for operation should call the associated function


def calculation ():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation_choice = input ("Enter operation: 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division: ")

    result = perform_operation (operation_choice, num1, num2)

    print (f"The result is: {result}")


def perform_operation (operation_choice, num1, num2):
    if operation_choice == '1':
        return addition (num1, num2)
    elif operation_choice == '2':
        return subtraction (num1, num2)
    elif operation_choice == '3':
        return multiplication (num1, num2)
    elif operation_choice == '4':
        return division (num1, num2)
    else:
        return "Invalid operation choice."

calculation()

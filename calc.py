#this is a calculator project

num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))

operator = input("Enter operator: ")

def add(num1,num2):
    result = num1 + num2
    return result

def subtract(num1,num2):
    result = num1 - num2
    return result

def divide(num1,num2):
    result = num1 / num2
    return result

def multiply(num1,num2):
    result  = num1 * num2
    return result
    

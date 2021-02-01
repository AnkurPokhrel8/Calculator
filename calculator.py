# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:42:06 2021

@author: Ankur Pokhrel

Python code for making a calculator in python
"""
import math

class Calculator:
    
    def __init__(self):                    
        print("Welcome to my calculator")
        
    def addition(self, num1, num2):
        return num1+num2
    def difference(self, num1, num2):
        return num1-num2
    def product(self, num1, num2):
        return num1*num2
    def quotient(self, num1, num2):
        return num1/num2
    def power(self, num1, num2):
        return math.power(num1, num2)
    def squareroot(self, num1):
        return math.isqrt(num1)
    def factorial(self, num1):
        return math.factorial(num1)
        
calculator = Calculator()

while True:
    print("Enter 1 for addition")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")
    print("Enter 5 for raising to a power")
    print("Enter 6 for squareroot")
    print("Enter 7 for factorial")
    print("Enter 'quit' for ending the program")
    action = input("What do you want to do? ")
    
    if action=='quit':
        break
    
    if action=="1" or action=="2" or action=="3" or action=="4" or action=="5":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        if action=="1":
            print(calculator.addition(num1,num2))
        elif action=="2":
            print(calculator.difference(num1, num2))
        elif action=="3":
            print(calculator.product(num1,num2))
        elif action=="4":
            print(calculator.quotient(num1,num2))
        else:
            print(calculator.power(num1,num2))
    else:
        num = int(input("Enter the number: "))
        if action=="6":
            print(calculator.squareroot(num))
        else:
            print(calculator.factorial(num))

print("Program ended")
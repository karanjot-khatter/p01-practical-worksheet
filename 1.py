#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     11/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Q1
def sayName():

    print("karanjot khatter")

sayName()

#Q2
def sayHello2():
    print("Hello")
    print("World")

sayHello2()

#Q3
def euros2pounds():

    print("This programs converts an amount in euros to pounds")
    euros = eval(input("Enter the amount of euros you have:"))
    conversion = euros /1.15
    print(euros, "euros", "converts to: ", conversion, "pounds")
euros2pounds()

#Q4

def addUp():
    print("Program add 2 user inputs")
    number1 = eval(input("Please enter the first value:"))
    number2 = eval(input("Please enter the second value:"))
    sum = number1 + number2
    print(sum)
addUp()

#Q5

def changeCounter():
    print("This program displays the total amount of money in pence")
    onePence = eval(input("Please enter the amount of 1p coins:"))
    twoPence = eval(input("Please enter the amount of 2p coins:"))
    fivePence = eval(input("Please enter the amount of 1p coins:"))
    onePenceTotal = onePence * 1
    twoPenceTotal = twoPence * 2
    fivePenceTotal = fivePence * 5
    Total = onePenceTotal + twoPenceTotal + fivePenceTotal
    print("The total amount of money is: ", Total, "pence" )

changeCounter()

#Q6

def tenHellos():
    for i in range(10):
        print("Hello,world!")

tenHellos()

# Q7

def count():
    for i in range(10):
        print(i+1)

count()

# Q8

def weightsTable():
    print("Kilograms and pounds chart")
    kilograms = -10
    for i in range(11):
        kilograms = kilograms + 10
        pounds = kilograms * 2.2
        print("|", kilograms, "kilograms |", pounds, "pounds|")

weightsTable()

#Q9

def futureValue():
    initalValue = eval(input("Please enter the intial value:"))
    years = eval(input("Enter the number of years to be invested:"))
    interestRate = 5.5
    for i in range(years):
        initalValue = initalValue + (1+interestRate/years)
        print("In year:", i+1, ", you get:", initalValue)

futureValue()
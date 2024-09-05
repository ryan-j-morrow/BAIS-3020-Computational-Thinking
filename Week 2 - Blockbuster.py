# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 09:51:10 2024

@author: oamin
"""

x = 15
y = 4

# Addition

print("X+Y=",x+y)

# Multiplication

print("X*Y=",x*y)

# Exponentiation

print("X^Y=",x**y)

a = 10
b = 15

# Is 'a' less than or equal to 'b'?

print("Is a less than or equal to b?",a<=b)


# Temperature Example if statement
temperature = 35

if temperature < 32:
    print("The temperature of", temperature, "degrees is below freezing")
else:
    print("The temperature of", temperature, "degrees is not below freezing")


# Problem: Check if the entered password matches the correct password

correct_password = "IowaHawks2024!"
attempted_password = ""
while attempted_password != correct_password:
    attempted_password = input("Please enter your password: ")
    if attempted_password != correct_password:
        print("ERROR: This password is incorrect, please try again")
    else:
        print("Password is correct, welcome to your account")
    
# Problem: Check if someone is old enough to enter a restricted area (e.g., 18+)

age = int(input("How old are you? "))
          
if age >= 18:
    print("You are old enough to enter this area, welcome.")
else:
    print("You are not old enough to enter this area, please try again in", 18 - age, "years.")
    
    
# Input the name of the movie, its budget, and box office sales

movie = input("What is the name of the movie you would like to analyze? ")
budget = float(input("In millions of dollars, what was the budget of the movie? M$"))
sales = float(input("In millions of dollars, what was the total box office sales of the movie? M$"))

# Calculate the sales multiplier 

#sales_multiplier = sales / budget

sales_multiplier = sales / budget

# Determine if the movie was a hit or bomb based on the sales multiplier

if round(sales_multiplier,1) >= 3.0:
    print("The total sales of this movie was", sales, "(M$), the budget was", budget, "(M$), this makes it a Blockbuster Hit.")
elif round(sales_multiplier,1) <= 1.5:
    print("The total sales of this movie was", sales, "(M$), the budget was", budget, "(M$), this makes it a Blockbuster Bomb.")
else:
    print("The total sales of this movie was", sales, "(M$), the budget was", budget, "(M$), this makes it an average performing movie.")

# Print the return of investment for the movie

profit = sales - budget
roi = (profit/budget)*100
roi_str = str(round(roi,2))+"%"
print("The ROI of", movie, "was", roi_str+".")

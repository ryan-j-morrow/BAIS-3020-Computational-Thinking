# Question 1: Print "Hello, Spyder" in the console.
print("Hello, Spyder")
# Question 2: Print the result of 5 + 3 in interactive mode vs. in a script.
print("Script Mode: The sum of your numbers is ",5+3)
a = float(input("What is the first number you are adding? "))
b = float(input("What is the second number you are adding? "))
c = a+b
print("Interactive Mode: The sum of your numbers is ", c)
# Question 3: Ask for a user's name and print a greeting.
name = input("What is your name? ")
print("Good evening ", name, " it is good to meet you.")
# Question 4: Store the number 10 in a variable and print it.
x = 10
print(x)
# Question 5: Calculate and print the product of 7 and 8.
a = 7
b = 8
c = a+b
print(c)
# Question 6: Show the difference between adding numbers and adding strings.
a = "string a"
b = "string b"
c = a+b
d = 7
e = 8
f = d+e
print("String 1 is ", a)
print("String 2 is ", b)
print("Number 1 is ", d)
print("Number 2 is ", e)
print("Adding String 1 and String 2 gives us a result of ", c, " while adding Number 1 and Number 2 gives us a result of ", f)
# Question 7: Convert the string "123" to an integer and add 7 to it.
a = int("123")
b = 7
c = a+b
print(c)
# Question 8: Calculate the area of a rectangle from user input.
l = float(input("What is the length of the rectangle? "))
h = float(input("What is the height of the rectangle? "))
a = l*h
print("The area of this rectangle is ", a, " square units")
# Calculate total interest to be paid on a student loan over the course of a loan period
# Total Interest = Principal * (annual rate / 100) * years
p = float(input("What is the principal amount on the loan in $? "))
r = float(input("What is the annual rate on the loan in %? "))
y = float(input("WHow many years is the loan for? "))
i = p*(r/100)*y
print("The total interest on this loan is $",i)

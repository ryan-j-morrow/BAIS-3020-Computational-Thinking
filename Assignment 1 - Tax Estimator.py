# -*- coding: utf-8 -*-
"""
Authors: Ryan Morrow
Progran: Assignment 1 - Tax Estimator.py
Last date modified: 9/5/2024
The purpose of this program is to estimate Iowa State Income Tax and Federal Income Tax amounts for 2024.
This was created under the specifications of Assignment 1 in BAIS:3020 Computational Thinking course at The University of Iowa.
Fall 2024 Semester
Inputs: Filing Status, Annual Income, Partner's Annual Income (if applicable).
Outputs: Iowa State Income Tax Amount, Federal Income Tax Amount, Total Income Tax Amount.
Variables:
mfj = boolean variable indicating tax filing status of the user, true means the user is filing married-jointly, false means the user is filing single.
income1 = float variable storing the annual income of the user if mfj is true.
income2 = float variable storing the annual income of the user's partner if mfj is true.
income2 = float variable storing the annual income of the user if mfj is false and storing the combined income of the user and their partner if mfj is true.
federal_income = float variable storing the annual income of the user if mfj is false and storing the combined income of the user and their partner if mfj is true less the applicable standard deduction.
state_tax = float variable estimating the user's 2024 Iowa State Income Tax payment.
federal_tax = float variable estimating the user's 2024 Federal Income Tax payment.
"""


#Asks the user a yes/no question regarding their tax filing status and converts that to a Married-Filing Jointly flag variable.
mfj = input("If you are married filing jointly type 'Yes';\n Otherwise, type 'No'. ") == "Yes"

#Branch to calculate User's tax payments based off the MFJ tax tables.
if mfj == True:
    
    #Collects User's Income Data
    income1 = float(input("What was your annual income for 2024 (e.g. 25000)? $"))
    income2 = float(input("What was your partner's annual income for 2024 (e.g. 25000)? $"))
    income = income1 + income2
    
    #Calculates User's Federally Taxable Income (income less standard deduction).
    if income - 29200 < 0:
        federal_income = 0
    else:
        federal_income = income - 29200
    
    #Calculates User's State Tax Payment
    if income <= 12420:
        state_tax = 0 + (.044*income)
    elif income <= 62100:
        state_tax = 546.48 + (.0482*(income-12420))
    else:
        state_tax = 2941.06 + (.0570*(income-62100))


    #Calculates User's Federal Tax Payment
    if income <= 23200:
        federal_tax = 0 + (.10*federal_income)
    elif income <= 94300:
        federal_tax = 2320 + (.12*(federal_income-23200))
    elif income <= 201050:
        federal_tax = 10852 + (.22*(federal_income-94300))
    elif income <= 383900:
        federal_tax = 34337 + (.24*(federal_income-201050))
    elif income <= 487450:
        federal_tax = 78221 + (.32*(federal_income-383900))
    elif income <= 731200:
        federal_tax = 111357 + (.35*(federal_income-487450))
    else:
        federal_tax = 196669.50 + (.37*(federal_income-731200))





#Branch to calculate User's tax payments based off the Single tax tables.
else:
    
    #Collects User's income data.
    income = float(input("What was your annual income for 2024 (e.g. 25000)? $"))
        
    #Calculates User's Federally Taxable Income (income less standard deduction).
    if income - 14600 < 0:
        federal_income = 0
    else:
        federal_income = income - 14600
   
    #Calculates User's State Tax Payment.
    if income <= 6210:
        state_tax = 0 + (.044*income)
    elif income <= 31050:
        state_tax = 273.24 + (.0482*(income-6210))
    else:
        state_tax = 1470.53 + (.0570*(income-3150))


    #Calculates User's Federal Tax Payment.
    if income <= 11600:
        federal_tax = 0 + (.10*federal_income)
    elif income <= 47150:
        federal_tax = 1160 + (.12*(federal_income-1160))
    elif income <= 100525:
        federal_tax = 5426 + (.22*(federal_income-47150))
    elif income <= 191950:
        federal_tax = 17168.50 + (.24*(federal_income-100525))
    elif income <= 243725:
        federal_tax = 39110.50 + (.32*(federal_income-191950))
    elif income <= 609350:
        federal_tax = 55678.50 + (.35*(federal_income-243725))
    else:
        federal_tax = 183647.25+ (.37*(federal_income-609350))

#Calculates total tax payment, rounds all tax payments to the nearest dollar, outputs all 3 tax payment ammounts.
print("Your state tax owed for Iowa in 2024 was $"+str(round(state_tax)))
print("Your federal tax owed for 2024 was $"+str(round(federal_tax)))       
print("Your state tax owed for 2024 was $"+str(round(state_tax+federal_tax)))               
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:20:36 2024

@author: rjmorrow
"""

status_raw = input("If you are married filing jointly type 'Yes'; Otherwise, type 'No'.")
mfj = status_raw == "Yes"
if mfj == True:
    income1 = float(input("What is your annual income? $"))
    income2 = float(input("What is your partner's annual income? $"))
    income = income1 + income2
    if income <= 12420:
        state_tax = 0 + (.044*income)
    elif income < 62100:
        state_tax = 546.48 + (.0482*(income-12420))
    else:
        state_tax = 2941.06 + (.0570*(income-62100))
    print("Your State Tax Owed Is $"+str(round(state_tax,2)))        
else:
    income = float(input("What is your annual income? $"))
    if income <= 6210:
        state_tax = 0 + (.044*income)
    elif income < 31050:
        state_tax = 273.24 + (.0482*(income-6210))
    else:
        state_tax = 1470.53 + (.0570*(income-3150))
    if income <= 11600:
        federal_tax = 0 + (.044*income)
    elif income < 47150:
        federal_tax = 273.24 + (.0482*(income-1160))
    elif income < 100525:
        federal_tax = 273.24 + (.0482*(income-47150))
    elif income < 191950:
        federal_tax = 273.24 + (.0482*(income-100525))
    elif income < 243725:
        federal_tax = 273.24 + (.0482*(income-191950))
    elif income < 609350:
        federal_tax = 273.24 + (.0482*(income-243725))
    else:
        federal_tax = 1470.53 + (.0570*(income-609350))
    print("Your State Tax Owed Is $"+str(round(state_tax,2)))        
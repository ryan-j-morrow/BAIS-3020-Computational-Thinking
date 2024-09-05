# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:20:36 2024

@author: rjmorrow
"""

mfj = input("If you are married filing jointly type 'Yes';\n Otherwise, type 'No'. ") == "Yes"

if mfj == True:
    
    income1 = float(input("What was your annual income for 2024 (e.g. 25000)? $"))
    income2 = float(input("What was your partner's annual income for 2024 (e.g. 25000)? $"))
    income = income1 + income2
    
    
    if income <= 12420:
        state_tax = 0 + (.044*income)
    elif income <= 62100:
        state_tax = 546.48 + (.0482*(income-12420))
    else:
        state_tax = 2941.06 + (.0570*(income-62100))



    if income <= 23200:
        federal_tax = 0 + (.10*income)
    elif income <= 94300:
        federal_tax = 2320 + (.12*(income-23200))
    elif income <= 201050:
        federal_tax = 10852 + (.22*(income-94300))
    elif income <= 383900:
        federal_tax = 34337 + (.24*(income-201050))
    elif income <= 487450:
        federal_tax = 78221 + (.32*(income-383900))
    elif income <= 731200:
        federal_tax = 111357 + (.35*(income-487450))
    else:
        federal_tax = 196669.50 + (.37*(income-731200))





else:
    
    income = float(input("What was your annual income for 2024 (e.g. 25000)? $"))
   
   
    if income <= 6210:
        state_tax = 0 + (.044*income)
    elif income <= 31050:
        state_tax = 273.24 + (.0482*(income-6210))
    else:
        state_tax = 1470.53 + (.0570*(income-3150))



    if income <= 11600:
        federal_tax = 0 + (.10*income)
    elif income <= 47150:
        federal_tax = 1160 + (.12*(income-1160))
    elif income <= 100525:
        federal_tax = 5426 + (.22*(income-47150))
    elif income <= 191950:
        federal_tax = 17168.50 + (.24*(income-100525))
    elif income <= 243725:
        federal_tax = 39110.50 + (.32*(income-191950))
    elif income <= 609350:
        federal_tax = 55678.50 + (.35*(income-243725))
    else:
        federal_tax = 183647.25+ (.37*(income-609350))


print("Your state tax owed for Iowa in 2024 was $"+str(round(state_tax)))
print("Your federal tax owed for 2024 was $"+str(round(federal_tax)))       
print("Your state tax owed for 2024 was $"+str(round(state_tax)+round(federal_tax)))               